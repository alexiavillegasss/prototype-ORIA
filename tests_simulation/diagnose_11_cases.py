import os
import sys
import asyncio
import json

sys.path.append(os.path.join(os.getcwd(), 'backend', 'src'))

from ai.extraction.extractor import SignalExtractor
from application.scoring_engine import ScoringEngine
from application.orientation_engine import OrientationEngine

BASE_DIR = os.getcwd()
RULES_DIR = os.path.join(BASE_DIR, 'config', 'rules')
SCHEMA_PATH = os.path.join(BASE_DIR, 'config', 'schemas', 'schema_definition.json')
COMID_PATH = os.path.join(RULES_DIR, 'COMID.json')
ORIENTATION_RULES_PATH = os.path.join(RULES_DIR, 'orientation_rules.json')

extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH, model="llama3")
scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
engine.set_matrix("cassi")

cases = [
    {
        "id": "01-CEV",
        "expected": "CEV",
        "text": "Bonjour, je suis kinésithérapeute et j'intervient chez un Monsieur de 55 ans. Son voisin est très aidant mais je suspecte qu'il lui prenne de l'argent lors de ses passages. Je ne sais pas qui contacter pour faire un signalement pour protéger ce Monsieur. Merci pour votre aide."
    },
    {
        "id": "02-CLIC",
        "expected": "CLIC",
        "text": "Bonjour, je suis IDE. J'ai une tournée sur La Seyne-sur-Mer et j'ai un patient de 75 ans qui se dégrade beaucoup il aurait besoin d'aides à domicile. Merci pour votre aide."
    },
    {
        "id": "03-CRT",
        "expected": "CRT",
        "text": "Bonjour, je suis médecin et j'aurai besoin qu'un point global soit fait au domicile d'une patiente de 80 ans en GIR 4 parce que la situation se dégrade. Elle a déjà des aides au domicile mais je me demande si c'est suffisant. Madame et sa famille souhaiteraient retarder l'entrée en EHPAD mais je pense qu'il faudrait faire un accompagnement plus global des équipes qui sont déjà en place."
    },
    {
        "id": "04-CCAS",
        "expected": "CCAS",
        "text": "Bonjour, je suis IDE. J'ai une tournée sur Bandol et j'ai un patient de 92 ans qui ne peut plus faire ses courses seul et il est isolé sans famille ou amis sur Bandol. Ses enfants vivent à l'étranger. Qui est-ce que je peux contacter ? Merci pour votre aide."
    },
    {
        "id": "05-CPTS",
        "expected": "CPTS",
        "text": "Bonjour, je suis IDE. J'intervient j'ai un patient dont le MT vient de partir à la retraite et sa patientèle n'est pas reprise par un confrère. Il aurait besoin d'un médecin qui fasse des visites au domicile. Il a 84 ans et vit sur Toulon"
    },
    {
        "id": "06-DAC",
        "expected": "DAC",
        "text": "Bonjour, je vous appelle car je suis MT sur Six-Fours. J'ai un patient de 80 ans que j'accompagne depuis plusieurs années. Son état général se dégrade tant sur le plan psychologique que social pour la question du logement notamment. Je souhaite rester anonyme concernant mon signalement car je suis la seule professionnelle qui intervient encore auprès de ce Monsieur. Je ne sais pas vers qui me tourner pour signaler la situation de ce Monsieur. Ce Monsieur est paranoïaque donc il ne faut vraiment pas que mon nom ressorte."
    },
    {
        "id": "08-CLIC",
        "expected": "CLIC",
        "text": "Je suis neurologue à l’hôpital de la Timone, j’oriente un patient vivant à Toulon âgé de 77 ans, il vit seul depuis le décès de son épouse, il y a trois ans, il a une aphasie progressive et une démence fronto temporale. Nous avons mis en place infirmier libéral, kiné et Orthophoniste, monsieur oublie d’aller à ses rendez-vous. Il a des aides à domicile ponctuellement à titre payant pour ménage, accompagnement médicaux et sorties, il a deux filles une qui habite Paris une qui habite Marseille toutes les deux très prises par leur travail. Il n’a pas d’APA,"
    },
    {
        "id": "09-CRT",
        "expected": "CRT",
        "text": "Je suis infirmière libérale à Toulon. Je prends en charge un patient de 80 ans qui vit avec son épouse, Monsieur est en refus de soins et d’hospitalisation, souhaite rester à domicile malgré un état général qui se dégrade et des chutes à répétition, madame est épuisée, un contexte de conjugopathie est à signaler à domicile, nous poursuivons 1, passage par jour, mais nous ne pouvons pas réaliser tous les soins prescrits en raison du refus de monsieur. Madame a besoin d’être soutenue et accompagnée par une assistante sociale et un psychologue."
    },
    {
        "id": "10-CCAS",
        "expected": "CCAS",
        "text": "Je suis la fille d’une femme de 88 ans dont le maintien à domicile est devenu trop compliqué par sa perte d’autonomie et son isolement. Elle souhaite intégrer un EHPAD mais nous n’avons pas les moyens pour payer. Je souhaite faire une demande d’aide sociale à l’hébergement."
    },
    {
        "id": "11-CPTS",
        "expected": "CPTS",
        "text": "Je suis assistante sociale, j’accompagne une dame de 55 ans vivant à la Seyne-sur-Mer en situation de handicap. Madame n’a plus de médecin traitant depuis le départ à la retraite du dernier qui la suivait. Elle a besoin rapidement d’un suivi médical à domicile et d’un certificat MDPH pour le renouvellement de ses droits."
    },
    {
        "id": "12-UTS",
        "expected": "UTS",
        "text": "Je suis la sœur d’un homme de 44 ans, vivant à six fours, il a besoin d’un accompagnement pour des démarches administratives et une demande de logement social suite à la perte d’autonomie en lien avec un accident de la vie courante"
    },
    {
        "id": "13-DAC",
        "expected": "DAC",
        "text": "Je suis assistante sociale, j’accompagne un monsieur de 36 ans, vivant à Toulon d’origine Afghane présent en France depuis plus de 20 ans, profil très précarisé depuis son arrivée en France, soucis administratifs qui ne lui ont pas permis de solliciter le droit d’asile, soucis avec des employeurs, soucis financiers, surendettement, expulsion, locative, ancien toxicomane, dit avoir arrêté de consommer de manière autonome, a besoin d’être accompagné et soutenu dans son parcours de soins: pas de médecin traitant, soins dentaires, santé mentale. Monsieur a des capacités, il parle correctement français, mais peine à mener à bien ses démarches du fait de la démotivation et de la difficulté à faire valoir ses droits."
    }
]

