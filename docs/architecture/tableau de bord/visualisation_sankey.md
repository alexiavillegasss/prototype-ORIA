# 📊 Manuel : Diagramme de Sankey – Visualisation des Flux

---

## 1. Vue d'ensemble de la Visualisation Sankey

Le tableau de bord ORIA intègre un **diagramme de Sankey interactif**. Cet outil visuel haut de gamme est conçu pour cartographier et analyser en un coup d'œil les parcours et flux d'orientation des usagers âgés à travers les différentes structures du territoire.

Le diagramme se lit de gauche à droite, reliant dynamiquement les caractéristiques administratives ou cliniques des usagers aux préconisations d'aiguillage finales.

```
[Caractéristique Niveau 1]  ───►  [Caractéristique Niveau 2]  ───►  [Structure Orientée]
```

---

## 2. Le Rendu Interactif avec Apache ECharts

*   **Librairie externe** : `Apache ECharts` (chargée via CDN dans `index.html`)
*   **Composant majeur** : `renderSankey` (Fonction JavaScript)
*   **Fichier source** : [app.js](file:///c:/Users/milac/Documents/Projet%20ORIA/prototype-ORIA/backend/src/static/app.js)

Le rendu visuel repose sur le moteur de rendu vectoriel d'**ECharts**, configuré de façon sur-mesure pour s'intégrer dans la charte esthétique premium d'ORIA (effets de fondu, gradients de liens, typographies modernes).

### Configuration ECharts clé :
*   `emphasis.focus: 'adjacency'` : Lorsqu'un utilisateur passe sa souris sur un nœud ou un lien, ECharts estompe le reste du graphique et met en valeur le chemin d'écoulement exact (les nœuds parents et enfants connectés).
*   `lineStyle.color: 'gradient'` : Les liens reliant deux nœuds adoptent un dégradé de couleur harmonieux qui fusionne la couleur de départ et la couleur d'arrivée pour un effet haut de gamme.
*   `draggable: true` : Les utilisateurs peuvent cliquer et déplacer verticalement ou horizontalement les blocs de nœuds pour réordonner et clarifier les chevauchements visuels.
*   `saveAsImage` : Une boîte à outils (Toolbox) discrète en haut à droite permet d'exporter et de télécharger instantanément le diagramme généré sous forme d'image PNG haute résolution.

---

## 3. Cartographie des Couleurs (`NODE_COLORS`)

Pour conserver une cohérence visuelle parfaite entre les interfaces, les couleurs des nœuds ne sont pas aléatoires. Elles sont régies par un référentiel de palettes de couleurs dans le fichier `app.js` sous la constante `NODE_COLORS`.

Cette charte attribue des teintes sémantiques précises en fonction de la nature des nœuds :
*   **Niveaux de complexité** : Dégradé du vert au rouge vif (`#4ade80` pour Situation simple, `#fb923c` pour Situation à risque, `#f87171` pour Situation très complexe).
*   **Communes** : Palette de tons bleus et turquoise rafraîchissants pour distinguer les zones du Var (`#38bdf8`, `#22d3ee`, `#2dd4bf`...).
*   **Structures** : Teintes distinctives stables (ex: Violet `#a78bfa` pour le CRT, Orange `#fb923c` pour le DAC, Bleu `#38bdf8` pour le CLIC).
*   **Paramètres d'Aide (APA / Médecin / Urgence)** : Couleurs booléennes standardisées (Vert pour la présence d'aide ou l'absence d'urgence, Rouge pour l'urgence ou l'absence d'aide).

---

## 4. Intégration du Style Dark Mode & Glassmorphism

*   **Fichier source** : [style.css](file:///c:/Users/milac/Documents/Projet%20ORIA/prototype-ORIA/backend/src/static/style.css)

L'interface du tableau de bord utilise les jetons de design (design tokens) définis dans `:root` de `style.css` pour créer un habillage sobre et professionnel :
*   `--bg-primary` : Un fond bleu nuit très sombre (`#0b0f19`).
*   `--bg-glass` : Des panneaux semi-transparents avec flou d'arrière-plan (`backdrop-filter: blur(12px)`) et de fines bordures lumineuses (`border: 1px solid rgba(255, 255, 255, 0.08)`).
*   `--shadow-glow` : Des ombres portées avec halos colorés bleutés pour donner un relief moderne aux modules.

---

## 5. Personnalisation & Évolution (Ajouter un Niveau)

Le diagramme de Sankey est conçu pour être extensible. Si vous souhaitez étendre la visualisation à **4 niveaux** au lieu de 3 (ex: Commune → Tranche d'âge → Complexité → Structure) :

1.  **Dans `main.py`** : Ajouter un sélecteur dynamique ou une quatrième dimension dans l'API, et calculer un troisième groupe de liens de parcours dans l'endpoint `/api/dashboard/sankey` (par exemple : `Liens Niveau 3 → Niveau 4`).
2.  **Dans `index.html`** : Ajouter un quatrième menu déroulant de sélection HTML avec un identifiant unique (ex: `select-dim4`).
3.  **Dans `app.js`** : Ajouter l'écouteur d'événement sur ce nouveau sélecteur. ECharts calculera automatiquement les largeurs de colonnes et réorganisera l'affichage pour intégrer la nouvelle colonne intermédiaire sans nécessiter de refonte visuelle.
