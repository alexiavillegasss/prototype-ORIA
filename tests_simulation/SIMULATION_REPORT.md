# 📋 Rapport d'Évaluation Clinique ORIA

Généré automatiquement le : `2026-07-03 09:32:01`  
Nombre de cas exécutés : **21**  
Taux de succès : **21/21**  
Temps d'exécution total : **339.79 secondes**  

## 📊 Tableau récapitulatif des Orientations

| Patient | Status | Score COMID | Orientation Principale | Temps d'exécution |
| :--- | :---: | :---: | :--- | :---: |
| **Mme Durand** | ✅ SUCCESS | 4 | `CRT - Centre de Ressources Territorial (Accompagnement Renforc)` | 23.12s |
| **Mme Huguette** | ✅ SUCCESS | 5 | `UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion)` | 19.46s |
| **Mr Vacek** | ✅ SUCCESS | 5 | `CEV - Cellule coute et Vigilance (Violences & Spoliation)` | 15.19s |
| **Mr Lambert** | ✅ SUCCESS | 5 | `CRT - Centre de Ressources Territorial (Accompagnement Renforc)` | 14.13s |
| **Mme Petit** | ✅ SUCCESS | 2 | `UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion)` | 11.64s |
| **Mme Lefebvre** | ✅ SUCCESS | 5 | `DAC - Dispositif d'Appui  la Coordination` | 17.64s |
| **Mr Leroy** | ✅ SUCCESS | 5 | `UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion)` | 19.19s |
| **Mme Rossi** | ✅ SUCCESS | 4 | `UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion)` | 13.83s |
| **Mme Martin** | ✅ SUCCESS | 4 | `CLIC - Centre Local d'Information et de Coordination` | 15.12s |
| **Mr Martin** | ✅ SUCCESS | 4 | `CLIC - Centre Local d'Information et de Coordination` | 14.49s |
| **Mme Fontaine** | ✅ SUCCESS | 6 | `CEV - Cellule coute et Vigilance (Violences & Spoliation)` | 12.94s |
| **Mme Gautier** | ✅ SUCCESS | 11 | `CLIC - Centre Local d'Information et de Coordination` | 27.02s |
| **Mme Vial** | ✅ SUCCESS | 2 | `CPTS - Communaut Professionnelle Territoriale de Sant` | 15.11s |
| **Mme Michu** | ✅ SUCCESS | 3 | `CRT - Centre de Ressources Territorial (Accompagnement Renforc)` | 14.41s |
| **Mr Petit** | ✅ SUCCESS | 4 | `CLIC - Centre Local d'Information et de Coordination` | 13.98s |
| **Mr Chen** | ✅ SUCCESS | 2 | `UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion)` | 13.21s |
| **Mme Morel** | ✅ SUCCESS | 2 | `Service Social de l'Hpital` | 15.80s |
| **Mr Pierre** | ✅ SUCCESS | 5 | `CLIC - Centre Local d'Information et de Coordination` | 13.43s |
| **Mme Bernard** | ✅ SUCCESS | 5 | `CLIC - Centre Local d'Information et de Coordination` | 14.42s |
| **Mr Dubois** | ✅ SUCCESS | 8 | `CLIC - Centre Local d'Information et de Coordination` | 16.65s |
| **Mme Mouton** | ✅ SUCCESS | 4 | `UTS Littoral Sud Sainte Baume - OLLIOULES (Relais CLIC)` | 19.02s |

---

## 📝 Détail des extractions et raisonnements

<details>
<summary>🔍 Cas Mme Durand (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Durand ---

1. Extraction IA pour : 'Mme Durand, 88 ans, vit  Hyres. Elle est trs co...'

--- DEBUG : ANALYSE EXPERTE ---
Mme D., 88 ans, vit  Hyres. Elle est trs confuse, elle dambule la nuit dans l'immeuble. Elle est agressive avec les infirmiers qui viennent pour son diabte et refuse qu'ils entrent. Ses voisins s'en plaignent et la situation devient dangereuse.
Ville extraite : Hyres
Mdecin : identifie
Malveillance : aucune
Hospitalisation : aucun
tat Logement : non_renseigne
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 88,
  "usager.localisation.commune_residence": "Hyres",
  "usager.situation_actuelle.APA": "oui",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "inconnu",
  "usager.cadre_de_vie.aidant_regulier": "inconnu",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
  "demande.proposition_mail": "Mme D., 88 ans, vit  Hyres. Elle est trs confuse et dambule la nuit dans l'immeuble. Elle est agressive avec les infirmiers qui viennent pour son diabte et refuse qu'ils entrent. Ses voisins s'en plaignent et la situation devient dangereuse.",
  "demande.resume_structur": "Mme D., 88 ans, vit  Hyres. Elle est trs confuse, elle dambule la nuit dans l'immeuble. Elle est agressive avec les infirmiers qui viennent pour son diabte et refuse qu'ils entrent. Ses voisins s'en plaignent et la situation devient dangereuse.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 100,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 0,
    "aidant_regulier": 0,
    "medecin_traitant": 80,
    "malveillance": 90,
    "urgence": 95,
    "hospitalisation": 95,
    "motif": 100,
    "etat_logement": 0
  },
  "evaluation.comid.justifications": [
    {
      "code": "troubles_cognitifs",
      "justification": "elle est trs confuse",
      "confiance": 95
    },
    {
      "code": "perte_autonomie_recente",
      "justification": "elle dambule la nuit dans l'immeuble",
      "confiance": 95
    },
    {
      "code": "agressivite",
      "justification": "elle est agressive avec les infirmiers",
      "confiance": 100
    }
  ],
  "evaluation.confiance.comid": {
    "troubles_cognitifs": 95,
    "perte_autonomie_recente": 95,
    "agressivite": 100,
    "opposition_soins": 0
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": true,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": false,
  "evaluation.comid.logement_inadapte": false,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": false,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": true,
  "evaluation.comid.opposition_soins": true,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": true,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": null
}

2. Calcul du score de complexit COMID...
Score Total : 4 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Hyres)...

--- RESULTATS DE L'ORIENTATION ---

[ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ] - Priorite : 125
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 125 pts).
Contact : Non trouve dans le referentiel territorial

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 120
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 120 pts).
Contact : Non trouve dans le referentiel territorial

[ PSCG SS APA - Ple Social de Solidarit et de Gestion (APA) ] - Priorite : 80
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 80 pts).
Contact : Non trouve dans le referentiel territorial

