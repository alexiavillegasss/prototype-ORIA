import json

class TerritoryManager:
    def __init__(self, territory_rules_path: str):
        with open(territory_rules_path, 'r', encoding='utf-8') as f:
            self.territory_data = json.load(f)

    def get_contacts_for_structures(self, eligible_structures: list, city: str | None):
        """
        Pour chaque structure éligible, récupère les coordonnées locales
        en fonction de la ville du patient.
        """
        if not city:
            return eligible_structures # On renvoie tel quel si pas de ville

        # Recherche de la zone géographique
        area_data = self._find_area(city)
        if not area_data:
            return eligible_structures

        available_local_structures = area_data.get("structures_disponibles", {})

        results = []
        for struct in eligible_structures:
            struct_type = struct["structure_type"]
            
            # Cas particulier pour les CLIC qui peuvent avoir des noms variés dans les règles
            search_key = struct_type
            if "CLIC" in struct_type:
                search_key = "CLIC"

            local_info = available_local_structures.get(search_key)
            
            if local_info and local_info.get("present"):
                # On enrichit l'objet avec les infos locales
                struct["nom_local"] = local_info.get("nom")
                struct["telephone"] = local_info.get("telephone")
                struct["email"] = local_info.get("email")
                struct["adresse"] = local_info.get("adresse")
                
            results.append(struct)

        return results

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
