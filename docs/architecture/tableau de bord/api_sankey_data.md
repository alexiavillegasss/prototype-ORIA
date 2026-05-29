# 🔌 Manuel : API de Données Sankey (Backend)

---

## 1. Vue d'ensemble de l'API Analytique

Pour alimenter le tableau de bord sans surcharger le navigateur du professionnel avec des calculs lourds de base de données, ORIA utilise une **architecture orientée services (API)**.

Le serveur FastAPI expose un endpoint HTTP hautement optimisé chargé d'extraire, d'anonymiser, de filtrer et d'agréger les informations cliniques sous forme de graphe mathématique de flux.

```
Navigateur (HTML/JS)  ─── GET /api/dashboard/sankey?dim1=X&dim2=Y ───►  FastAPI (main.py)
                                                                            │
   Réponse JSON (Nodes & Links + KPIs)  ◄───────────────────────────────────┘
```

---

## 2. L'Endpoint d'Agrégation `/api/dashboard/sankey`

*   **Endpoint HTTP** : `GET /api/dashboard/sankey`
*   **Fichier source** : [main.py](file:///c:/Users/milac/Documents/Projet%20ORIA/prototype-ORIA/backend/src/main.py)
*   **Paramètres de requête** : `dim1` (Niveau 1), `dim2` (Niveau 2), `dim3` (Niveau 3)

Lorsqu'il reçoit une requête, l'endpoint interroge la base de données via `db_manager.get_all_dossiers()` puis orchestre le calcul des KPIs et la structuration du diagramme.

---

## 3. Extraction et Traduction des Dimensions (`_get_dimension_value`)

Chaque dossier patient contient un dictionnaire imbriqué (Schéma Pivot). Les dimensions brutes ne sont pas toujours lisibles ou harmonisées (booléens `true/false`, nombres bruts). La fonction interne `_get_dimension_value` a pour rôle de traduire ces données brutes en étiquettes (labels) textuelles standardisées :

*   **Commune (`commune`)** : Extrait la chaîne textuelle `usager.localisation.commune_residence` (ou renvoie `"Inconnue"` par défaut).
*   **Tranche d'âge (`tranche_age`)** : Récupère `usager.identite.age_estime`, valide sa valeur numérique et le classe dans l'une des 6 tranches standardisées (ex: `60-64 ans`, `85 ans et plus`...).
*   **Complexité COMID (`complexite`)** : Extrait le libellé de complexité calculé par le docteur mathématicien (`niveau_comid`).
*   **Indicateurs d'aide (`apa` / `medecin_traitant` / `urgence`)** : Traduit les champs booléens du schéma pivot en phrases explicites lisibles (ex: `true` pour l'APA donne `"APA : Oui"`, `null` donne `"APA : Non renseigné"`).
*   **GIR (`gir`)** : Extrait la valeur et la formate sous l'intitulé officiel (ex: `"GIR 2"`).

---

## 4. Algorithme de Construction Dynamique du Graphe

Une fois les dimensions traduites pour chaque dossier patient, l'API construit dynamiquement les liaisons entre les colonnes :

### Étape 1 : Initialisation des compteurs d'arêtes (liens)
L'API calcule le nombre de liaisons entre les niveaux adjacents en utilisant des compteurs de fréquence (`Counter` du module Python `collections`) :
```python
links_counts = []
for i in range(len(valid_dims) - 1):
    links_counts.append(Counter())
```

### Étape 2 : Remplissage des liaisons
Pour chaque dossier de la BDD, le moteur récupère la valeur correspondante pour chaque niveau de dimension choisi. Il crée ensuite des couples de liaison `(Source, Cible)` entre chaque niveau consécutif (Niveau 1 → Niveau 2, puis Niveau 2 → Niveau 3) et incrémente leur fréquence :
```python
for i in range(len(valid_dims) - 1):
    vals_src = dim_values[i]
    vals_tgt = dim_values[i+1]
    for src in vals_src:
        for tgt in vals_tgt:
            links_counts[i][(src, tgt)] += 1
```

### Étape 3 : Génération des Nœuds uniques et des Liens JSON
Pour que la librairie ECharts frontend puisse dessiner le graphique, l'API reformate les compteurs Python en une structure JSON standardisée composée de deux tableaux :
1.  **`nodes`** : La liste de tous les nœuds uniques identifiés (les noms des communes, des tranches d'âges, des structures) triés par ordre alphabétique.
2.  **`links`** : La liste de toutes les connexions individuelles, contenant le nom du nœud de départ (`source`), le nom du nœud d'arrivée (`target`) et le volume de dossiers concernés (`value`).

---

## 5. Algorithme de Calcul des KPIs

En plus du graphe de flux, l'API calcule les métriques globales de synthèse en effectuant des analyses statistiques rapides sur les lignes SQLite extraites :

*   **Volume de dossiers** : Calculé par `len(dossiers)`.
*   **Moyenne COMID** : Extrait la colonne `score_comid` de chaque ligne de BDD et calcule la moyenne arithmétique globale.
*   **Valeurs dominantes** : Utilise le compteur de fréquences `collections.Counter` pour identifier instantanément la valeur ayant la plus haute occurrence dans la base :
    *   La commune la plus fréquente via `Counter(communes).most_common(1)`.
    *   Le niveau de complexité dominant via `Counter(niveaux).most_common(1)`.
    *   La structure la plus sollicitée via `Counter(all_structure_types).most_common(1)`.

Ces données sont combinées dans la réponse JSON finale pour alimenter instantanément le tableau de bord.