[ DAC - Dispositif d'Appui  la Coordination ] - Priorite : 60
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 60 pts).
Contact : Non trouve dans le referentiel territorial

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Huguette (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Huguette (Urgence Sociale / Protection) ---

1. Extraction IA (Temp=0.0) pour : 'Mme Huguette, 79 ans, vit seule dans un logement insalubre et humide  La Valett...'

--- DEBUG : ANALYSE EXPERTE ---
Mme H., 79 ans, vit seule dans un logement insalubre et humide  La Valette du Var. Elle n'a pas l'APA et vit sous le seuil de pauvret avec une infime pension de retraite. Une amie trs proche s'inquite : elle signale que le neveu d'Huguette, qui a procuration sur ses comptes bancaires, effectue des retraits d'argent massifs et rpts sans justification, laissant Huguette sans le moindre sou pour s'acheter de quoi manger. Huguette est terrifie par son neveu et n'ose rien dire par peur de reprsailles.
Ville extraite : La Valette du Var
Mdecin : incertain
Malveillance : spoliation_financiere
Hospitalisation : aucun
tat Logement : insalubre
--- FIN DEBUG ---

Donnes extraites (JSON) :
{
  "usager.identite.age_estime": 79,
  "usager.localisation.commune_residence": "La Valette du Var",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "spoliation_financiere",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "logement",
  "vulnerabilites.sante.professionnels_domicile": "inconnu",
  "usager.cadre_de_vie.aidant_regulier": "inconnu",
  "usager.cadre_de_vie.etat_logement": "insalubre",
  "demande.proposition_mail": "Mme H., 79 ans, vit seule dans un logement insalubre et humide  La Valette du Var. Elle n'a pas l'APA et vit sous le seuil de pauvret avec une infime pension de retraite. Son neveu procdure sur ses comptes bancaires effectue des retraits d'argent massifs et rpts sans justification, laissant Huguette sans le moindre sou pour s'acheter de quoi manger.",
  "demande.resume_structur": "Mme H., 79 ans, vit seule dans un logement insalubre et humide  La Valette du Var. Elle n'a pas l'APA et vit sous le seuil de pauvret avec une infime pension de retraite. Une amie trs proche s'inquite : elle signale que le neveu d'Huguette, qui a procuration sur ses comptes bancaires, effectue des retraits d'argent massifs et rpts sans justification, laissant Huguette sans le moindre sou pour s'acheter de quoi manger. Huguette est terrifie par son neveu et n'ose rien dire par peur de reprsailles.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 0,
    "aidant_regulier": 0,
    "medecin_traitant": 0,
    "malveillance": 90,
    "urgence": 95,
    "hospitalisation": 95,
    "motif": 100,
    "etat_logement": 0
  },
  "evaluation.comid.justifications": [
    {
      "code": "precarite_financiere",
      "justification": "elle n'a pas l'APA et vit sous le seuil de pauvret avec une infime pension de retraite",
      "confiance": 95
    },
    {
      "code": "logement_inadapte",
      "justification": "le logement est insalubre et humide",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "elle vit seule",
      "confiance": 95
    },
    {
      "code": "anxiete",
      "justification": "elle est terrifie par son neveu et n'ose rien dire par peur de reprsailles",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "precarite_financiere": 95,
    "logement_inadapte": 100,
    "isolement_social": 95,
    "anxiete": 95,
    "lourdeur_reseau": 100
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": true,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": true,
  "evaluation.comid.logement_inadapte": true,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": true,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": true,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 5 (Situation non complexe)

3. valuation de l'orientation...

4. Recherche des contacts territoriaux (La Valette)...

--- RSULTATS DE L'ORIENTATION POUR MME HUGUETTE ---

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorit : 105 | Confiance : 97%
Justification confiance : critre COMID 'precarite_financiere' dtect  95%, variable 'motif' extraite  100%
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 105 pts).
Contact : 04 83 95 56 90 | 427 Avenue Duchatel 83130 La Valette du Var

[ CEV - Cellule coute et Vigilance (Violences & Spoliation) ] - Priorit : 85 | Confiance : 90%
Justification confiance : variable 'malveillance' extraite  90%
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 85 pts).
Contact : 04 83 95 16 01 | None

[ CCAS - Centre Communal d'Action Sociale ] - Priorit : 65 | Confiance : 97%
Justification confiance : critre COMID 'precarite_financiere' dtect  95%, variable 'motif' extraite  100%
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 65 pts).
Contact : 04 94 20 92 70 | place Gnral de Gaulle 83160 la Valette du Var

[ CLIC - Centre Local d'Information et de Coordination ] - Priorit : 25 | Confiance : 100%
Justification confiance : variable 'age' extraite  100%
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 25 pts).
Contact : 04 22 44 84 73 | None

[ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ] - Priorit : 25 | Confiance : 100%
Justification confiance : variable 'age' extraite  100%
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 25 pts).
Contact : Non trouv dans le rfrentiel territorial

