import sys
import os
import asyncio
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend", "src")))
from ai.extraction.extractor import SignalExtractor
from application.scoring_engine import ScoringEngine
from application.orientation_engine import OrientationEngine

sys.stdout.reconfigure(encoding='utf-8')

text = "Je suis assistante sociale, j’accompagne un monsieur de 36 ans, vivant à Toulon d’origine Afghane présent en France depuis plus de 20 ans, profil très précarisé depuis son arrivée en France, soucis administratifs qui ne lui ont pas permis de solliciter le droit d’asile, soucis avec des employeurs, soucis financiers, surendettement, expulsion, locative, ancien toxicomane, dit avoir arrêté de consommer de manière autonome, a besoin d’être accompagné et soutenu dans son parcours de soins: pas de médecin traitant, soins dentaires, santé mentale. Monsieur a des capacités, il parle correctement français, mais peine à mener à bien ses démarches du fait de la démotivation et de la difficulty à faire valoir ses droits."

async def test():
    extractor = SignalExtractor(schema_path='config/schemas/schema_definition.json', comid_path='config/rules/COMID.json')
    scoring_engine = ScoringEngine(comid_rules_path='config/rules/COMID.json')
    orientation_engine = OrientationEngine(rules_path='config/rules/orientation_rules.json')
    
    extracted_data = await extractor.extract(text)
    comid_results = scoring_engine.calculate_comid_score(extracted_data)
    
    scores = {struct: 0 for struct in orientation_engine.structures}
    identified_needs = []
    text_lower = text.lower()
    
    for need in orientation_engine.needs_mapping:
        if orientation_engine._is_need_identified(need, extracted_data, text_lower):
            if len(need['structures_cochees']) > 0:
                identified_needs.append(need)
                for s in need['structures_cochees']:
                    if s in scores:
                        scores[s] += 1
                        
    print('Identified needs count:', len(identified_needs))
    temp_winner = max(scores, key=scores.get)
    print('temp_winner:', temp_winner)
    
    excluded_structures = []
    for rule in orientation_engine.exclusion_rules:
        detail = rule['detail']
        struct_type = rule['structure']
        if detail in orientation_engine.condition_map:
            checker = orientation_engine.condition_map[detail]
            if checker(extracted_data, extracted_data, text_lower):
                excluded_structures.append(struct_type)
                
    if 'COMPAGNONS_BATISSEURS' not in excluded_structures:
        insalubre_ok = extracted_data.get('usager.cadre_de_vie.etat_logement') in ['insalubre', 'diogene', 'incurie']
        logement_inadapte_ok = extracted_data.get('evaluation.comid.logement_inadapte') is True
        if not insalubre_ok and not logement_inadapte_ok:
            excluded_structures.append('COMPAGNONS_BATISSEURS')
            
    for s in excluded_structures:
        scores[s] = -9999
        
    print('Scores before redirect:', scores)
    
    # Check variables
    psych = extracted_data.get('evaluation.comid.psychiatrie')
    addict = extracted_data.get('evaluation.comid.addiction')
    dep = extracted_data.get('evaluation.comid.depression')
    
    print('psychiatrie in extracted_data:', psych, type(psych))
    print('addiction in extracted_data:', addict, type(addict))
    print('depression in extracted_data:', dep, type(dep))
    
    c1 = (temp_winner == 'UTS' and False)
    c2 = (len(identified_needs) > 5 and comid_results.get('score_total', 0) >= 6)
    c3 = False
    c4 = ((psych is True or addict is True or dep is True) and len(identified_needs) >= 4)
           
    print('c1 (cannot move):', c1)
    print('c2 (needs > 5 and comid >= 6):', c2)
    print('c3 (refusal):', c3)
    print('c4 (psych/addiction/dep >= 4):', c4)
    
    redirection_dac = c1 or c2 or c3 or c4
    print('redirection_dac:', redirection_dac)
    
    # CRT override check
    if scores.get('POLICE', 0) > 0 or scores.get('CEV', 0) > 0:
        redirection_dac = False
    elif scores.get('CRT', 0) > 0 and not (psych is True or addict is True or dep is True):
        redirection_dac = False
        
    print('redirection_dac after overrides:', redirection_dac)
    print('comid score_total:', comid_results.get('score_total'))
    
asyncio.run(test())
