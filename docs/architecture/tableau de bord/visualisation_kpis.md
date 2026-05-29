# 📈 Manuel : Cartes KPIs & Sélecteurs Dynamiques

---

## 1. Vue d'ensemble des Indicateurs Métier (KPIs)

En complément du diagramme de Sankey, le tableau de bord d'ORIA affiche en tête de page **4 cartes d'indicateurs clés de performance (KPIs)**. Elles offrent une synthèse statistique temps réel des flux médico-sociaux du département du Var.

Ces indicateurs s'actualisent automatiquement à chaque fois qu'un nouveau cas est validé dans le tableau principal ou via l'API, ou lorsque l'utilisateur modifie les filtres d'affichage.

```
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ Dossiers Totaux │ │ Score Moyenne   │ │ Commune Top     │ │ Structure Top   │
│       14        │ │   11.5 / 20     │ │     Toulon      │ │      DAC        │
└─────────────────┘ └─────────────────┘ └─────────────────┘ └─────────────────┘
```

---

## 2. Description Fonctionnelle des 4 Cartes KPIs

Chaque carte KPI possède une icône SVG dédiée, un chiffre clé principal et un libellé descriptif :

1.  **Total des dossiers** (Badge d'en-tête `total-dossiers`) :
    Affiche le nombre total de situations patients uniques enregistrées dans la base de données locale. Cet indicateur donne le volume global de l'activité du service d'orientation.
2.  **Score COMID moyen** (`kpi-score-value`) :
    Calcule la moyenne arithmétique de la complexité clinique des cas. Un score moyen élevé indique que le service traite des situations globalement plus lourdes et dépendantes.
3.  **Commune la plus fréquente** (`kpi-commune-value`) :
    Identifie le secteur géographique le plus actif (la ville ayant généré le plus de requêtes). Utile pour planifier les ressources territoriales.
4.  **Structure la plus sollicitée** (`kpi-structure-value`) :
    Indique quelle structure d'accueil médico-sociale (ex: DAC, CRT, CLIC...) reçoit le plus de recommandations d'éligibilité.
5.  **Niveau de complexité dominant** (`kpi-complexity-value`) :
    Indique quelle tranche de complexité COMID revient le plus fréquemment (ex: *"Situation à risque de complexité"*).

---

## 3. Mécanisme de Mise à Jour du DOM (`updateKPIs`)

*   **Composant majeur** : `updateKPIs` (Fonction JavaScript)
*   **Fichier source** : [app.js](file:///c:/Users/milac/Documents/Projet%20ORIA/prototype-ORIA/backend/src/static/app.js)

Lors du chargement de la page ou d'une modification de dimension, le script récupère l'objet `kpis` inclus dans la réponse JSON de l'API. La fonction `updateKPIs` cible ensuite les éléments HTML via leurs identifiants uniques et met à jour leur contenu textuel :

```javascript
function updateKPIs(kpis) {
    document.getElementById('total-dossiers').textContent = kpis.total_dossiers;
    document.getElementById('kpi-score-value').textContent = kpis.score_moyen !== null
        ? kpis.score_moyen.toFixed(1)
        : '–';
    document.getElementById('kpi-commune-value').textContent = kpis.commune_top || '–';
    document.getElementById('kpi-structure-value').textContent = kpis.structure_top || '–';
    document.getElementById('kpi-complexity-value').textContent = kpis.niveau_top || '–';
}
```

Si la base de données ne contient aucun enregistrement, les indicateurs affichent des tirets cadratins `–` pour éviter d'induire le professionnel en erreur.

---

## 4. Les Sélecteurs de Dimensions Dynamiques

Pour permettre une exploration multidimensionnelle intuitive, le tableau de bord dispose de trois listes déroulantes de sélection correspondant aux colonnes verticales du diagramme :

*   **Niveau 1** (`select-dim1`) - *Par défaut : Commune*
*   **Niveau 2** (`select-dim2`) - *Par défaut : Complexité COMID*
*   **Niveau 3** (`select-dim3`) - *Par défaut : Type de structure*

### Liste des dimensions explorables :
L'utilisateur peut affecter n'importe laquelle de ces dimensions sur l'une des trois colonnes :
*   `commune` : Ville de résidence.
*   `tranche_age` : Regroupements par âges (ex: 60-64 ans, 85 ans et plus).
*   `apa` : Bénéficiaire effectif de l'APA (Oui / Non).
*   `gir` : Niveau de dépendance GIR (GIR 1 à 6).
*   `medecin_traitant` : Présence déclarée d'un médecin traitant.
*   `urgence` : Caractère urgent de la situation.
*   `complexite` : Classification COMID globale.
*   `structure` : Type de structure d'orientation recommandée.

---

## 5. Contrôle de Validité & Gestion des Doublons

*   **Composant majeur** : `loadDashboard` (Fonction JavaScript)

Les diagrammes de Sankey ne tolèrent pas de **cycles** logiques (par exemple, relier `Commune → Commune` ou créer une boucle infinie). Si un utilisateur sélectionne accidentellement la même dimension sur deux niveaux différents :

1.  La fonction `loadDashboard` extrait les dimensions et filtre les valeurs non-vides (`none`).
2.  Elle compare la longueur de cette liste avec un ensemble de valeurs uniques (`Set`).
3.  Si des doublons sont détectés, l'application bloque la requête API et affiche un message d'avertissement visuel élégant à l'écran : **"Veuillez ne pas sélectionner deux dimensions identiques."**, masquant le graphique vide.

Cela préserve le moteur de rendu ECharts d'un blocage de script et améliore l'expérience utilisateur globale.