[ DAC - Dispositif d'Appui  la Coordination ] - Priorit : 10 | Confiance : 100%
Justification confiance : variable 'age' extraite  100%
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 10 pts).
Contact : 04 94 35 32 01 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Vacek (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Vacek (Habitat Indigne & Danger) ---

1. Extraction IA pour la situation de pril...

--- DEBUG : ANALYSE EXPERTE ---
Patient de 65 ans  Toulon, vivant dans un appartement insalubre sans eau courante et menac par une infiltration. Il est terrifi et a des problmes respiratoires srieux.
Ville extraite : Toulon
Mdecin : incertain
Malveillance : violences_physiques
Hospitalisation : aucun
tat Logement : insalubre
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 65,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "violences_physiques",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "logement",
  "vulnerabilites.sante.professionnels_domicile": "inconnu",
  "usager.cadre_de_vie.aidant_regulier": "inconnu",
  "usager.cadre_de_vie.etat_logement": "insalubre",
  "demande.proposition_mail": "Monsieur, g de 65 ans et habitant  Toulon, vit dans un appartement insalubre sans eau courante et menac par une infiltration. Il est terrifi et a des problmes respiratoires srieux. Nous sollicitons votre intervention pour une valuation globale et un soutien  domicile.",
  "demande.resume_structur": "Patient de 65 ans  Toulon, vivant dans un appartement insalubre sans eau courante et menac par une infiltration. Il est terrifi et a des problmes respiratoires srieux.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 100,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 0,
    "aidant_regulier": 0,
    "medecin_traitant": 0,
    "malveillance": 100,
    "urgence": 100,
    "hospitalisation": 100,
    "motif": 100,
    "etat_logement": 100
  },
  "evaluation.comid.justifications": [
    {
      "code": "logement_inadapte",
      "justification": "son appartement est insalubre",
      "confiance": 100
    },
    {
      "code": "isolement_social",
      "justification": "il vit seul",
      "confiance": 95
    },
    {
      "code": "precarite_financiere",
      "justification": "son dossier de retraite est bloqu",
      "confiance": 95
    },
    {
      "code": "anxiete",
      "justification": "il est terrifi",
      "confiance": 100
    }
  ],
  "evaluation.confiance.comid": {
    "logement_inadapte": 100,
    "isolement_social": 95,
    "precarite_financiere": 95,
    "anxiete": 100,
    "lourdeur_reseau": 100
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": true,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": true,
  "evaluation.comid.logement_inadapte": true,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": true,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": true,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 5 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- REPONSE D'ORIA (URGENCE HABITAT) ---
ORIA : 'La situation de M. Vacek prsente un DANGER IMMINENT.'

VOTRE PRIORIT ABSOLUE : [ CEV - Cellule coute et Vigilance (Violences & Spoliation) ]
MISSION : Mise en scurit immdiate et protection d'urgence des majeurs vulnrables en situation de violence physique active ou menace.
CONTACT : 04 83 95 16 01

ENSUITE (VOLET SOCIAL) : [ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ]
MISSION : Orientation clinique recommande par l'valuation clinique multicritre (Score : 105 pts).

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Lambert (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Lambert (Appel Infirmire) ---

1. Extraction IA pour le rcit de l'infirmire...

--- DEBUG : ANALYSE EXPERTE ---
Patient de 78 ans  La Seyne, en refus de soins et isolement, avec urgence faible.
Ville extraite : La Seyne
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : diogene
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 78,
  "usager.localisation.commune_residence": "La Seyne",
  "usager.situation_actuelle.APA": "inconnu",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "inconnu",
  "usager.cadre_de_vie.aidant_regulier": "inconnu",
  "usager.cadre_de_vie.etat_logement": "diogene",
  "demande.proposition_mail": "Monsieur, g de 78 ans et habitant  La Seyne, refuse les soins prescrits et est isol. Nous sollicitons votre intervention pour une valuation globale et un soutien  domicile.",
  "demande.resume_structur": "Patient de 78 ans  La Seyne, en refus de soins et isolement, avec urgence faible.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 0,
    "aidant_regulier": 0,
    "medecin_traitant": 0,
    "malveillance": 100,
    "urgence": 100,
    "hospitalisation": 100,
    "motif": 100,
    "etat_logement": 100
  },
  "evaluation.comid.justifications": [
    {
      "code": "isolement_social",
      "justification": "veuf, sa famille est  Paris et ils ne dcrochent plus le tlphone",
      "confiance": 95
    },
    {
      "code": "logement_inadapte",
      "justification": "son appartement, qui tait impeccable, est devenu un dpotoir : il y a des sacs poubelles partout et a sent trs fort l'urine",
      "confiance": 95
    },
    {
      "code": "perte_autonomie_recente",
      "justification": "il refuse que j'entre faire ses pansements, il me crie dessus et me dit que je veux l'empoisonner avec ses mdicaments",
      "confiance": 95
    },
    {
      "code": "anxiete",
      "justification": "je suis perdue avec un de mes patients",
      "confiance": 70
    }
  ],
  "evaluation.confiance.comid": {
    "isolement_social": 95,
    "logement_inadapte": 100,
    "perte_autonomie_recente": 95,
    "anxiete": 70,
    "opposition_soins": 0
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": true,
  "evaluation.comid.logement_inadapte": true,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": true,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": true,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": true,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 5 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (La Seyne-sur-Mer)...

--- REPONSE D'ORIA POUR L'INFIRMIERE ---
ORIA : 'D'aprs votre description, la situation de M. Lambert est Situation non complexe. Voici les priorits d'appel :'

CONTACTER : [ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ]
POURQUOI : Orientation clinique recommande par l'valuation clinique multicritre (Score : 105 pts).
CONTACT : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chnes 83500 LA SEYNE SUR MER

CONTACTER : [ CLIC - Centre Local d'Information et de Coordination ]
POURQUOI : Orientation clinique recommande par l'valuation clinique multicritre (Score : 100 pts).
CONTACT : 04 94 06 97 04 | None

CONTACTER : [ DAC - Dispositif d'Appui  la Coordination ]
POURQUOI : Orientation clinique recommande par l'valuation clinique multicritre (Score : 55 pts).
CONTACT : 04 94 35 32 01 | None

CONTACTER : [ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ]
POURQUOI : Orientation clinique recommande par l'valuation clinique multicritre (Score : 30 pts).
CONTACT : 04 83 95 48 30 ou 04 83 95 37 99 | rue Charles Gide 83500 La Seyne sur mer

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Petit (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Petit (Urgence CCAS) ---

1. Extraction IA pour : 'Mme Petit, 78 ans, habite  La Garde. Elle vit seu...'

--- DEBUG : ANALYSE EXPERTE ---
Mme P., 78 ans, habitante  La Garde, demande de l'aide pour s'acheter  manger et faire ses courses en raison d'une petite retraite.
Ville extraite : La Garde
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : propre
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 78,
  "usager.localisation.commune_residence": "La Garde",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "aide_alimentaire",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "demande.proposition_mail": "Madame P., ge de 78 ans et rsidente  La Garde, a une petite retraite et est en difficult pour s'acheter  manger. Elle sollicite notre aide pour obtenir des courses et viter les impays.",
  "demande.resume_structur": "Mme P., 78 ans, habitante  La Garde, demande de l'aide pour s'acheter  manger et faire ses courses en raison d'une petite retraite.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 100,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 100,
    "aidant_regulier": 100,
    "medecin_traitant": 0,
    "malveillance": 100,
    "urgence": 100,
    "hospitalisation": 100,
    "motif": 100,
    "etat_logement": 100
  },
  "evaluation.comid.justifications": [
    {
      "code": "precarite_financiere",
      "justification": "son compte bancaire est  dcouvert",
      "confiance": 100
    },
    {
      "code": "isolement_social",
      "justification": "elle vit seule",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "precarite_financiere": 100,
    "isolement_social": 95
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": true,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": true,
  "evaluation.comid.logement_inadapte": false,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": false,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 2 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (La Garde)...

--- RESULTATS DE L'ORIENTATION (Territoire: La Garde) ---

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorite : 55
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 55 pts).
Contact : 04 83 95 56 50 | 53 Impasse Blriot Immeuble Le Frdric 83130 La Garde

[ CCAS - Centre Communal d'Action Sociale ] - Priorite : 35
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 35 pts).
Contact : 04 94 08 98 34 | 81 Rue Marius Tardivier 83130 La garde

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 25
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 25 pts).
Contact : 04 22 44 84 73 | None

[ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ] - Priorite : 25
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 25 pts).
Contact : 06 83 38 39 39 | 421 Av 1er Bataillon Infanterie de Marine du Pacifique 83130 La Garde

[ DAC - Dispositif d'Appui  la Coordination ] - Priorite : 10
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 10 pts).
Contact : 04 94 35 32 01 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Lefebvre (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Lefebvre ---

1. Extraction IA pour : 'Mme Lefebvre, 65 ans, vit  La Garde. Elle est sui...'

--- DEBUG : ANALYSE EXPERTE ---
Mme L., 65 ans, vit  La Garde. Elle est suivie pour une bipolarit depuis des annes mais elle a arrt son traitement le mois dernier. Elle consomme beaucoup d'alcool pour 'calmer ses angoisses' selon ses propres mots. Elle vit dans un appartement trs encombr (Syndrome de Diogne suspect) et ses voisins se plaignent d'odeurs fortes. Elle n'a plus de famille et refuse toute aide du service social, se montrant parfois trs agressive verbalement quand on frappe  sa porte.
Ville extraite : La Garde
Mdecin : identifie
Malveillance : aucune
Hospitalisation : aucun
tat Logement : diogene
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 65,
  "usager.localisation.commune_residence": "La Garde",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "inconnu",
  "usager.cadre_de_vie.aidant_regulier": "inconnu",
  "usager.cadre_de_vie.etat_logement": "diogene",
  "demande.proposition_mail": "Mme L., ge de 65 ans et habitant  La Garde, a arrt son traitement pour une bipolarit. Elle consomme beaucoup d'alcool pour calmer ses angoisses et refuse toute aide du service social. Son logement est trs encombr et les odeurs fortes sont signales par les voisins.",
  "demande.resume_structur": "Mme L., 65 ans, vit  La Garde. Elle est suivie pour une bipolarit depuis des annes mais elle a arrt son traitement le mois dernier. Elle consomme beaucoup d'alcool pour 'calmer ses angoisses' selon ses propres mots. Elle vit dans un appartement trs encombr (Syndrome de Diogne suspect) et ses voisins se plaignent d'odeurs fortes. Elle n'a plus de famille et refuse toute aide du service social, se montrant parfois trs agressive verbalement quand on frappe  sa porte.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 0,
    "aidant_regulier": 0,
    "medecin_traitant": 80,
    "malveillance": 90,
    "urgence": 95,
    "hospitalisation": 95,
    "motif": 100,
    "etat_logement": 0
  },
  "evaluation.comid.justifications": [
    {
      "code": "addiction",
      "justification": "consomme beaucoup d'alcool pour 'calmer ses angoisses'",
      "confiance": 100
    },
    {
      "code": "psychiatrie",
      "justification": "bipolarit depuis des annes",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "n'a plus de famille et refuse toute aide du service social",
      "confiance": 95
    },
    {
      "code": "logement_inadapte",
      "justification": "appartement trs encombr (Syndrome de Diogne suspect)",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "addiction": 100,
    "psychiatrie": 95,
    "isolement_social": 95,
    "logement_inadapte": 100,
    "opposition_soins": 0
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": true,
  "evaluation.comid.logement_inadapte": true,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": true,
  "evaluation.comid.addiction": true,
  "evaluation.comid.anxiete": false,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": true,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 5 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (La Garde)...

--- RESULTATS DE L'ORIENTATION ---

[ DAC - Dispositif d'Appui  la Coordination ] - Priorite : 70
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 70 pts).
Contact : 04 94 35 32 01 | None

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 55
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 55 pts).
Contact : 04 22 44 84 73 | None

[ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ] - Priorite : 55
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 55 pts).
Contact : 06 83 38 39 39 | 421 Av 1er Bataillon Infanterie de Marine du Pacifique 83130 La Garde

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorite : 50
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 50 pts).
Contact : 04 83 95 56 50 | 53 Impasse Blriot Immeuble Le Frdric 83130 La Garde

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Leroy (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Leroy (Moins de 60 ans) ---

1. Extraction IA pour : 'M. Leroy, 45 ans, habite  Toulon. Il est atteint ...'

--- DEBUG : ANALYSE EXPERTE ---
Patient de 45 ans  Toulon, atteint d'une Sclrose en Plaques (SEP) diagnostique il y a 2 ans. Sa sant se dgrade rapidement et il a d arrter son activit professionnelle. Il vit seul, ses revenus ont chut et il a du mal  payer son loyer. Il se sent perdu dans son parcours de soins entre les diffrents spcialistes et son moral est au plus bas, il exprime des ides noires.
Ville extraite : Toulon
Mdecin : identifie
Malveillance : aucune
Hospitalisation : aucun
tat Logement : incurie
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 45,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "incurie",
  "demande.proposition_mail": "Monsieur, g de 45 ans et habitant  Toulon, atteint d'une Sclrose en Plaques (SEP) diagnostique il y a 2 ans. Sa sant se dgrade rapidement et il a d arrter son activit professionnelle. Il vit seul, ses revenus ont chut et il a du mal  payer son loyer. Il se sent perdu dans son parcours de soins entre les diffrents spcialistes et son moral est au plus bas, il exprime des ides noires.",
  "demande.resume_structur": "Patient de 45 ans  Toulon, atteint d'une Sclrose en Plaques (SEP) diagnostique il y a 2 ans. Sa sant se dgrade rapidement et il a d arrter son activit professionnelle. Il vit seul, ses revenus ont chut et il a du mal  payer son loyer. Il se sent perdu dans son parcours de soins entre les diffrents spcialistes et son moral est au plus bas, il exprime des ides noires.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 100,
    "aidant_regulier": 100,
    "medecin_traitant": 80,
    "malveillance": 90,
    "urgence": 95,
    "hospitalisation": 95,
    "motif": 100,
    "etat_logement": 0
  },
  "evaluation.comid.justifications": [
    {
      "code": "precarite_financiere",
      "justification": "ses revenus ont chut et il a du mal  payer son loyer",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "il vit seul",
      "confiance": 95
    },
    {
      "code": "troubles_cognitifs",
      "justification": "il se sent perdu dans son parcours de soins",
      "confiance": 70
    },
    {
      "code": "depression",
      "justification": "il exprime des ides noires",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "precarite_financiere": 95,
    "isolement_social": 95,
    "troubles_cognitifs": 70,
    "depression": 95,
    "logement_inadapte": 100
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": true,
  "evaluation.comid.precarite_financiere": true,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": true,
  "evaluation.comid.logement_inadapte": true,
  "evaluation.comid.depression": true,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": false,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 5 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION (Age: 45 ans) ---

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorite : 85
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 85 pts).
Contact : 04 83 95 24 42 | 100, traverse des minimes 83000 Toulon

[ CCAS - Centre Communal d'Action Sociale ] - Priorite : 35
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 35 pts).
Contact : 04 94 24 65 00 | 100 rue des remparts - CS 20813 83051 Toulon Cedex

[ DAC - Dispositif d'Appui  la Coordination ] - Priorite : 25
Objectif : [/!\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] Orientation clinique recommande par l'valuation clinique multicritre (Score : 25 pts).
Contact : 04 94 35 32 01 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Rossi (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Rossi (Violences Conjugales) ---

1. Extraction IA pour : 'Mme Rossi, 70 ans, habite  Toulon. Elle vient d'a...'

--- DEBUG : ANALYSE EXPERTE ---
Mme R., 70 ans, habitante  Toulon, a d quitter son domicile en urgence suite  des violences physiques et verbales de la part de son mari. Elle est actuellement cache chez une amie et a besoin d'tre protge et de trouver un hbergement d'urgence.
Ville extraite : Toulon
Mdecin : incertain
Malveillance : violences_physiques
Hospitalisation : aucun
tat Logement : incurie
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 70,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "violences_physiques",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "logement",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "incurie",
  "demande.proposition_mail": "Mme R., ge de 70 ans et habitante  Toulon, a t victime de violences physiques et verbales de la part de son mari. Elle est actuellement cache chez une amie et sollicite notre aide pour trouver un hbergement d'urgence et tre protge.",
  "demande.resume_structur": "Mme R., 70 ans, habitante  Toulon, a d quitter son domicile en urgence suite  des violences physiques et verbales de la part de son mari. Elle est actuellement cache chez une amie et a besoin d'tre protge et de trouver un hbergement d'urgence.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 100,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 100,
    "aidant_regulier": 100,
    "medecin_traitant": 0,
    "malveillance": 100,
    "urgence": 100,
    "hospitalisation": 100,
    "motif": 100,
    "etat_logement": 100
  },
  "evaluation.comid.justifications": [
    {
      "code": "isolement_social",
      "justification": "elle est actuellement cache chez une amie",
      "confiance": 95
    },
    {
      "code": "logement_inadapte",
      "justification": "son mari est devenu trs violent physiquement et verbalement",
      "confiance": 70
    },
    {
      "code": "depression",
      "justification": "elle est actuellement trs angoisse pour sa sant",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "isolement_social": 95,
    "logement_inadapte": 100,
    "depression": 95,
    "lourdeur_reseau": 100
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": true,
  "evaluation.comid.logement_inadapte": true,
  "evaluation.comid.depression": true,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": false,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": true,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 4 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION (Protection / Violences) ---

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorite : 80
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 80 pts).
Contact : 04 83 95 24 42 | 100, traverse des minimes 83000 Toulon

[ Les Compagnons Btisseurs (Diogne ou Incurie unique/principale) ] - Priorite : 75
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 75 pts).
Contact : Non trouve dans le referentiel territorial

[ CCAS - Centre Communal d'Action Sociale ] - Priorite : 30
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 30 pts).
Contact : 04 94 24 65 00 | 100 rue des remparts - CS 20813 83051 Toulon Cedex

[ DAC - Dispositif d'Appui  la Coordination ] - Priorite : 15
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 15 pts).
Contact : 04 94 35 32 01 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Martin (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Martin (Dtresse Aidant) ---

1. Extraction IA pour le rcit de l'aidante...

--- DEBUG : ANALYSE EXPERTE ---
Fille de 82 ans  Toulon, en situation de carence et de stress li  la prise en charge de sa mre ge, qui ncessite une aide pour tre en scurit et permettre  la fille de se ressourcer.
Ville extraite : Toulon
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : propre
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 82,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "inconnu",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "oui",
  "usager.cadre_de_vie.etat_logement": "propre",
  "demande.proposition_mail": "Bonjour, nous sommes proccups par la situation de votre fille, ge de 82 ans et vivant  Toulon. Elle est puise aprs avoir pris soin de sa mre ge et craque sous le poids des responsabilits. Nous sollicitons votre intervention pour aider cette famille en difficult.",
  "demande.resume_structur": "Fille de 82 ans  Toulon, en situation de carence et de stress li  la prise en charge de sa mre ge, qui ncessite une aide pour tre en scurit et permettre  la fille de se ressourcer.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 100,
    "aidant_regulier": 100,
    "medecin_traitant": 0,
    "malveillance": 100,
    "urgence": 100,
    "hospitalisation": 100,
    "motif": 100,
    "etat_logement": 100
  },
  "evaluation.comid.justifications": [
    {
      "code": "epuisement_aidant",
      "justification": "Je n'en peux plus, je craque.",
      "confiance": 95
    },
    {
      "code": "perte_autonomie_recente",
      "justification": "elle laisse le gaz allum, elle se relve la nuit et elle est tombe deux fois.",
      "confiance": 100
    },
    {
      "code": "troubles_cognitifs",
      "justification": "elle laisse le gaz allum, elle se relve la nuit et elle est tombe deux fois.",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "Je travaille  temps plein et je passe toutes mes soires et mes week-ends chez elle.",
      "confiance": 70
    }
  ],
  "evaluation.confiance.comid": {
    "epuisement_aidant": 95,
    "perte_autonomie_recente": 100,
    "troubles_cognitifs": 95,
    "isolement_social": 70
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": true,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": true,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": true,
  "evaluation.comid.logement_inadapte": false,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": false,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": true,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 4 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- REPONSE D'ORIA POUR L'AIDANTE ---
ORIA : 'Je comprends votre puisement. La situation de votre mre est Situation non complexe.'

VOTRE PRIORIT ABSOLUE : [ CLIC - Centre Local d'Information et de Coordination ]
MISSION : Orientation clinique recommande par l'valuation clinique multicritre (Score : 125 pts).
CONTACT : 04 94 24 65 25

CONSEIL POUR VOUS : 'Pensez galement  contacter une plateforme de rpit pour aidants. Ces structures proposent du soutien psychologique pour vous permettre de souffler.'

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Martin (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Martin ---

1. Extraction IA pour : 'M. Martin, 75 ans, habite  La Seyne-sur-Mer. Il a...'

--- DEBUG : ANALYSE EXPERTE ---
M. M., 75 ans, habite  La Seyne-sur-Mer. Il a de graves problmes de vue et sa femme, qui s'occupait de tout, vient d'tre hospitalise. Il se retrouve seul et n'arrive plus  prparer ses repas ni  prendre ses mdicaments.
Ville extraite : La Seyne-sur-Mer
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : non_renseigne
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 75,
  "usager.localisation.commune_residence": "La Seyne-sur-Mer",
  "usager.situation_actuelle.APA": "inconnu",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
  "demande.proposition_mail": "Monsieur M., g de 75 ans et habitant  La Seyne-sur-Mer, est isol depuis l'hospitalisation de sa femme. Il a des problmes de vue et ne peut plus prparer ses repas ni prendre ses mdicaments.",
  "demande.resume_structur": "M. M., 75 ans, habite  La Seyne-sur-Mer. Il a de graves problmes de vue et sa femme, qui s'occupait de tout, vient d'tre hospitalise. Il se retrouve seul et n'arrive plus  prparer ses repas ni  prendre ses mdicaments.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 100,
    "aidant_regulier": 100,
    "medecin_traitant": 0,
    "malveillance": 100,
    "urgence": 100,
    "hospitalisation": 100,
    "motif": 100,
    "etat_logement": 0
  },
  "evaluation.comid.justifications": [
    {
      "code": "multimorbidite",
      "justification": "de graves problmes de vue et sa femme, qui s'occupait de tout, vient d'tre hospitalise.",
      "confiance": 70
    },
    {
      "code": "douleurs",
      "justification": "de graves problmes de vue",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "il se retrouve seul",
      "confiance": 95
    },
    {
      "code": "logement_inadapte",
      "justification": "il n'arrive plus  prparer ses repas ni  prendre ses mdicaments",
      "confiance": 70
    }
  ],
  "evaluation.confiance.comid": {
    "multimorbidite": 70,
    "douleurs": 95,
    "isolement_social": 95,
    "logement_inadapte": 70
  },
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": true,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": true,
  "evaluation.comid.logement_inadapte": true,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": false,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 4 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (La Seyne-sur-Mer)...

--- RESULTATS DE L'ORIENTATION ---

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 60
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 60 pts).
Contact : 04 94 06 97 04 | None

[ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ] - Priorite : 40
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 40 pts).
Contact : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chnes 83500 LA SEYNE SUR MER

[ DAC - Dispositif d'Appui  la Coordination ] - Priorite : 10
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 10 pts).
Contact : 04 94 35 32 01 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Fontaine (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Fontaine (Alerte Kin) ---

1. Extraction IA pour l'alerte du kin...

--- DEBUG : ANALYSE EXPERTE ---
Patient de 85 ans  Sanary, en situation de perte d'autonomie et de dnutrition, avec un aidant agressif.
Ville extraite : Sanary
Mdecin : identifie
Malveillance : spoliation_financiere
Hospitalisation : aucun
tat Logement : incurie
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 85,
  "usager.localisation.commune_residence": "Sanary",
  "usager.situation_actuelle.APA": "inconnu",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "spoliation_financiere",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "aide_alimentaire",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "incurie",
  "demande.proposition_mail": "Mme F., ge de 85 ans et habitant  Sanary, est en difficult pour se nourrir et subit des pressions financires de la part de son fils. Nous sollicitons votre intervention pour une valuation globale et un soutien  domicile.",
  "demande.resume_structur": "Patient de 85 ans  Sanary, en situation de perte d'autonomie et de dnutrition, avec un aidant agressif.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 100,
    "aidant_regulier": 100,
    "medecin_traitant": 100,
    "malveillance": 100,
    "urgence": 100,
    "hospitalisation": 100,
    "motif": 100,
    "etat_logement": 100
  },
  "evaluation.comid.justifications": [
    {
      "code": "precarite_financiere",
      "justification": "son frigo est littralement vide",
      "confiance": 95
    },
    {
      "code": "troubles_cognitifs",
      "justification": "oublie ses mdicaments",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "elle a l'air terrorise",
      "confiance": 70
    },
    {
      "code": "agressivite",
      "justification": "son fils qui vit avec elle : il est trs agressif",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "precarite_financiere": 95,
    "troubles_cognitifs": 95,
    "isolement_social": 70,
    "agressivite": 95,
    "logement_inadapte": 100,
    "lourdeur_reseau": 100
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": true,
  "evaluation.comid.precarite_financiere": true,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": true,
  "evaluation.comid.logement_inadapte": true,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": false,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": true,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": true,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 6 (Situation  risque de complexit)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Sanary-sur-Mer)...

--- REPONSE D'ORIA POUR LE KINE ---
ORIA : 'Situation identifie comme Situation  risque de complexit. Voici les actions prioritaires :'

ACTION : [ CEV - Cellule coute et Vigilance (Violences & Spoliation) ]
MOTIF : Orientation clinique recommande par l'valuation clinique multicritre (Score : 85 pts).
CONTACT : 04 83 95 16 01

ACTION : [ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ]
MOTIF : Orientation clinique recommande par l'valuation clinique multicritre (Score : 85 pts).
CONTACT : 04 83 95 83 10

ACTION : [ UTS Littoral Sud Sainte Baume - SANARY (Relais CLIC) ]
MOTIF : La commune ne dispose pas de CLIC, se rapprocher de l'UTS. Orientation clinique recommande par l'valuation clinique multicritre (Score : 45 pts).
CONTACT : 04 83 95 83 10

ACTION : [ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ]
MOTIF : Orientation clinique recommande par l'valuation clinique multicritre (Score : 45 pts).
CONTACT : 06 84 99 32 49

ACTION : [ DAC - Dispositif d'Appui  la Coordination ]
MOTIF : Orientation clinique recommande par l'valuation clinique multicritre (Score : 35 pts).
CONTACT : 04 94 35 32 01

ACTION : [ CCAS - Centre Communal d'Action Sociale ]
MOTIF : Orientation clinique recommande par l'valuation clinique multicritre (Score : 35 pts).
CONTACT : 04 94 88 50 70

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Gautier (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Jeanne Gautier (Trs Complexe) ---

1. Extraction IA pour le cas trs complexe...

--- DEBUG : ANALYSE EXPERTE ---
Analyse manquante
Ville extraite : Toulon
Mdecin : identifie
Malveillance : aucune
Hospitalisation : aucun
tat Logement : incurie
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 90,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "incurie",
  "demande.proposition_mail": "Mme G., ge de 90 ans et habitant  Toulon, traverse une priode de transition majeure suite au dcs rcent de son poux. Elle prsente une grave dpression clinique avec des ides noires, un diabte de type 2, une insuffisance cardiaque et une arthrose dformante qui lui causent des douleurs chroniques permanentes et intolrables. Son ordonnance est extrmement lourde avec une polymdication de plus de 9 mdicaments par jour. Elle vit seule dans un logement insalubre et inadapt, situ au 3me tage sans ascenseur. Sa retraite de 800  ne lui permet plus de faire face  ses factures d'lectricit, crant une grande prcarit financire. Sa fille unique est en situation d'puisement total de l'aidant rgulier et ne peut plus l'assister. De plus, Mme G. est trs angoisse par sa sant, mais elle s'oppose de manire hostile aux soins et refuse d'ouvrir aux infirmiers  domicile. Depuis sa chute rcente avec fracture du poignet, elle prsente une perte d'autonomie rcente pour toutes les activits de la vie quotidienne. Son tat de sant est instable et caractris par une forte imprvisibilit.",
  "demande.resume_structur": "",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 100,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 100,
    "aidant_regulier": 100,
    "medecin_traitant": 100,
    "malveillance": 100,
    "urgence": 100,
    "hospitalisation": 100,
    "motif": 100,
    "etat_logement": 100
  },
  "evaluation.comid.justifications": [
    {
      "code": "multimorbidite",
      "justification": "diabte de type 2, insuffisance cardiaque et arthrose dformante",
      "confiance": 95
    },
    {
      "code": "douleurs",
      "justification": "souffre d'une arthrose dformante qui lui cause des douleurs chroniques permanentes",
      "confiance": 95
    },
    {
      "code": "polymedication",
      "justification": "ordonnance extrmement lourde avec une polymdication de plus de 9 mdicaments par jour",
      "confiance": 95
    },
    {
      "code": "troubles_cognitifs",
      "justification": "prsente des troubles cognitifs majeurs avec une perte de mmoire et une dsorientation temporelle",
      "confiance": 95
    },
    {
      "code": "precarite_financiere",
      "justification": "sa retraite de 800  ne lui permet plus de faire face  ses factures d'lectricit, crant une grande prcarit financire",
      "confiance": 95
    },
    {
      "code": "epuisement_aidant",
      "justification": "sa fille unique est en situation d'puisement total de l'aidant rgulier et ne peut plus l'assister",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "vit seule dans un logement insalubre et inadapt, situ au 3me tage sans ascenseur",
      "confiance": 95
    },
    {
      "code": "logement_inadapte",
      "justification": "logement insalubre et inadapt, situ au 3me tage sans ascenseur",
      "confiance": 95
    },
    {
      "code": "depression",
      "justification": "prsente une grave dpression clinique avec des ides noires",
      "confiance": 95
    },
    {
      "code": "perte_autonomie_recente",
      "justification": "prsente une perte d'autonomie rcente pour toutes les activits de la vie quotidienne",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "multimorbidite": 95,
    "douleurs": 95,
    "polymedication": 95,
    "troubles_cognitifs": 95,
    "precarite_financiere": 95,
    "epuisement_aidant": 95,
    "isolement_social": 95,
    "logement_inadapte": 100,
    "depression": 95,
    "perte_autonomie_recente": 95,
    "opposition_soins": 0
  },
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": true,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
  "evaluation.comid.troubles_cognitifs": true,
  "evaluation.comid.precarite_financiere": true,
  "evaluation.comid.epuisement_aidant": true,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": true,
  "evaluation.comid.logement_inadapte": true,
  "evaluation.comid.depression": true,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": false,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": true,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": true,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 11 (Situation complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION ---

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 175
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 175 pts).
Contact : 04 94 24 65 25 | None

[ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ] - Priorite : 165
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 165 pts).
Contact : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chnes 83500 LA SEYNE SUR MER

[ DAC - Dispositif d'Appui  la Coordination ] - Priorite : 150
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 150 pts).
Contact : 04 94 35 32 01 | None

[ CCAS - Centre Communal d'Action Sociale ] - Priorite : 90
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 90 pts).
Contact : 04 94 24 65 00 | 100 rue des remparts - CS 20813 83051 Toulon Cedex

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorite : 85
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 85 pts).
Contact : 04 83 95 24 42 | 100, traverse des minimes 83000 Toulon

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Vial (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Vial (Recherche Mdecin Traitant) ---

1. Extraction IA pour : 'Mme Vial, 82 ans, vient de s'installer  Toulon po...'

--- DEBUG : ANALYSE EXPERTE ---
Mme V., 82 ans, vient de s'installer  Toulon pour se rapprocher de sa fille. Elle souffre de diabte de type 2 et d'hypertension. Elle n'a plus de mdecin traitant car elle a dmnag et son ancien cabinet est trop loin. Elle a appel plusieurs mdecins dans son nouveau quartier mais aucun ne prend de nouveaux patients. Elle commence  manquer de mdicaments et elle est trs angoisse par cette rupture de suivi mdical. Sa fille travaille beaucoup et s'inquite de ne pas trouver de solution pour sa mre.
Ville extraite : Toulon
Mdecin : absent
Malveillance : aucune
Hospitalisation : aucun
tat Logement : propre
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 82,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "inconnu",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "recherche_medecin",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "demande.proposition_mail": "Mme V., 82 ans, vient de dmnager  Toulon pour se rapprocher de sa fille. Elle souffre de diabte de type 2 et d'hypertension et n'a plus de mdecin traitant. Elle a appel plusieurs mdecins dans son nouveau quartier mais aucun ne prend de nouveaux patients. Elle manque de mdicaments et est trs angoisse par cette rupture de suivi mdical.",
  "demande.resume_structur": "Mme V., 82 ans, vient de s'installer  Toulon pour se rapprocher de sa fille. Elle souffre de diabte de type 2 et d'hypertension. Elle n'a plus de mdecin traitant car elle a dmnag et son ancien cabinet est trop loin. Elle a appel plusieurs mdecins dans son nouveau quartier mais aucun ne prend de nouveaux patients. Elle commence  manquer de mdicaments et elle est trs angoisse par cette rupture de suivi mdical. Sa fille travaille beaucoup et s'inquite de ne pas trouver de solution pour sa mre.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 100,
    "aidant_regulier": 100,
    "medecin_traitant": 100,
    "malveillance": 100,
    "urgence": 100,
    "hospitalisation": 100,
    "motif": 100,
    "etat_logement": 100
  },
  "evaluation.comid.justifications": [
    {
      "code": "multimorbidite",
      "justification": "souffre de diabte de type 2 et d'hypertension",
      "confiance": 100
    },
    {
      "code": "anxiete",
      "justification": "trs angoisse",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "multimorbidite": 100,
    "anxiete": 95
  },
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": false,
  "evaluation.comid.logement_inadapte": false,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": true,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": null
}

2. Calcul du score de complexit COMID...
Score Total : 2 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux...
Ville extraite par l'IA : Toulon

--- RESULTATS DE L'ORIENTATION (Territoire: Toulon - Canton 1, 2 et 3) ---

[ CPTS - Communaut Professionnelle Territoriale de Sant ] - Priorite : 130
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 130 pts).
Contact : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 25
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 25 pts).
Contact : 04 94 24 65 25 | None

[ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ] - Priorite : 25
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 25 pts).
Contact : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chnes 83500 LA SEYNE SUR MER

[ DAC - Dispositif d'Appui  la Coordination ] - Priorite : 10
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 10 pts).
Contact : 04 94 35 32 01 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Michu (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Michu ---

1. Extraction IA pour : 'Mme Michu, 82 ans, vit seule  Toulon dans son app...'

--- DEBUG : ANALYSE EXPERTE ---
Mme M., 82 ans, vit seule  Toulon dans son appartement. Elle commence  oublier de manger, elle a chut la semaine dernire mais n'a pas t hospitalise. Elle refuse l'aide  domicile car elle dit qu'elle peut tout faire seule, mais sa fille est puise et trs inquite.
Ville extraite : Toulon
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : propre
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 82,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "demande.proposition_mail": "Mme M., ge de 82 ans et vivant  Toulon, refuse les soins prescrits et demande une aide  domicile. Sa fille est puise et inquite.",
  "demande.resume_structur": "Mme M., 82 ans, vit seule  Toulon dans son appartement. Elle commence  oublier de manger, elle a chut la semaine dernire mais n'a pas t hospitalise. Elle refuse l'aide  domicile car elle dit qu'elle peut tout faire seule, mais sa fille est puise et trs inquite.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 100,
    "aidant_regulier": 100,
    "medecin_traitant": 0,
    "malveillance": 90,
    "urgence": 95,
    "hospitalisation": 95,
    "motif": 100,
    "etat_logement": 80
  },
  "evaluation.comid.justifications": [
    {
      "code": "troubles_cognitifs",
      "justification": "elle commence  oublier de manger",
      "confiance": 95
    },
    {
      "code": "perte_autonomie_recente",
      "justification": "elle a chut la semaine dernire mais n'a pas t hospitalise",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "troubles_cognitifs": 95,
    "perte_autonomie_recente": 95,
    "opposition_soins": 0
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": true,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": false,
  "evaluation.comid.logement_inadapte": false,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": false,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": true,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": true,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": null
}

2. Calcul du score de complexit COMID...
Score Total : 3 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION ---

[ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ] - Priorite : 125
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 125 pts).
Contact : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chnes 83500 LA SEYNE SUR MER

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 120
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 120 pts).
Contact : 04 94 24 65 25 | None

[ DAC - Dispositif d'Appui  la Coordination ] - Priorite : 50
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 50 pts).
Contact : 04 94 35 32 01 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Petit (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Petit (Aidant Conjoint Epuis) ---

1. Extraction IA pour le rcit du conjoint aidant...

--- DEBUG : ANALYSE EXPERTE ---
Patient de 83 ans  Toulon, en difficult pour sortir du logement et ncessitant un hbergement temporaire pour permettre une opration du dos.
Ville extraite : Toulon
Mdecin : identifie
Malveillance : aucune
Hospitalisation : aucun
tat Logement : non_renseigne
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 83,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "oui",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
  "demande.proposition_mail": "Monsieur, g de 83 ans et habitant  Toulon, est en difficult pour sortir de son logement sans ascenseur. Il a besoin d'un hbergement temporaire pour permettre une opration du dos.",
  "demande.resume_structur": "Patient de 83 ans  Toulon, en difficult pour sortir du logement et ncessitant un hbergement temporaire pour permettre une opration du dos.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 100,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 100,
    "aidant_regulier": 100,
    "medecin_traitant": 100,
    "malveillance": 100,
    "urgence": 100,
    "hospitalisation": 100,
    "motif": 100,
    "etat_logement": 0
  },
  "evaluation.comid.justifications": [
    {
      "code": "epuisement_aidant",
      "justification": "Je suis au bout du rouleau",
      "confiance": 95
    },
    {
      "code": "logement_inadapte",
      "justification": "On habite  Toulon au 3me tage sans ascenseur",
      "confiance": 100
    },
    {
      "code": "perte_autonomie_recente",
      "justification": "Je dois la porter et j'ai le dos en compote",
      "confiance": 95
    },
    {
      "code": "anxiete",
      "justification": "Je sens que je fatigue",
      "confiance": 90
    }
  ],
  "evaluation.confiance.comid": {
    "epuisement_aidant": 95,
    "logement_inadapte": 100,
    "perte_autonomie_recente": 95,
    "anxiete": 90
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": true,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": false,
  "evaluation.comid.logement_inadapte": true,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": true,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": true,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": null
}

2. Calcul du score de complexit COMID...
Score Total : 4 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- REPONSE D'ORIA POUR L'AIDANT ---
voici votre priorit :'

VOTRE PRIORIT ABSOLUE : [ CLIC - Centre Local d'Information et de Coordination ]
MISSION : Orientation clinique recommande par l'valuation clinique multicritre (Score : 105 pts).
CONTACT : 04 94 24 65 25

CONSEIL POUR VOUS : 'Prenez soin de vous galement. En plus de votre rfrent APA, sachez que les plateformes de rpit peuvent vous soutenir pendant votre hospitalisation.'

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Chen (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Chen (PCH / Handicap) ---

1. Extraction IA pour : 'M. Chen, 52 ans, habite  Toulon. Il est en situat...'

--- DEBUG : ANALYSE EXPERTE ---
M. C., 52 ans, habite  Toulon et cherche des informations sur les logements adapts  son fauteuil roulant dans la commune et souhaiterait savoir s'il existe des prestataires spcialiss pour l'aide humaine le week-end.
Ville extraite : Toulon
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : non_renseigne
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 52,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "inconnu",
  "usager.situation_actuelle.PCH": "oui",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "logement",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
  "demande.proposition_mail": "Monsieur C., g de 52 ans et habitant  Toulon, cherche des informations sur les logements adapts  son fauteuil roulant dans la commune et souhaite savoir s'il existe des prestataires spcialiss pour l'aide humaine le week-end.",
  "demande.resume_structur": "M. C., 52 ans, habite  Toulon et cherche des informations sur les logements adapts  son fauteuil roulant dans la commune et souhaiterait savoir s'il existe des prestataires spcialiss pour l'aide humaine le week-end.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 100,
    "gir": 0,
    "professionnels_domicile": 100,
    "aidant_regulier": 100,
    "medecin_traitant": 0,
    "malveillance": 100,
    "urgence": 100,
    "hospitalisation": 100,
    "motif": 100,
    "etat_logement": 0
  },
  "evaluation.comid.justifications": [
    {
      "code": "logement_inadapte",
      "justification": "habite  Toulon et cherche des informations sur les logements adapts  son fauteuil roulant dans la commune",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "il est en situation de handicap moteur et bnficie de la PCH, ce qui peut entraner un isolement social",
      "confiance": 70
    }
  ],
  "evaluation.confiance.comid": {
    "logement_inadapte": 95,
    "isolement_social": 70
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": true,
  "evaluation.comid.logement_inadapte": true,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": false,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 2 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION (Cas Handicap / PCH) ---

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorite : 50
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 50 pts).
Contact : 04 83 95 24 42 | 100, traverse des minimes 83000 Toulon

[ CCAS - Centre Communal d'Action Sociale ] - Priorite : 30
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 30 pts).
Contact : 04 94 24 65 00 | 100 rue des remparts - CS 20813 83051 Toulon Cedex

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Morel (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Morel (Hpital) ---

1. Extraction IA pour : 'Mme Morel, 80 ans, est actuellement hospitalise ...'

--- DEBUG : ANALYSE EXPERTE ---
Mme M., 80 ans, est actuellement hospitalise  l'hpital Sainte Musse suite  une mauvaise chute. Elle s'inquite beaucoup pour son retour  domicile car elle vit seule au 3me tage. Elle a besoin que quelqu'un l'aide  organiser sa sortie et  remplir ses dossiers administratifs car elle a perdu ses papiers lors de son admission en urgence.
Ville extraite : La Valette
Mdecin : identifie
Malveillance : aucune
Hospitalisation : en_cours
tat Logement : propre
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 80,
  "usager.localisation.commune_residence": "La Valette",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "en_cours",
  "demande.motif_principal": "sortie_hospitalisation",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "demande.proposition_mail": "Mme M., ge de 80 ans, est hospitalise  l'hpital Sainte Musse suite  une mauvaise chute. Elle s'inquite pour son retour  domicile et a besoin d'aide pour organiser sa sortie et remplir ses dossiers administratifs.",
  "demande.resume_structur": "Mme M., 80 ans, est actuellement hospitalise  l'hpital Sainte Musse suite  une mauvaise chute. Elle s'inquite beaucoup pour son retour  domicile car elle vit seule au 3me tage. Elle a besoin que quelqu'un l'aide  organiser sa sortie et  remplir ses dossiers administratifs car elle a perdu ses papiers lors de son admission en urgence.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 100,
    "aidant_regulier": 100,
    "medecin_traitant": 80,
    "malveillance": 90,
    "urgence": 95,
    "hospitalisation": 100,
    "motif": 100,
    "etat_logement": 80
  },
  "evaluation.comid.justifications": [
    {
      "code": "perte_autonomie_recente",
      "justification": "elle a besoin que quelqu'un l'aide  organiser sa sortie et  remplir ses dossiers administratifs car elle a perdu ses papiers lors de son admission en urgence.",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "elle vit seule au 3me tage",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "perte_autonomie_recente": 95,
    "isolement_social": 95
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": true,
  "evaluation.comid.logement_inadapte": false,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": false,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": true,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 2 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION (Hopital Sainte Musse) ---

[ Service Social de l'Hpital ] - Priorite : 95
Objectif : Accompagnement social en milieu hospitalier : Organisation de la sortie et lien direct avec le service social de l'tablissement.
Contact : Non trouve dans le referentiel territorial

[ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ] - Priorite : 50
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 50 pts).
Contact : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chnes 83500 LA SEYNE SUR MER

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 45
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 45 pts).
Contact : 04 94 24 65 25 | None

[ DAC - Dispositif d'Appui  la Coordination ] - Priorite : 20
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 20 pts).
Contact : 04 94 35 32 01 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Pierre (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Antoinette (Nouveau Cas Complexe) ---

1. Extraction IA (Dterministe, Temp=0.0) pour : 'M. Pierre age de 88 ans vis seul  domicile polypathologie avais oubli ma visi...'

--- DEBUG : ANALYSE EXPERTE ---
Analyse manquante
Ville extraite : Toulon
Mdecin : absent
Malveillance : aucune
Hospitalisation : aucun
tat Logement : non_renseigne
--- FIN DEBUG ---

Donnes extraites (JSON) :
{
  "usager.identite.age_estime": 88,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
  "demande.proposition_mail": "Monsieur, g de 88 ans et vivant  Toulon, a oubli sa visite mdicale prvue. Il vit seul  domicile et bnficie d'un aide pour faire ses courses. Il est polypathologue et a une difficult  la marche.",
  "demande.resume_structur": "",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 100,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 100,
    "aidant_regulier": 100,
    "medecin_traitant": 100,
    "malveillance": 100,
    "urgence": 100,
    "hospitalisation": 100,
    "motif": 100,
    "etat_logement": 0
  },
  "evaluation.comid.justifications": [
    {
      "code": "addiction",
      "justification": "addiction  l'alcool",
      "confiance": 100
    },
    {
      "code": "troubles_cognitifs",
      "justification": "oubli ma visite prvue",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "vit seul  domicile",
      "confiance": 95
    },
    {
      "code": "logement_inadapte",
      "justification": "refrigirateur ne fonctionne plus",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "addiction": 100,
    "troubles_cognitifs": 95,
    "isolement_social": 95,
    "logement_inadapte": 95,
    "multimorbidite": 100
  },
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": true,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": true,
  "evaluation.comid.logement_inadapte": true,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": true,
  "evaluation.comid.anxiete": false,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 5 (Situation non complexe)

3. valuation de l'orientation...

4. Recherche des contacts territoriaux (La Garde)...

--- RSULTATS DE L'ORIENTATION POUR MME ANTOINETTE ---

[ CLIC - Centre Local d'Information et de Coordination ] - Priorit : 80
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 80 pts).
Contact : 04 22 44 84 73 | None

[ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ] - Priorit : 60
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 60 pts).
Contact : 06 83 38 39 39 | 421 Av 1er Bataillon Infanterie de Marine du Pacifique 83130 La Garde

[ CPTS - Communaut Professionnelle Territoriale de Sant ] - Priorit : 50
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 50 pts).
Contact : 06 63 63 63 91 | 3 Rue Aspirant Franois Philippe 83260 La Crau

[ DAC - Dispositif d'Appui  la Coordination ] - Priorit : 20
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 20 pts).
Contact : 04 94 35 32 01 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Bernard (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Bernard (Suspicion de maltraitance) ---

1. Extraction IA pour : 'Mme Bernard, 88 ans, habite  La Seyne-sur-Mer. El...'

--- DEBUG : ANALYSE EXPERTE ---
Mme B., 88 ans, habitante  La Seyne-sur-Mer, est trs isole. Elle est victime de spoliation financire par son petit-fils qui lui vole de l'argent. Elle est terrorise  l'ide de parler et trs amaigrie.
Ville extraite : La Seyne-sur-Mer
Mdecin : incertain
Malveillance : spoliation_financiere
Hospitalisation : aucun
tat Logement : non_renseigne
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 88,
  "usager.localisation.commune_residence": "La Seyne-sur-Mer",
  "usager.situation_actuelle.APA": "inconnu",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "spoliation_financiere",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "aide_alimentaire",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
  "demande.proposition_mail": "Mme B., 88 ans, habitante  La Seyne-sur-Mer, est victime de spoliation financire par son petit-fils qui lui vole de l'argent. Elle est terrorise  l'ide de parler et trs amaigrie.",
  "demande.resume_structur": "Mme B., 88 ans, habitante  La Seyne-sur-Mer, est trs isole. Elle est victime de spoliation financire par son petit-fils qui lui vole de l'argent. Elle est terrorise  l'ide de parler et trs amaigrie.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 100,
    "aidant_regulier": 100,
    "medecin_traitant": 0,
    "malveillance": 100,
    "urgence": 100,
    "hospitalisation": 100,
    "motif": 100,
    "etat_logement": 0
  },
  "evaluation.comid.justifications": [
    {
      "code": "isolement_social",
      "justification": "trs isole",
      "confiance": 100
    },
    {
      "code": "precarite_financiere",
      "justification": "son compte est vide",
      "confiance": 95
    },
    {
      "code": "perte_autonomie_recente",
      "justification": "ne plus de quoi s'acheter  manger",
      "confiance": 95
    },
    {
      "code": "troubles_cognitifs",
      "justification": "ecchymoses suspectes sur les bras",
      "confiance": 70
    }
  ],
  "evaluation.confiance.comid": {
    "isolement_social": 100,
    "precarite_financiere": 95,
    "perte_autonomie_recente": 95,
    "troubles_cognitifs": 70,
    "lourdeur_reseau": 100
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": true,
  "evaluation.comid.precarite_financiere": true,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": true,
  "evaluation.comid.logement_inadapte": false,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": false,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": true,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": true,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 5 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux...
Ville extraite par l'IA : La Seyne-sur-Mer

--- RESULTATS DE L'ORIENTATION (Territoire: La Seyne-sur-mer) ---

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 95
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 95 pts).
Contact : 04 94 06 97 04 | None

[ CCAS - Centre Communal d'Action Sociale ] - Priorite : 90
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 90 pts).
Contact : 04 94 06 97 18 | Espace Herms 2 avenue Charles-Gide 83500 La Seyne-sur-Mer

[ CEV - Cellule coute et Vigilance (Violences & Spoliation) ] - Priorite : 85
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 85 pts).
Contact : 04 83 95 16 01 | None

[ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ] - Priorite : 70
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 70 pts).
Contact : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chnes 83500 LA SEYNE SUR MER

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorite : 55
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 55 pts).
Contact : 04 83 95 48 30 ou 04 83 95 37 99 | rue Charles Gide 83500 La Seyne sur mer

[ DAC - Dispositif d'Appui  la Coordination ] - Priorite : 30
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 30 pts).
Contact : 04 94 35 32 01 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Dubois (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Dubois ---

1. Extraction IA pour : 'M. Dubois, 74 ans, vit  Toulon. Il souffre de dia...'

--- DEBUG : ANALYSE EXPERTE ---
Patient de 74 ans  Toulon, souffrant de diabte, d'hypertension et d'insuffisance rnale chronique, en difficult pour payer son loyer et ses factures, demandant un accompagnement social.
Ville extraite : Toulon
Mdecin : identifie
Malveillance : aucune
Hospitalisation : aucun
tat Logement : propre
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 74,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "inconnu",
  "usager.cadre_de_vie.aidant_regulier": "inconnu",
  "usager.cadre_de_vie.etat_logement": "propre",
  "demande.proposition_mail": "Monsieur, g de 74 ans et habitant  Toulon, souffre de diabte, d'hypertension et d'insuffisance rnale chronique. Il a besoin d'un accompagnement social pour l'aider dans ses dmarches administratives et payer son loyer et ses factures.",
  "demande.resume_structur": "Patient de 74 ans  Toulon, souffrant de diabte, d'hypertension et d'insuffisance rnale chronique, en difficult pour payer son loyer et ses factures, demandant un accompagnement social.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 100,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 0,
    "aidant_regulier": 0,
    "medecin_traitant": 100,
    "malveillance": 100,
    "urgence": 100,
    "hospitalisation": 100,
    "motif": 100,
    "etat_logement": 100
  },
  "evaluation.comid.justifications": [
    {
      "code": "multimorbidite",
      "justification": "souffre de diabte, d'hypertension et d'une insuffisance rnale chronique",
      "confiance": 95
    },
    {
      "code": "douleurs",
      "justification": "souffre en permanence dans les jambes",
      "confiance": 95
    },
    {
      "code": "polymedication",
      "justification": "prend 8 mdicaments par jour",
      "confiance": 95
    },
    {
      "code": "precarite_financiere",
      "justification": "a du mal  payer son loyer et ses factures",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "vit seule",
      "confiance": 70
    },
    {
      "code": "logement_inadapte",
      "justification": "appartement au 4me tage sans ascenseur",
      "confiance": 95
    },
    {
      "code": "anxiete",
      "justification": "est trs anxieux pour sa sant",
      "confiance": 100
    }
  ],
  "evaluation.confiance.comid": {
    "multimorbidite": 95,
    "douleurs": 95,
    "polymedication": 95,
    "precarite_financiere": 95,
    "isolement_social": 70,
    "logement_inadapte": 95,
    "anxiete": 100,
    "opposition_soins": 0
  },
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": true,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": true,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": true,
  "evaluation.comid.logement_inadapte": true,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": true,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": true,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 8 (Situation  risque de complexit)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION ---

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 55
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 55 pts).
Contact : 04 94 24 65 25 | None

[ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ] - Priorite : 55
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 55 pts).
Contact : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chnes 83500 LA SEYNE SUR MER

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorite : 55
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 55 pts).
Contact : 04 83 95 24 42 | 100, traverse des minimes 83000 Toulon

[ CCAS - Centre Communal d'Action Sociale ] - Priorite : 35
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 35 pts).
Contact : 04 94 24 65 00 | 100 rue des remparts - CS 20813 83051 Toulon Cedex

[ DAC - Dispositif d'Appui  la Coordination ] - Priorite : 20
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 20 pts).
Contact : 04 94 35 32 01 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Mouton (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Georgette Mouton (Ollioules) ---

1. Extraction IA pour : 'Mme Georgette Mouton, 83 ans, vit seule  Ollioules dans un appartement devenu e...'

--- DEBUG : ANALYSE EXPERTE ---
Mme G. M., 83 ans, vit seule  Ollioules dans un appartement devenu extrmement insalubre et encombr de dchets et d'objets accumuls (syndrome de Diogne). Elle est en situation de grand isolement social et n'a aucun aidant  proximit. L'infirmire librale qui passe pour son traitement contre l'hypertension signale un risque majeur de chute et de frquents oublis de mdicaments (mise en danger). De plus, elle n'a plus de mdecin traitant depuis 6 mois et ne bnficie pas de l'APA.
Ville extraite : Ollioules
Mdecin : absent
Malveillance : aucune
Hospitalisation : aucun
tat Logement : diogene
--- FIN DEBUG ---

Donnes extraites (JSON) :
{
  "usager.identite.age_estime": 83,
  "usager.localisation.commune_residence": "Ollioules",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "inconnu",
  "usager.cadre_de_vie.aidant_regulier": "inconnu",
  "usager.cadre_de_vie.etat_logement": "diogene",
  "demande.proposition_mail": "Mme G. M., ge de 83 ans et habitant  Ollioules, vit dans un logement extrmement insalubre et encombr. Elle est isole et n'a pas d'aidant. Nous sollicitons votre intervention pour une valuation globale et un soutien  domicile.",
  "demande.resume_structur": "Mme G. M., 83 ans, vit seule  Ollioules dans un appartement devenu extrmement insalubre et encombr de dchets et d'objets accumuls (syndrome de Diogne). Elle est en situation de grand isolement social et n'a aucun aidant  proximit. L'infirmire librale qui passe pour son traitement contre l'hypertension signale un risque majeur de chute et de frquents oublis de mdicaments (mise en danger). De plus, elle n'a plus de mdecin traitant depuis 6 mois et ne bnficie pas de l'APA.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 0,
    "aidant_regulier": 0,
    "medecin_traitant": 90,
    "malveillance": 95,
    "urgence": 95,
    "hospitalisation": 95,
    "motif": 100,
    "etat_logement": 100
  },
  "evaluation.comid.justifications": [
    {
      "code": "isolement_social",
      "justification": "vit seule  Ollioules dans un appartement devenu extrmement insalubre et encombr de dchets et d'objets accumuls",
      "confiance": 95
    },
    {
      "code": "logement_inadapte",
      "justification": "appartement devenu extrmement insalubre et encombr de dchets et d'objets accumuls",
      "confiance": 95
    },
    {
      "code": "epuisement_aidant",
      "justification": "n'a aucun aidant  proximit",
      "confiance": 95
    },
    {
      "code": "troubles_cognitifs",
      "justification": "oublis de mdicaments",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "isolement_social": 95,
    "logement_inadapte": 100,
    "epuisement_aidant": 95,
    "troubles_cognitifs": 95
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": true,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": true,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": true,
  "evaluation.comid.logement_inadapte": true,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": false,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 4 (Situation non complexe)

3. valuation de l'orientation...

4. Recherche des contacts territoriaux (Ollioules)...

--- RSULTATS DE L'ORIENTATION POUR MME GEORGETTE MOUTON ---

[ UTS Littoral Sud Sainte Baume - OLLIOULES (Relais CLIC) ] - Priorit : 105
Objectif : La commune ne dispose pas de CLIC, se rapprocher de l'UTS. Orientation clinique recommande par l'valuation clinique multicritre (Score : 105 pts).
Contact : 04 83 95 58 50 | Espace Pierre Puget 2 Place Marius Trotobas 83190 Ollioules

[ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ] - Priorit : 100
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 100 pts).
Contact : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chnes 83500 LA SEYNE SUR MER

[ Les Compagnons Btisseurs (Diogne ou Incurie unique/principale) ] - Priorit : 75
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 75 pts).
Contact : Non trouv dans le rfrentiel territorial

[ DAC - Dispositif d'Appui  la Coordination ] - Priorit : 50
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 50 pts).
Contact : 04 94 35 32 01 | None

[ CPTS - Communaut Professionnelle Territoriale de Sant ] - Priorit : 50
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 50 pts).
Contact : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorit : 30
Objectif : Orientation clinique recommande par l'valuation clinique multicritre (Score : 30 pts).
Contact : 04 83 95 58 50 | Espace Pierre Puget 2 Place Marius Trotobas 83190 Ollioules

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

