import asyncio
import os
import sys
import json

# Ajout du chemin pour importer les modules du backend
sys.path.append(os.path.join(os.getcwd(), 'backend', 'src'))

from ai.extraction.extractor import SignalExtractor

async def run_test():
    BASE_DIR = os.getcwd()
    SCHEMA_PATH = os.path.join(BASE_DIR, 'config', 'schemas', 'schema_definition.json')
    COMID_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'COMID.json')

    print("--- Lancement du test de précision du besoin principal ---")
    
    extractor = SignalExtractor(schema_path=SCHEMA_PATH, comid_path=COMID_PATH)

    scenarios = [
        {
            "name": "Cas A (Besoin clair : Renoncement aux soins)",
            "text": "M. Jean, 78 ans, vit seul à Toulon. L'infirmière libérale signale qu'il s'oppose activement à toute prise en charge. Il refuse catégoriquement de la laisser entrer pour faire ses pansements et crie sur les soignants.",
            "expected": "Renoncement aux soins"
        },
        {
            "name": "Cas B (Aucun besoin clair : indetermine)",
            "text": "Mme Yvonne, 85 ans, vit seule à La Seyne-sur-Mer. L'infirmière passe deux fois par semaine pour surveiller sa tension. Mme Yvonne est parfois un peu fatiguée, mais elle ne formule aucune demande d'aide, accepte parfaitement la surveillance et n'a pas de problème financier ou de santé aigu.",
            "expected": "indetermine"
        },
        {
            "name": "Cas C (Besoins multiples d'intensité égale : indetermine)",
            "text": "M. Raymond, 82 ans, vit à Ollioules dans un grand dénuement. Son frigo est totalement vide et il n'a plus d'argent pour se nourrir. En parallèle, il refuse de recevoir l'aide à domicile que sa fille essaie de mettre en place, et refuse de prendre ses médicaments ou de voir son médecin pour ses douleurs.",
            "expected": "indetermine"
        }
    ]

    success_count = 0

    for i, scenario in enumerate(scenarios, 1):
        print(f"\n--- Scénario {i} : {scenario['name']} ---")
        print(f"Récit : \"{scenario['text']}\"")
        try:
            extracted_data = await extractor.extract(scenario['text'])
            besoin = extracted_data.get("demande.besoin_principal")
            conf = extracted_data.get("evaluation.confiance.variables", {}).get("motif", 0)
            
            print(f"Besoin extrait   : {besoin} (Confiance : {conf}%)")
            print(f"Besoin attendu   : {scenario['expected']}")
            
            if besoin == scenario['expected']:
                print("[OK] SUCCES")
                success_count += 1
            else:
                print("[KO] ECHEC")
                
        except Exception as e:
            import traceback
            print(f"Erreur d'extraction : {e}")
            traceback.print_exc()

    print("\n" + "="*50)
    print(f"Résultats finaux : {success_count}/{len(scenarios)} scénarios réussis.")
    print("="*50)

if __name__ == "__main__":
    asyncio.run(run_test())
