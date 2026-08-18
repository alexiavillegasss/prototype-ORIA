import os
import tempfile
import logging

logger = logging.getLogger(__name__)

class WhisperTranscriber:
    def __init__(self):
        self.api_key = os.environ.get("OPENAI_API_KEY")
        self.client = None
        if self.api_key:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=self.api_key)
            except Exception as e:
                logger.warning(f"Impossible d'initialiser le client OpenAI: {e}")

    def transcribe_audio_bytes(self, audio_bytes: bytes, filename: str = "audio.webm") -> str:
        """Transcrit les octets audio en texte français haute précision via Whisper."""
        suffix = os.path.splitext(filename)[1] or ".webm"
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(audio_bytes)
            tmp_path = tmp.name

        try:
            # 1. Utilisation de l'API Cloud OpenAI Whisper si la clé est présente
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
            
            # 2. Tentative avec faster-whisper local (Ultra rapide sur CPU)
            try:
                from faster_whisper import WhisperModel
                # Modèle 'base' ou 'tiny' en français sur CPU avec int8 pour un chargement rapide
                model = WhisperModel("base", device="cpu", compute_type="int8")
                segments, _ = model.transcribe(tmp_path, language="fr", initial_prompt="Dictée médicale et médico-sociale en français : situation de personne âgée, autonomie, GIR, APA, chutes, aidant, hospitalisation, maintien à domicile.")
                text = " ".join([segment.text for segment in segments])
                if text.strip():
                    return text.strip()
            except Exception as e1:
                logger.debug(f"Faster-whisper local non disponible ou erreur: {e1}")

            # 3. Tentative avec openai-whisper local
            try:
                import whisper
                model = whisper.load_model("base")
                result = model.transcribe(tmp_path, language="fr")
                return result.get("text", "").strip()
            except Exception as e2:
                logger.debug(f"Whisper local non disponible: {e2}")

            raise RuntimeError("Clé OPENAI_API_KEY non configurée et aucun paquet local Whisper (faster-whisper) disponible.")

        finally:
            if os.path.exists(tmp_path):
                try:
                    os.remove(tmp_path)
                except Exception:
                    pass
