# Manuel Gestion Sankey – Tableau de Bord ORIA

---

## 1. Vue d'ensemble

Le tableau de bord ORIA affiche un **diagramme de Sankey interactif** qui permet de visualiser les flux d'orientation des personnes âgées.  
Il se lit de gauche à droite en **3 niveaux** :

```
Commune du patient  →  Niveau de complexité (COMID)  →  Type de structure orientée
```

Le diagramme s'enrichit automatiquement à chaque nouveau dossier analysé et enregistré en base de données.

---

## 2. Fichiers concernés

Le code du Sankey est réparti dans **4 fichiers** :

| Fichier | Rôle |
|---------|------|
| `backend/src/main.py` | Contient l'**endpoint API** `/api/dashboard/sankey` qui lit la BDD et construit les données (nœuds + liens), ainsi que la route `/dashboard` qui sert la page HTML. |
| `backend/src/static/index.html` | Page HTML du tableau de bord : structure de la page, cartes KPI, conteneur du graphique, et chargement des dépendances (ECharts, CSS, JS). |
| `backend/src/static/style.css` | Feuille de style CSS : design dark mode, effets glassmorphism, animations d'apparition, responsive. |
| `backend/src/static/app.js` | Logique JavaScript : appel à l'API, mise à jour des KPIs, configuration et rendu du diagramme Sankey avec ECharts. |

---

## 3. Comment ça fonctionne

### Étape 1 – L'utilisateur ouvre le tableau de bord

L'utilisateur accède à `http://localhost:8000/dashboard` dans son navigateur.  
FastAPI sert le fichier `index.html` via la route `/dashboard`.

### Étape 2 – Le JavaScript appelle l'API

Au chargement de la page, le fichier `app.js` envoie une requête vers :

```
GET /api/dashboard/sankey
```

### Étape 3 – L'API construit les données

L'endpoint `/api/dashboard/sankey` (dans `main.py`) effectue les opérations suivantes :

1. **Récupération** : il appelle `db_manager.get_all_dossiers()` pour lire tous les dossiers de la table `dossiers_patients` dans la base SQLite.
2. **Calcul des KPIs** :
   - Nombre total de dossiers.
   - Score COMID moyen.
   - Commune la plus fréquente.
   - Structure la plus sollicitée.
   - Niveau de complexité dominant.
3. **Construction du Sankey** : pour chaque dossier, il crée deux types de liens :
   - **Commune → Niveau COMID** : un lien par dossier.
   - **Niveau COMID → Type de structure** : un lien par structure orientée (sans doublon par dossier).
4. **Réponse JSON** : il renvoie un objet contenant les KPIs et les données Sankey (liste de nœuds + liste de liens avec leurs valeurs).

Exemple simplifié de réponse :
```json
{
  "kpis": {
    "total_dossiers": 5,
    "score_moyen": 5.0,
    "commune_top": "Toulon",
    "structure_top": "CLIC",
    "niveau_top": "Situation à risque de complexité"
  },
  "sankey": {
    "nodes": [
      {"name": "Toulon"},
      {"name": "Situation non complexe"},
      {"name": "CLIC"}
    ],
    "links": [
      {"source": "Toulon", "target": "Situation non complexe", "value": 2},
      {"source": "Situation non complexe", "target": "CLIC", "value": 2}
    ]
  }
}
```

### Étape 4 – Le JavaScript affiche le résultat

`app.js` reçoit le JSON et :

1. Met à jour les **4 cartes KPI** en haut de page.
2. Passe les données Sankey à la librairie **ECharts** qui dessine le diagramme interactif.

---

## 4. Schéma du flux de données

```
┌──────────────────────┐
│  Navigateur (HTML)   │
│  http://localhost:    │
│  8000/dashboard      │
└──────────┬───────────┘
           │ GET /api/dashboard/sankey
           ▼
┌──────────────────────┐
│  FastAPI (main.py)   │
│  Endpoint Sankey     │
└──────────┬───────────┘
           │ get_all_dossiers()
           ▼
┌──────────────────────┐
│  SQLite              │
│  oria_database.db    │
│  table:              │
│  dossiers_patients   │
└──────────────────────┘
```

---

## 5. Technologies utilisées

| Technologie | Utilisation |
|-------------|-------------|
| **FastAPI** | Serveur web Python qui expose l'API et sert les fichiers statiques. |
| **SQLite** | Base de données locale contenant les dossiers patients anonymisés. |
| **ECharts** (v5) | Librairie JavaScript de visualisation de données. Chargée via CDN. |
| **HTML / CSS / JS** | Interface du tableau de bord, sans framework frontend (Vanilla). |

---

## 6. Lancer le tableau de bord

1. S'assurer que le serveur FastAPI est démarré :
```bash
cd backend/src
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

2. Ouvrir dans le navigateur :
```
http://localhost:8000/dashboard
```

3. Si la base est vide, un message indique d'utiliser `tester_interactivement.py` pour ajouter des dossiers.

---

## 7. Alimenter le diagramme

Chaque dossier analysé et enregistré dans la base de données enrichit automatiquement le Sankey.  
Il y a deux façons d'ajouter des dossiers :

- **Terminal interactif** : lancer `python tester_interactivement.py` à la racine et saisir un cas.
- **API** : envoyer une requête POST vers `/analyze` avec un texte de situation.

Après l'ajout, il suffit de **rafraîchir la page** du tableau de bord pour voir le Sankey mis à jour.

---

## 8. Personnalisation

### Modifier les couleurs du Sankey
Les couleurs sont définies dans `app.js`, dans l'objet `NODE_COLORS` :
```javascript
const NODE_COLORS = {
    'commune': ['#38bdf8', '#22d3ee', ...],  // Couleurs des communes
    'Situation simple': '#4ade80',             // Vert pour les cas simples
    'CRT': '#a78bfa',                          // Violet pour le CRT
    ...
};
```

### Modifier le design de la page
Le fichier `style.css` contient toutes les variables CSS en haut du fichier (section `:root`).  
Modifier ces variables change l'apparence globale :
```css
:root {
    --bg-primary: #0b0f19;       /* Fond principal */
    --accent-blue: #38bdf8;      /* Couleur d'accent */
    --radius: 16px;              /* Arrondi des cartes */
    ...
}
```

### Ajouter un 4ème niveau au Sankey
Pour ajouter un niveau supplémentaire (ex : tranche d'âge, GIR, présence APA), il faut :

1. Dans `main.py`, ajouter un 3ème compteur de liens (ex : `link_structure_gir`).
2. Alimenter ce compteur dans la boucle `for d in dossiers`.
3. Ajouter les nouveaux nœuds et liens dans la réponse JSON.

Le JavaScript (`app.js`) n'a pas besoin de modifications : ECharts gère automatiquement les niveaux supplémentaires.

---

## 9. Résumé des routes

| Route                    | Méthode |                              Description                               |
|--------------------------|---------|------------------------------------------------------------------------|
|       `/dashboard`       |   GET   |                   Sert la page HTML du tableau de bord.                |
|  `/api/dashboard/sankey` |   GET   |        Retourne le JSON contenant les KPIs et les données Sankey.      |
|         `/analyze`       |   POST  | Analyse un texte et enregistre le dossier en BDD (alimente le Sankey). |

---