CACHE_FILE = "tests_simulation/cache_11_extractions.json"

async def get_or_extract(c):
    cache = {}
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                cache = json.load(f)
        except:
            pass
    if c["id"] in cache:
        return cache[c["id"]]
    
    extracted_data = await extractor.extract(c["text"])
    cache[c["id"]] = extracted_data
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)
    return extracted_data

async def diagnose():
    print("=== DIAGNOSTIC DES 11 CAS ===")
    for c in cases:
        print(f"\n=======================================================")
        print(f"CASE {c['id']} | EXPECTED: {c['expected']}")
        print(f"TEXT: {c['text'][:100]}...")
        extracted_data = await get_or_extract(c)
        comid = scoring_engine.calculate_comid_score(extracted_data)
        
        # Test CASSI
        data_cassi = extracted_data.copy()
        res_cassi = engine.evaluate_orientation(data_cassi, comid, c["text"], matrix="cassi")
        top_cassi = res_cassi[0]["structure_type"] if res_cassi else "NONE"
        scores = data_cassi.get("evaluation.moteur_points.scores", {})
        needs = [n["detaille"] for n in data_cassi.get("evaluation.moteur_points.besoins_identifies", [])]
        prios = data_cassi.get("evaluation.moteur_points.priorisations_declenchees", [])
        exclus = data_cassi.get("evaluation.moteur_points.exclusions_declenchees", [])
        
        status = "[PASS]" if top_cassi == c["expected"] else "[FAIL]"
        print(f"RESULT: {top_cassi} vs {c['expected']} -> {status}")
        print(f"  Prios: {prios} | Exclus: {exclus}")
        print(f"  Top Scores: {sorted(scores.items(), key=lambda x: x[1], reverse=True)[:5]}")
        print(f"  Needs ({len(needs)}): {needs[:5]}")
        print(f"  Extracted Age: {extracted_data.get('usager.identite.age_estime')} | Motif: {extracted_data.get('demande.motif_principal')} | Adresseur: {extracted_data.get('adresseur.profession_ou_statut')}")

if __name__ == "__main__":
    asyncio.run(diagnose())
