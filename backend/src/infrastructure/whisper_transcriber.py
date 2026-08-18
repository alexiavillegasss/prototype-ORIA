import os
import tempfile
import logging

logger = logging.getLogger(__name__)

class WhisperTranscriber:
    def __init__(self):
        self.api_key = os.environ.get("OPENAI_API_KEY")
        self.client = None
        self.local_model = None

        if self.api_key:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=self.api_key)
            except Exception as e:
                logger.warning(f"Impossible d'initialiser le client OpenAI: {e}")

        if not self.client:
            try:
                from faster_whisper import WhisperModel
                logger.info("Chargement du modèle local faster-whisper (tiny)...")
                self.local_model = WhisperModel("tiny", device="cpu", compute_type="int8")
                logger.info("Modèle local faster-whisper prêt !")
            except Exception as e:
                logger.warning(f"Impossible de pré-charger faster-whisper: {e}")

    def transcribe_audio_bytes(self, audio_bytes: bytes, filename: str = "audio.webm") -> str:
        """Transcrit les octets audio en texte français haute précision via Whisper."""
        suffix = os.path.splitext(filename)[1] or ".webm"
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(audio_bytes)
            tmp_path = tmp.name

        try:
            # 1. API Cloud OpenAI si la clé est renseignée
            if not self.client and os.environ.get("OPENAI_API_KEY"):
                self.api_key = os.environ.get("OPENAI_API_KEY")
                try:
                    from openai import OpenAI
                    self.client = OpenAI(api_key=self.api_key)
                except Exception as e:
                    logger.error(f"Erreur d'instanciation client OpenAI: {e}")

            if self.client:
                with open(tmp_path, "rb") as audio_file:
                    response = self.client.audio.transcriptions.create(
                        model="whisper-1",
                        file=audio_file,
                        language="fr",
                        prompt="Dictée médicale et médico-sociale en français : situation de personne âgée, autonomie, GIR, APA, chutes, aidant, hospitalisation, maintien à domicile."
                    )
                    return response.text.strip()
            
            # 2. Utilisation du modèle pré-chargé faster-whisper local
            if self.local_model:
                segments, _ = self.local_model.transcribe(
                    tmp_path, 
                    language="fr", 
                    initial_prompt="Dictée médicale et médico-sociale en français : situation de personne âgée, autonomie, GIR, APA, chutes, aidant, hospitalisation."
                )
                text = " ".join([segment.text for segment in segments])
                return text.strip()

            # 3. Fallback instanciation dynamique
            try:
                from faster_whisper import WhisperModel
                model = WhisperModel("tiny", device="cpu", compute_type="int8")
                segments, _ = model.transcribe(tmp_path, language="fr")
                text = " ".join([segment.text for segment in segments])
                return text.strip()
            except Exception as e:
                logger.error(f"Erreur transcription local: {e}")

            raise RuntimeError("Aucun moteur Whisper disponible.")

        finally:
            if os.path.exists(tmp_path):
                try:
                    os.remove(tmp_path)
                except Exception:
                    pass
