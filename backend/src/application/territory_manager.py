import json

class TerritoryManager:
    def __init__(self, territory_rules_path: str):
        with open(territory_rules_path, 'r', encoding='utf-8') as f:
            self.territory_data = json.load(f)

    def get_contacts_for_structures(self, eligible_structures: list, city: str | None):
        """
        Pour chaque structure éligible, récupère les coordonnées locales.
        En mode de test interactif, lance automatiquement la validation humaine.
        """
        import sys
        
        # Détection si on est dans un script de test de simulation interactif
        is_test_run = any(arg.endswith('.py') and ('test_' in arg or 'tests_simulation' in arg) for arg in sys.argv)
        
        if is_test_run and hasattr(sys.stdin, 'isatty') and sys.stdin.isatty():
            from ai.extraction.extractor import SignalExtractor
            if SignalExtractor.last_extracted_data is not None:
                return self._run_interactive_loop(eligible_structures, city, SignalExtractor.last_extracted_data)
                
        return self.get_contacts_for_structures_non_interactive(eligible_structures, city)

    def get_contacts_for_structures_non_interactive(self, eligible_structures: list, city: str | None):
        """Récupère les fiches contacts réelles sans boucle interactive (utilisé en prod/API)."""
        if not city:
            return eligible_structures

        area_data = self._find_area(city)
        if not area_data:
            return eligible_structures

        available_local_structures = area_data.get("structures_disponibles", {})

        results = []
        for struct in eligible_structures:
            struct_copy = struct.copy()
            struct_type = struct_copy["structure_type"]
            
            local_info = available_local_structures.get(struct_type)
            
            # LOGIQUE DE RELAIS : Si CLIC absent -> Redirection directe vers UTS
            if struct_type == "CLIC" and (not local_info or not local_info.get("present")):
                uts_info = available_local_structures.get("UTS")
                if uts_info and uts_info.get("present"):
                    struct_copy["label"] = f"{uts_info.get('nom', 'UTS')} (Relais CLIC)"
                    struct_copy["objectif"] = f"La commune ne dispose pas de CLIC, se rapprocher de l'UTS. {struct_copy.get('objectif', '')}"
                    local_info = uts_info
            
            if local_info and local_info.get("present"):
                struct_copy["nom_local"] = local_info.get("nom")
                struct_copy["telephone"] = local_info.get("telephone")
                struct_copy["email"] = local_info.get("email")
                struct_copy["adresse"] = local_info.get("adresse")
                
            results.append(struct_copy)

        return results

    def _run_interactive_loop(self, eligible_structures: list, city: str | None, extracted_data: dict):
        """Boucle interactive en ligne de commande pour guider le travailleur social et affiner l'éligibilité."""
        import os
        from application.scoring_engine import ScoringEngine
        from application.orientation_engine import OrientationEngine
        from application.clarification_engine import ClarificationEngine
        from ai.extraction.extractor import SignalExtractor
        
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        COMID_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'COMID.json')
        ORIENTATION_RULES_PATH = os.path.join(BASE_DIR, 'config', 'rules', 'orientation_rules.json')
        
        scoring_engine = ScoringEngine(comid_rules_path=COMID_PATH)
        orientation_engine = OrientationEngine(rules_path=ORIENTATION_RULES_PATH)
        clarification_engine = ClarificationEngine()
        
        # 1. Affichage de la première proposition brute
        print("\n=====================================================================")
        print(" ORIA - PREMIERE PROPOSITION D'ORIENTATION (BASE IA DE DEPART)")
        print("=====================================================================")
        
        initial_contacts = self.get_contacts_for_structures_non_interactive(eligible_structures, city)
        if not initial_contacts:
            print("Aucune structure éligible détectée au départ.")
        else:
            for struct in initial_contacts:
                print(f"\n[ {struct['label']} ] - Priorité : {struct['priorite']}")
                print(f"Objectif : {struct['objectif']}")
                if struct.get("telephone") or struct.get("adresse"):
                    print(f"Contact : {struct.get('telephone', 'N/A')} | {struct.get('adresse', 'N/A')}")
                else:
                    print("Contact : Non trouvé dans le référentiel territorial")
        print("=====================================================================\n")
        
        # 2. Récupération des questions de clarification
        questions = clarification_engine.get_clarification_questions(extracted_data, initial_contacts, SignalExtractor.last_text)
        
        if not questions:
            print(" Toutes les informations critiques sont complètes. Aucune clarification requise.")
            return initial_contacts
            
        print(" Des informations critiques manquent pour affiner et valider l'orientation.")
        print("Lancement de la validation humaine en temps réel...\n")
        
        current_data = {**extracted_data}
        new_contacts = initial_contacts
        
        for q in questions:
            field = q["champ"]
            libelle = q["libelle"]
            question_text = q["question"]
            impact = q["impact"]
            
            print(f"\n [?] {libelle} : {question_text}")
            print(f"      Impact : {impact}")
            
            while True:
                try:
                    user_input = input("      Votre réponse (oui / non / je ne sais pas) : ").strip().lower()
                except (KeyboardInterrupt, EOFError):
                    print("\n   [Interruption] Fin de la session interactive.")
                    return new_contacts
                
                # Validation des réponses spécifiques
                if field == "usager.situation_actuelle.GIR":
                    if user_input in ["je ne sais pas", "nsp", "inconnu", "unknown", ""]:
                        value = "inconnu"
                        break
                    try:
                        val_int = int(user_input)
                        if 1 <= val_int <= 6:
                            value = val_int
                            break
                        else:
                            print("      Veuillez saisir un chiffre de 1 à 6, ou 'je ne sais pas'.")
                    except ValueError:
                        print("      Veuillez saisir un chiffre de 1 à 6, ou 'je ne sais pas'.")
                        
                elif field == "usager.identite.age_estime":
                    if user_input in ["je ne sais pas", "nsp", "inconnu", "unknown", ""]:
                        value = None
                        break
                    try:
                        val_int = int(user_input)
                        if val_int > 0:
                            value = val_int
                            break
                        else:
                            print("      Veuillez saisir un âge valide, ou 'je ne sais pas'.")
                    except ValueError:
                        print("      Veuillez saisir un âge valide, ou 'je ne sais pas'.")
                        
                else:
                    if user_input in ["oui", "o", "yes", "y", "true"]:
                        value = "oui"
                        break
                    elif user_input in ["non", "n", "no", "false"]:
                        value = "non"
                        break
                    elif user_input in ["je ne sais pas", "nsp", "inconnu", "unknown", ""]:
                        value = "inconnu"
                        break
                    else:
                        print("      Veuillez répondre par 'oui', 'non' ou 'je ne sais pas'.")
            
            # Application de la réponse
            if value != "inconnu" and value is not None:
                current_data[field] = value
                print(f"      Donnée enregistrée : {value}")
            else:
                current_data[field] = "inconnu" if isinstance(value, str) else None
                print("      Donnée laissée comme non définie (je ne sais pas).")
                
            # Recalcul en temps réel
            new_comid = scoring_engine.calculate_comid_score(current_data)
            new_orientations = orientation_engine.evaluate_orientation(current_data, new_comid)
            new_contacts = self.get_contacts_for_structures_non_interactive(new_orientations, city)
            
            print(f"\n      Recalcul : Score COMID = {new_comid['score_total']} ({new_comid['label']})")
            print("      Orientations affinées en temps réel :")
            if not new_contacts:
                print("      - Aucune structure éligible à ce stade.")
            else:
                for struct in new_contacts:
                    print(f"      - {struct['label']} (Priorité : {struct['priorite']})")
                    
        print("\n=====================================================================")
        print("🎉 VALIDATION INTERACTIVE COMPLETE ! ORIENTATION FINALE")
        print("=====================================================================")
        
        SignalExtractor.last_extracted_data = current_data
        
        return new_contacts

    def _find_area(self, city: str):
        """
        Trouve la clé correspondant à la ville dans le référentiel.
        Gère les correspondances simples pour le moment.
        """
        city_lower = city.lower()
        
        for area_name in self.territory_data.keys():
            if city_lower in area_name.lower():
                return self.territory_data[area_name]
        
        return None
