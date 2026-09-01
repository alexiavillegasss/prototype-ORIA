import json

class TerritoryManager:
    def __init__(self, territory_rules_path: str):
        with open(territory_rules_path, 'r', encoding='utf-8') as f:
            self.territory_data = json.load(f)

    def get_contacts_for_structures(self, eligible_structures: list, city: str | None):
        """
        Pour chaque structure éligible, récupère les coordonnées locales.
        Gère les relais territoriaux (ex: CLIC absent -> UTS).
        """
        if not city:
            city = "La Garde"

        area_data = self._find_area(city)
        if not area_data:
            area_data = self._find_area("La Garde")

        if not area_data:
            return eligible_structures

        available_local_structures = area_data.get("structures_disponibles", {})

        results = []
        for struct in eligible_structures:
            # On travaille sur une copie pour ne pas polluer les autres tests
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
            
            # NUMÉROS NATIONAUX ET D'URGENCE INCONTOURNABLES
            emergency_phones = {
                "POLICE": "17",
                "SAMU": "15",
                "3919": "3919",
                "3977": "3977",
                "115": "115"
            }
            if struct_type in emergency_phones:
                struct_copy["telephone"] = emergency_phones[struct_type]

            if local_info and local_info.get("present"):
                struct_copy["nom_local"] = local_info.get("nom")
                if struct_type not in emergency_phones:
                    struct_copy["telephone"] = local_info.get("telephone")
                struct_copy["email"] = local_info.get("email")
                struct_copy["adresse"] = local_info.get("adresse")
                
            # Enrichissement de cpts_section (CPTS intégrée sous le CLIC)
            if struct_copy.get("cpts_section"):
                cpts_info = available_local_structures.get("CPTS")
                if cpts_info and cpts_info.get("present"):
                    struct_copy["cpts_section"]["nom_local"] = cpts_info.get("nom")
                    struct_copy["cpts_section"]["telephone"] = cpts_info.get("telephone")
                    struct_copy["cpts_section"]["email"] = cpts_info.get("email")
                    struct_copy["cpts_section"]["adresse"] = cpts_info.get("adresse")

            results.append(struct_copy)

        return results

    def _find_area(self, city: str):
        """
        Trouve la clé correspondant à la ville dans le référentiel en ignorant les accents.
        """
        import unicodedata
        
        def remove_accents(s):
            if not s:
                return ""
            return "".join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

        city_clean = remove_accents(city).lower()
        
        for area_name in self.territory_data.keys():
            area_clean = remove_accents(area_name).lower()
            if city_clean in area_clean:
                return self.territory_data[area_name]
        
        return None
