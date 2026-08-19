import unicodedata

def remove_accents(s: str) -> str:
    if not s:
        return ""
    return "".join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

# Table de normalisation officielle des communes du territoire
COMMUNE_MAP = {
    # Sanary
    "sanary": "Sanary-sur-Mer",
    "sanary sur mer": "Sanary-sur-Mer",
    "sanary-sur-mer": "Sanary-sur-Mer",
    "sanary/mer": "Sanary-sur-Mer",
    
    # Toulon
    "toulon": "Toulon",
    "toulon centre": "Toulon",
    "toulon est": "Toulon",
    "toulon ouest": "Toulon",

    # La Seyne
    "la seyne": "La Seyne-sur-Mer",
    "la seyne sur mer": "La Seyne-sur-Mer",
    "la seyne-sur-mer": "La Seyne-sur-Mer",
    "laseyne": "La Seyne-sur-Mer",
    "laseyne sur mer": "La Seyne-sur-Mer",

    # Six Fours
    "six fours": "Six-Fours-les-Plages",
    "six fours les plages": "Six-Fours-les-Plages",
    "six-fours-les-plages": "Six-Fours-les-Plages",
    "six fours/plages": "Six-Fours-les-Plages",

    # Hyères
    "hyeres": "Hyères",
    "hyeres les palmiers": "Hyères",
    "hyeres-les-palmiers": "Hyères",
    
    # La Valette
    "la valette": "La Valette-du-Var",
    "la valette du var": "La Valette-du-Var",
    "la valette-du-var": "La Valette-du-Var",

    # La Garde
    "la garde": "La Garde",

    # Le Pradet
    "le pradet": "Le Pradet",

    # Ollioules
    "ollioules": "Ollioules",

    # Bandol
    "bandol": "Bandol",

    # Saint Cyr
    "saint cyr": "Saint-Cyr-sur-Mer",
    "st cyr": "Saint-Cyr-sur-Mer",
    "saint cyr sur mer": "Saint-Cyr-sur-Mer",
    "saint-cyr-sur-mer": "Saint-Cyr-sur-Mer",

    # Le Beausset
    "le beausset": "Le Beausset",

    # Le Castellet
    "le castellet": "Le Castellet",

    # La Cadière
    "la cadiere": "La Cadière-d'Azur",
    "la cadiere d azur": "La Cadière-d'Azur",
    "la cadiere d'azur": "La Cadière-d'Azur",

    # Saint Mandrier
    "saint mandrier": "Saint-Mandrier-sur-Mer",
    "st mandrier": "Saint-Mandrier-sur-Mer",
    "saint-mandrier-sur-mer": "Saint-Mandrier-sur-Mer",

    # Brignoles & Provence Verte
    "brignoles": "Brignoles",
    "bras": "Bras",
    "cotignac": "Cotignac",

    # Bormes & Hadage
    "bormes": "Bormes-les-Mimosas",
    "bormes les mimosas": "Bormes-les-Mimosas",
    "carqueiranne": "Carqueiranne",
    "la londe": "La Londe-les-Maures",
    "la londe les maures": "La Londe-les-Maures",
    "pierrefeu": "Pierrefeu-du-Var",
    "pierrefeu du var": "Pierrefeu-du-Var",
}

def normalize_commune(city: str) -> str:
    """Normalise le nom d'une commune pour l'agrégation statistique dans le Sankey."""
    if not city or not isinstance(city, str):
        return "Inconnue"

    raw = city.strip()
    if not raw or raw.lower() in ["inconnue", "inconnu", "none", "null", ""]:
        return "Inconnue"

    # Nettoyage de base (minuscules, retrait accents et caractères spéciaux)
    clean = remove_accents(raw).lower()
    clean = clean.replace("-", " ").replace("_", " ").replace("/", " ")
    clean = " ".join(clean.split())

    # 1. Recherche directe dans la table des synonymes
    if clean in COMMUNE_MAP:
        return COMMUNE_MAP[clean]

    # 2. Recherche par mot-clé principal
    if "sanary" in clean:
        return "Sanary-sur-Mer"
    if "toulon" in clean:
        return "Toulon"
    if "seyne" in clean:
        return "La Seyne-sur-Mer"
    if "six" in clean and "four" in clean:
        return "Six-Fours-les-Plages"
    if "hyere" in clean:
        return "Hyères"
    if "valette" in clean:
        return "La Valette-du-Var"
    if "garde" in clean:
        return "La Garde"
    if "pradet" in clean:
        return "Le Pradet"
    if "ollioule" in clean:
        return "Ollioules"
    if "bandol" in clean:
        return "Bandol"
    if "beausset" in clean:
        return "Le Beausset"
    if "castellet" in clean:
        return "Le Castellet"
    if "cadiere" in clean:
        return "La Cadière-d'Azur"
    if "mandrier" in clean:
        return "Saint-Mandrier-sur-Mer"
    if "borme" in clean:
        return "Bormes-les-Mimosas"
    if "londe" in clean:
        return "La Londe-les-Maures"
    if "pierrefeu" in clean:
        return "Pierrefeu-du-Var"

    # Sinon retourner le nom nettoyé avec majuscules appropriées
    return raw.title()
