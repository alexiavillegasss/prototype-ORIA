import unicodedata

def remove_accents(s: str) -> str:
    if not s:
        return ""
    return "".join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

# Table de normalisation officielle de l'ensemble des communes du Var (Var Ouest, Métropole, Provence Verte, Hadage)
COMMUNE_MAP = {
    # --- MÉTROPOLE & VAR OUEST ---
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
    "toulon canton 1": "Toulon",
    "toulon canton 2": "Toulon",
    "toulon canton 3": "Toulon",

    # La Seyne (avec rattrapage des erreurs de dictée vocale)
    "la seyne": "La Seyne-sur-Mer",
    "la seyne sur mer": "La Seyne-sur-Mer",
    "la seyne-sur-mer": "La Seyne-sur-Mer",
    "laseyne": "La Seyne-sur-Mer",
    "la saine en l'air": "La Seyne-sur-Mer",
    "la saine en lair": "La Seyne-sur-Mer",
    "la saine en l air": "La Seyne-sur-Mer",
    "la saine sur mer": "La Seyne-sur-Mer",
    "la saine": "La Seyne-sur-Mer",
    "la scene sur mer": "La Seyne-sur-Mer",
    "la scene": "La Seyne-sur-Mer",
    "la seine sur mer": "La Seyne-sur-Mer",
    "la seine": "La Seyne-sur-Mer",
    "la scene-sur-mer": "La Seyne-sur-Mer",

    # Six Fours
    "six fours": "Six-Fours-les-Plages",
    "six fours les plages": "Six-Fours-les-Plages",
    "six-fours-les-plages": "Six-Fours-les-Plages",
    "6 fours": "Six-Fours-les-Plages",
    "6 fours les plages": "Six-Fours-les-Plages",
    "si fours": "Six-Fours-les-Plages",

    # Hyères
    "hyeres": "Hyères",
    "hyeres les palmiers": "Hyères",
    "hyeres-les-palmiers": "Hyères",
    
    # La Valette
    "la valette": "La Valette-du-Var",
    "la valette du var": "La Valette-du-Var",
    "la valette-du-var": "La Valette-du-Var",

    # La Garde & Le Pradet
    "la garde": "La Garde",
    "le pradet": "Le Pradet",

    # Ollioules & Bandol
    "ollioules": "Ollioules",
    "olioules": "Ollioules",
    "olioule": "Ollioules",
    "bandol": "Bandol",

    # Saint-Cyr & Saint-Mandrier
    "saint cyr": "Saint-Cyr-sur-Mer",
    "st cyr": "Saint-Cyr-sur-Mer",
    "saint-cyr-sur-mer": "Saint-Cyr-sur-Mer",
    "saint mandrier": "Saint-Mandrier-sur-Mer",
    "st mandrier": "Saint-Mandrier-sur-Mer",
    "saint-mandrier-sur-mer": "Saint-Mandrier-sur-Mer",

    # Sud Sainte Baume / Var Ouest (Evenos, Riboux, Signes, Beausset, Castellet, Cadière)
    "evenos": "Évenos",
    "riboux": "Riboux",
    "signes": "Signes",
    "le beausset": "Le Beausset",
    "le castellet": "Le Castellet",
    "la cadiere": "La Cadière-d'Azur",
    "la cadiere d azur": "La Cadière-d'Azur",
    "la cadiere d'azur": "La Cadière-d'Azur",

    # Vallon du Gapeau & Revest
    "la farlede": "La Farlède",
    "le revest": "Le Revest-les-Eaux",
    "le revest les eaux": "Le Revest-les-Eaux",
    "sollies pont": "Solliès-Pont",
    "sollies toucas": "Solliès-Toucas",
    "sollies ville": "Solliès-Ville",
    "cuers": "Cuers",

    # Sectorisation HADAGE (Secteur Hyères & Littoral Est)
    "bormes": "Bormes-les-Mimosas",
    "bormes les mimosas": "Bormes-les-Mimosas",
    "carqueiranne": "Carqueiranne",
    "cavalaire": "Cavalaire-sur-Mer",
    "cavalaire sur mer": "Cavalaire-sur-Mer",
    "collobrieres": "Collobrières",
    "la londe": "La Londe-les-Maures",
    "la londe les maures": "La Londe-les-Maures",
    "le rayol": "Le Rayol-Canadel-sur-Mer",
    "rayol canadel": "Le Rayol-Canadel-sur-Mer",
    "pierrefeu": "Pierrefeu-du-Var",
    "pierrefeu du var": "Pierrefeu-du-Var",

    # Sectorisation PROVENCE VERTE
    "brignoles": "Brignoles",
    "bras": "Bras",
    "camps la source": "Camps-la-Source",
    "carces": "Carcès",
    "chateauvert": "Châteauvert",
    "cotignac": "Cotignac",
    "correns": "Correns",
    "entrecasteaux": "Entrecasteaux",
    "gareoult": "Garéoult",
    "forcalqueiret": "Forcalqueiret",
    "la celle": "La Celle",
    "la roquebrussane": "La Roquebrussane",
    "mazaugues": "Mazaugues",
    "meounes": "Méounes-lès-Montrieux",
    "montfort": "Montfort-sur-Argens",
    "nans les pins": "Nans-les-Pins",
    "neoules": "Néoules",
    "ollieres": "Ollières",
    "plan d aups": "Plan-d'Aups-Sainte-Baume",
    "pourcieux": "Pourcieux",
    "pourrieres": "Pourrières",
    "rocbaron": "Rocbaron",
    "rougiers": "Rougiers",
    "saint maximin": "Saint-Maximin-la-Sainte-Baume",
    "st maximin": "Saint-Maximin-la-Sainte-Baume",
    "sainte anastasie": "Sainte-Anastasie-sur-Issole",
    "tourves": "Tourves",
    "vins sur caramy": "Vins-sur-Caramy",
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

    # 2. Recherche par mot-clé principal pour Var Ouest & Métropole
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
    if "evenos" in clean:
        return "Évenos"
    if "riboux" in clean:
        return "Riboux"
    if "signe" in clean:
        return "Signes"
    if "farlede" in clean:
        return "La Farlède"
    if "revest" in clean:
        return "Le Revest-les-Eaux"
    if "borme" in clean:
        return "Bormes-les-Mimosas"
    if "londe" in clean:
        return "La Londe-les-Maures"
    if "pierrefeu" in clean:
        return "Pierrefeu-du-Var"
    if "maximin" in clean:
        return "Saint-Maximin-la-Sainte-Baume"
    if "brignole" in clean:
        return "Brignoles"

    # Sinon retourner le nom nettoyé avec majuscules appropriées
    return raw.title()
