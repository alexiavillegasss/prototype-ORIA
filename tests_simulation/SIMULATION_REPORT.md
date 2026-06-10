# 📋 Rapport d'Évaluation Clinique ORIA

Généré automatiquement le : `2026-06-10 15:50:13`  
Nombre de cas exécutés : **21**  
Taux de succès : **21/21**  
Temps d'exécution total : **281.77 secondes**  

## 📊 Tableau récapitulatif des Orientations

| Patient | Status | Score COMID | Orientation Principale | Temps d'exécution |
| :--- | :---: | :---: | :--- | :---: |
| **Mme Durand** | ✅ SUCCESS | 4 | `DAC - Dispositif d'Appui  la Coordination` | 14.32s |
| **Mme Huguette** | ✅ SUCCESS | 5 | `CEV - Cellule coute et Vigilance (Spoliation & Autres Dangers)` | 13.91s |
| **Mr Vacek** | ✅ SUCCESS | 5 | `CEV - Cellule coute et Vigilance (Violences Physiques & Danger Immdiat)` | 13.84s |
| **Mr Lambert** | ✅ SUCCESS | 5 | `DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)` | 16.01s |
| **Mme Petit** | ✅ SUCCESS | 2 | `CLIC - Centre Local d'Information et de Coordination (Snior)` | 10.39s |
| **Mme Lefebvre** | ✅ SUCCESS | 5 | `DAC - Dispositif d'Appui  la Coordination` | 14.00s |
| **Mr Leroy** | ✅ SUCCESS | 5 | `DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)` | 13.68s |
| **Mme Rossi** | ✅ SUCCESS | 4 | `Police / Gendarmerie (Urgence Vitale & Intervention)` | 11.22s |
| **Mme Martin** | ✅ SUCCESS | 3 | `CLIC - Centre Local d'Information et de Coordination (Snior)` | 13.28s |
| **Mr Martin** | ✅ SUCCESS | 3 | `Informations insuffisantes pour orienter` | 10.99s |
| **Mme Fontaine** | ✅ SUCCESS | 5 | `CEV - Cellule coute et Vigilance (Spoliation & Autres Dangers)` | 14.60s |
| **Mme Gautier** | ✅ SUCCESS | 10 | `DAC - Dispositif d'Appui  la Coordination` | 19.77s |
| **Mme Vial** | ✅ SUCCESS | 3 | `CPTS - Communaut Professionnelle Territoriale de Sant` | 12.33s |
| **Mme Michu** | ✅ SUCCESS | 4 | `DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)` | 11.46s |
| **Mr Petit** | ✅ SUCCESS | 6 | `PSCG SS APA - Ple Social de Solidarit et de Gestion (APA)` | 14.44s |
| **Mr Chen** | ✅ SUCCESS | 2 | `CLIC - Centre Local d'Information et de Coordination` | 12.04s |
| **Mme Morel** | ✅ SUCCESS | 3 | `Service Social de l'Hpital (Hospitalisation en cours)` | 11.70s |
| **Mr Pierre** | ✅ SUCCESS | 5 | `CLIC - Centre Local d'Information et de Coordination (Snior)` | 12.65s |
| **Mme Bernard** | ✅ SUCCESS | 5 | `CEV - Cellule coute et Vigilance (Violences Physiques & Danger Immdiat)` | 12.36s |
| **Mr Dubois** | ✅ SUCCESS | 7 | `DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)` | 17.20s |
| **Mme Mouton** | ✅ SUCCESS | 4 | `DAC - Dispositif d'Appui  la Coordination` | 11.59s |

---

## 📝 Détail des extractions et raisonnements

<details>
<summary>🔍 Cas Mme Durand (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Durand ---

1. Extraction IA pour : 'Mme Durand, 88 ans, vit  Hyres. Elle est trs co...'

--- DEBUG : ANALYSE EXPERTE ---
La situation clinique concerne une personne ge de 88 ans, vivant  Hyres, qui est confuse et dambule la nuit. Elle refuse les soins mdicaux et prsente un risque pour elle-mme et ses voisins.
Ville extraite : Hyres
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : propre
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 88,
  "usager.localisation.commune_residence": "Hyres",
  "usager.situation_actuelle.APA": "oui",
  "usager.situation_actuelle.PCH": "none",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "none",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 100,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 40,
    "aidant_regulier": 0,
    "medecin_traitant": 0,
    "malveillance": 90,
    "urgence": 80,
    "hospitalisation": 60,
    "motif": 100,
    "etat_logement": 90
  },
  "evaluation.comid.justifications": [
    {
      "code": "troubles_cognitifs",
      "justification": "elle est trs confuse",
      "confiance": 95
    },
    {
      "code": "agressivite",
      "justification": "elle est agressive avec les infirmiers",
      "confiance": 95
    },
    {
      "code": "opposition_soins",
      "justification": "elle refuse qu'ils entrent",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "elle vit  Hyres seule",
      "confiance": 70
    }
  ],
  "evaluation.confiance.comid": {
    "troubles_cognitifs": 95,
    "agressivite": 95,
    "opposition_soins": 95,
    "isolement_social": 70
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": true,
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
  "evaluation.comid.agressivite": true,
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
Score Total : 4 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Hyres)...

--- RESULTATS DE L'ORIENTATION ---

[ DAC - Dispositif d'Appui  la Coordination ] - Priorite : 105
Objectif : Motifs d'orientation combins :
  - [Refus de soins ou d'aide (Priorit Absolue)] (Confiance : 97%) : Refus de soins ou opposition critique aux aides  domicile : Rupture critique de parcours ncessitant l'intervention immdiate du DAC pour dbloquer la situation.
    -> Justification confiance : variable 'motif' extraite avec certitude de 100%, critre COMID 'opposition_soins' dtect avec certitude de 95%
  - [Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)] (Confiance : 88%) : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
    -> Justification confiance : score complexit COMID estim  88% de certitude, score complexit COMID estim  88% de certitude
Contact : Non trouve dans le referentiel territorial

[ PSCG SS APA - Ple Social de Solidarit et de Gestion (APA) ] - Priorite : 100
Objectif : Contacter votre rfrent APA au Conseil Dpartemental (PSCG SS APA) pour toute modification de plan d'aide ou besoin d'accompagnement social supplmentaire.
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
Analyse manquante
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
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "insalubre",
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
    "urgence": 70,
    "hospitalisation": 0,
    "motif": 100,
    "etat_logement": 90
  },
  "evaluation.comid.justifications": [
    {
      "code": "isolement_social",
      "justification": "Mme H. vit seule dans un logement insalubre et humide  La Valette du Var.",
      "confiance": 95
    },
    {
      "code": "precarite_financiere",
      "justification": "Elle n'a pas l'APA et vit sous le seuil de pauvret avec une infime pension de retraite.",
      "confiance": 95
    },
    {
      "code": "logement_inadapte",
      "justification": "Le logement est insalubre et humide.",
      "confiance": 95
    },
    {
      "code": "conflit_reseau",
      "justification": "Un neveu d'Huguette, qui a procuration sur ses comptes bancaires, effectue des retraits d'argent massifs et rpts sans justification.",
      "confiance": 95
    },
    {
      "code": "lourdeur_reseau",
      "justification": "Huguette est terrifie par son neveu et n'ose rien dire par peur de reprsailles.",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "isolement_social": 95,
    "precarite_financiere": 95,
    "logement_inadapte": 100,
    "conflit_reseau": 95,
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
  "evaluation.comid.anxiete": false,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": true,
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

[ CEV - Cellule coute et Vigilance (Spoliation & Autres Dangers) ] - Priorit : 107 | Confiance : 45%
Justification confiance : variable 'ville' extraite avec certitude de 100%, variable 'etat_logement' extraite avec certitude de 90%, variable 'motif' extraite avec certitude de 100%, donne 'vulnerabilites.habitat.securite_du_domicile' manquante, variable 'hospitalisation' extraite avec certitude de 0%, variable 'malveillance' extraite avec certitude de 100% (Pnalit de compltude applique de -20% pour 1 variable(s) manquante(s))
Objectif : Mise en scurit immdiate, protection juridique et physique des majeurs vulnrables en situation de danger social ou maltraitance financire.
Contact : 04 83 95 16 01 | None

[ DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social) ] - Priorit : 72 | Confiance : 97%
Justification confiance : score complexit COMID estim  97% de certitude, score complexit COMID estim  97% de certitude
Objectif : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
Contact : 04 94 35 32 01 | None

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorit : 70 | Confiance : 45%
Justification confiance : donne 'vulnerabilites.social.precarite' manquante, critre COMID 'precarite_financiere' dtect avec certitude de 95%, variable 'motif' extraite avec certitude de 100% (Pnalit de compltude applique de -20% pour 1 variable(s) manquante(s))
Objectif : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
Contact : 04 83 95 56 90 | 427 Avenue Duchatel 83130 La Valette du Var

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Vacek (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Vacek (Habitat Indigne & Danger) ---

1. Extraction IA pour la situation de pril...

--- DEBUG : ANALYSE EXPERTE ---
M. V., 65 ans, vit dans un appartement insalubre  Toulon, sans eau courante ni plafond stable.
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
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "inconnu",
  "usager.cadre_de_vie.etat_logement": "insalubre",
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
    "urgence": 80,
    "hospitalisation": 0,
    "motif": 100,
    "etat_logement": 90
  },
  "evaluation.comid.justifications": [
    {
      "code": "logement_inadapte",
      "justification": "Son appartement est insalubre : il n'a plus d'eau courante depuis 3 mois et le plafond de sa chambre menace de s'effondrer suite  une infiltration.",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "Il vit dans l'humidit totale et il commence  avoir des problmes respiratoires srieux.",
      "confiance": 70
    },
    {
      "code": "precarite_financiere",
      "justification": "Son propritaire est un marchand de sommeil qui le menace physiquement s'il appelle la mairie. Il n'a plus de revenus car son dossier de retraite est bloqu.",
      "confiance": 90
    },
    {
      "code": "anxiete",
      "justification": "Il est terrifi, il n'a plus de revenus car son dossier de retraite est bloqu.",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "logement_inadapte": 100,
    "isolement_social": 70,
    "precarite_financiere": 90,
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

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- REPONSE D'ORIA (URGENCE HABITAT) ---
ORIA : 'La situation de M. Vacek prsente un DANGER IMMINENT.'

VOTRE PRIORIT ABSOLUE : [ CEV - Cellule coute et Vigilance (Violences Physiques & Danger Immdiat) ]
MISSION : Mise en scurit immdiate et protection d'urgence des majeurs vulnrables en situation de violence physique active ou menace.
CONTACT : 04 83 95 16 01

ENSUITE (VOLET SOCIAL) : [ DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social) ]
MISSION : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Lambert (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Lambert (Appel Infirmire) ---

1. Extraction IA pour le rcit de l'infirmire...

--- DEBUG : ANALYSE EXPERTE ---
Le patient est un homme de 78 ans qui vit  La Seyne. Il a des difficults pour se prendre en charge et son logement est dans un tat insalubre. Il refuse les soins mdicaux et il y a une urgence faible.
Ville extraite : La Seyne
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : insalubre
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
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "insalubre",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 70,
    "aidant_regulier": 70,
    "medecin_traitant": 0,
    "malveillance": 90,
    "urgence": 80,
    "hospitalisation": 100,
    "motif": 100,
    "etat_logement": 90
  },
  "evaluation.comid.justifications": [
    {
      "code": "isolement_social",
      "justification": "son appartement, qui tait impeccable, est devenu un dpotoir : il y a des sacs poubelles partout et a sent trs fort l'urine.",
      "confiance": 95
    },
    {
      "code": "perte_autonomie_recente",
      "justification": "il refuse que j'entre faire ses pansements, il me crie dessus et me dit que je veux l'empoisonner avec ses mdicaments.",
      "confiance": 95
    },
    {
      "code": "troubles_cognitifs",
      "justification": "il refuse que j'entre faire ses pansements, il me crie dessus et me dit que je veux l'empoisonner avec ses mdicaments.",
      "confiance": 95
    },
    {
      "code": "logement_inadapte",
      "justification": "son appartement, qui tait impeccable, est devenu un dpotoir : il y a des sacs poubelles partout et a sent trs fort l'urine.",
      "confiance": 95
    },
    {
      "code": "inquietude_sante",
      "justification": "il est veuf, sa famille est  Paris et ils ne dcrochent plus le tlphone.",
      "confiance": 70
    }
  ],
  "evaluation.confiance.comid": {
    "isolement_social": 95,
    "perte_autonomie_recente": 95,
    "troubles_cognitifs": 95,
    "logement_inadapte": 100,
    "inquietude_sante": 70
  },
  "evaluation.comid.multimorbidite": false,
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
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": false,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": true,
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
Score Total : 5 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (La Seyne-sur-Mer)...

--- REPONSE D'ORIA POUR L'INFIRMIERE ---
ORIA : 'D'aprs votre description, la situation de M. Lambert est Situation non complexe. Voici les priorits d'appel :'

CONTACTER : [ DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social) ]
POURQUOI : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
CONTACT : 04 94 35 32 01 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Petit (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Petit (Urgence CCAS) ---

1. Extraction IA pour : 'Mme Petit, 78 ans, habite  La Garde. Elle vit seu...'

--- DEBUG : ANALYSE EXPERTE ---
La patiente est une personne ge vivant seule et ayant des difficults financires. Elle demande de l'aide pour ses courses et ne pas avoir d'impay.
Ville extraite : La Garde
Mdecin : identifie
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
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 40,
    "aidant_regulier": 40,
    "medecin_traitant": 100,
    "malveillance": 100,
    "urgence": 70,
    "hospitalisation": 100,
    "motif": 90,
    "etat_logement": 80
  },
  "evaluation.comid.justifications": [
    {
      "code": "precarite_financiere",
      "justification": "son compte bancaire est  dcouvert",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "elle vit seule",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "precarite_financiere": 95,
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

[ CLIC - Centre Local d'Information et de Coordination (Snior) ] - Priorite : 80
Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
Contact : 04 22 44 84 73 | None

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorite : 70
Objectif : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
Contact : 04 83 95 56 50 | 53 Impasse Blriot Immeuble Le Frdric 83130 La Garde

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Lefebvre (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Lefebvre ---

1. Extraction IA pour : 'Mme Lefebvre, 65 ans, vit  La Garde. Elle est sui...'

--- DEBUG : ANALYSE EXPERTE ---
La patiente est suivie pour une bipolarit et a arrt son traitement le mois dernier. Elle consomme beaucoup d'alcool pour 'calmer ses angoisses' selon ses propres mots. Elle vit dans un appartement trs encombr (Syndrome de Diogne suspect) et ses voisins se plaignent d'odeurs fortes.
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
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "diogene",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 0,
    "aidant_regulier": 0,
    "medecin_traitant": 100,
    "malveillance": 100,
    "urgence": 40,
    "hospitalisation": 0,
    "motif": 70,
    "etat_logement": 90
  },
  "evaluation.comid.justifications": [
    {
      "code": "psychiatrie",
      "justification": "bipolarit",
      "confiance": 95
    },
    {
      "code": "addiction",
      "justification": "consomme beaucoup d'alcool pour 'calmer ses angoisses'",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "n'a plus de famille et refuse toute aide du service social",
      "confiance": 95
    },
    {
      "code": "logement_inadapte",
      "justification": "appartement trs encombr (Syndrome de Diogne suspect) et odeurs fortes",
      "confiance": 95
    },
    {
      "code": "anxiete",
      "justification": "trs angoisse pour sa sant",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "psychiatrie": 95,
    "addiction": 95,
    "isolement_social": 95,
    "logement_inadapte": 100,
    "anxiete": 95
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
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 5 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (La Garde)...

--- RESULTATS DE L'ORIENTATION ---

[ DAC - Dispositif d'Appui  la Coordination ] - Priorite : 96
Objectif : Motifs d'orientation combins :
  - [Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)] (Confiance : 96%) : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
    -> Justification confiance : score complexit COMID estim  96% de certitude, score complexit COMID estim  96% de certitude
  - [Suspicion de Diogne ou incurie] (Confiance : 90%) : Insalubrit ou ngligence critique  domicile : Suspicion ou syndrome de Diogne/incurie avr ncessitant une coordination multidimensionnelle renforce par le DAC.
    -> Justification confiance : variable 'etat_logement' extraite avec certitude de 90%
Contact : 04 94 35 32 01 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Leroy (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Leroy (Moins de 60 ans) ---

1. Extraction IA pour : 'M. Leroy, 45 ans, habite  Toulon. Il est atteint ...'

--- DEBUG : ANALYSE EXPERTE ---
Le patient est atteint d'une sclrose en plaques diagnostique il y a 2 ans. Il vit seul et ses revenus ont chut, ce qui rend difficile le paiement de son loyer.
Ville extraite : Toulon
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : propre
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 45,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 70,
    "aidant_regulier": 0,
    "medecin_traitant": 0,
    "malveillance": 100,
    "urgence": 30,
    "hospitalisation": 0,
    "motif": 90,
    "etat_logement": 80
  },
  "evaluation.comid.justifications": [
    {
      "code": "multimorbidite",
      "justification": "Il est atteint d'une Sclrose en Plaques (SEP) diagnostique il y a 2 ans.",
      "confiance": 95
    },
    {
      "code": "douleurs",
      "justification": "Sa sant se dgrade rapidement et il a d arrter son activit professionnelle.",
      "confiance": 70
    },
    {
      "code": "precarite_financiere",
      "justification": "Il vit seul, ses revenus ont chut et il a du mal  payer son loyer.",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "Il vit seul",
      "confiance": 95
    },
    {
      "code": "depression",
      "justification": "Il exprime des ides noires.",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "multimorbidite": 95,
    "douleurs": 70,
    "precarite_financiere": 95,
    "isolement_social": 95,
    "depression": 95
  },
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": true,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": true,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": true,
  "evaluation.comid.logement_inadapte": false,
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

[ DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social) ] - Priorite : 72
Objectif : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
Contact : 04 94 35 32 01 | None

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorite : 70
Objectif : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
Contact : 04 83 95 24 42 | 100, traverse des minimes 83000 Toulon

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Rossi (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Rossi (Violences Conjugales) ---

1. Extraction IA pour : 'Mme Rossi, 70 ans, habite  Toulon. Elle vient d'a...'

--- DEBUG : ANALYSE EXPERTE ---
La situation est critique car la patiente a d quitter son domicile en urgence en raison de violences physiques subies par son mari.
Ville extraite : Toulon
Mdecin : identifie
Malveillance : violences_physiques
Hospitalisation : aucun
tat Logement : propre
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 70,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "violences_physiques",
  "adresseur.degre_urgence_percu": "critique",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "secours_urgence",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 70,
    "aidant_regulier": 0,
    "medecin_traitant": 100,
    "malveillance": 100,
    "urgence": 100,
    "hospitalisation": 0,
    "motif": 100,
    "etat_logement": 90
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
      "confiance": 95
    },
    {
      "code": "depression",
      "justification": "elle est actuellement trs angoisse",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "isolement_social": 95,
    "logement_inadapte": 95,
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

[ Police / Gendarmerie (Urgence Vitale & Intervention) ] - Priorite : 110
Objectif : Intervention immdiate des forces de l'ordre en cas d'agression physique active et en cours ou danger vital imminent.
Contact : Non trouve dans le referentiel territorial

[ CCAS - Secours d'Urgence (Alimentaire & Factures) ] - Priorite : 85
Objectif : Secours financier ou alimentaire d'urgence de proximit : Attribution d'aides extra-lgales par la mairie.
Contact : 04 94 24 65 00 | 100 rue des remparts - CS 20813 83051 Toulon Cedex

[ CLIC - Centre Local d'Information et de Coordination (Snior) ] - Priorite : 80
Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
Contact : 04 94 24 65 25 | None

[ DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social) ] - Priorite : 72
Objectif : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
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
La fille de Mme M. (82 ans) est  bout, travaillant  temps plein et passant toutes ses soires et week-ends chez sa mre. Cette dernire perd la tte, laisse le gaz allum, se relve la nuit et a dj tombe deux fois. La fille craque et a peur de devenir mchante avec sa mre.
Ville extraite : Toulon
Mdecin : identifie
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
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 70,
    "aidant_regulier": 40,
    "medecin_traitant": 90,
    "malveillance": 100,
    "urgence": 60,
    "hospitalisation": 80,
    "motif": 90,
    "etat_logement": 70
  },
  "evaluation.comid.justifications": [
    {
      "code": "epuisement_aidant",
      "justification": "Je n'en peux plus, je craque.",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "Ma mre commence  perdre la tte, elle laisse le gaz allum, elle se relve la nuit et elle est tombe deux fois.",
      "confiance": 95
    },
    {
      "code": "lourdeur_reseau",
      "justification": "Je pleure tout le temps au travail.",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "epuisement_aidant": 95,
    "isolement_social": 95,
    "lourdeur_reseau": 95
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
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
Score Total : 3 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- REPONSE D'ORIA POUR L'AIDANTE ---
ORIA : 'Je comprends votre puisement. La situation de votre mre est Situation non complexe.'

VOTRE PRIORIT ABSOLUE : [ CLIC - Centre Local d'Information et de Coordination (Snior) ]
MISSION : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
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
Analyse manquante
Ville extraite : La Seyne-sur-Mer
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : propre
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 75,
  "usager.localisation.commune_residence": "La Seyne-sur-Mer",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
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
    "urgence": 70,
    "hospitalisation": 100,
    "motif": 90,
    "etat_logement": 80
  },
  "evaluation.comid.justifications": [
    {
      "code": "multimorbidite",
      "justification": "de graves problmes de vue et sa femme, qui s'occupait de tout, vient d'tre hospitalise",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "Il se retrouve seul",
      "confiance": 95
    },
    {
      "code": "logement_inadapte",
      "justification": "Il n'arrive plus  prparer ses repas ni  prendre ses mdicaments",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "multimorbidite": 95,
    "isolement_social": 95,
    "logement_inadapte": 95
  },
  "evaluation.comid.multimorbidite": true,
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
Score Total : 3 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (La Seyne-sur-Mer)...

--- RESULTATS DE L'ORIENTATION ---

[ Informations insuffisantes pour orienter ] - Priorite : 0
Objectif : Les informations fournies ne permettent pas de determiner une orientation. Il est necessaire de recueillir plus de precisions (ex: age de la personne, commune de residence, presence d'aides comme l'APA/professionnels, description precise des difficultes ou de la demande).
Contact : Non trouve dans le referentiel territorial

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Fontaine (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Fontaine (Alerte Kin) ---

1. Extraction IA pour l'alerte du kin...

--- DEBUG : ANALYSE EXPERTE ---
La patiente est ge de 85 ans et rside  Sanary. Elle bnficie d'une rducation de la hanche mais sa situation drape car elle a perdu 5 kg en un mois, son frigo est vide et elle oublie ses mdicaments. Son fils vit avec elle et il est trs agressif, ce qui la rend terrorise.
Ville extraite : Sanary
Mdecin : identifie
Malveillance : spoliation_financiere
Hospitalisation : aucun
tat Logement : propre
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 85,
  "usager.localisation.commune_residence": "Sanary",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "spoliation_financiere",
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "aide_alimentaire",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 90,
    "aidant_regulier": 40,
    "medecin_traitant": 100,
    "malveillance": 80,
    "urgence": 60,
    "hospitalisation": 30,
    "motif": 70,
    "etat_logement": 50
  },
  "evaluation.comid.justifications": [
    {
      "code": "precarite_financiere",
      "justification": "son frigo est littralement vide",
      "confiance": 95
    },
    {
      "code": "douleurs",
      "justification": "elle oublie ses mdicaments contre la douleur",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "son fils qui vit avec elle : il est trs agressif, il lui crie dessus et j'ai remarqu qu'il lui demande de l'argent de faon trs insistante  chaque fois que je suis l.",
      "confiance": 95
    },
    {
      "code": "agressivite",
      "justification": "son fils qui vit avec elle : il est trs agressif, il lui crie dessus et j'ai remarqu qu'il lui demande de l'argent de faon trs insistante  chaque fois que je suis l.",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "precarite_financiere": 95,
    "douleurs": 95,
    "isolement_social": 95,
    "agressivite": 95,
    "lourdeur_reseau": 100
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": true,
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
Score Total : 5 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Sanary-sur-Mer)...

--- REPONSE D'ORIA POUR LE KINE ---
ORIA : 'Situation identifie comme Situation non complexe. Voici les actions prioritaires :'

ACTION : [ CEV - Cellule coute et Vigilance (Spoliation & Autres Dangers) ]
MOTIF : [/!\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] Mise en scurit immdiate, protection juridique et physique des majeurs vulnrables en situation de danger social ou maltraitance financire.
CONTACT : 04 83 95 16 01

ACTION : [ CCAS - Secours d'Urgence (Alimentaire & Factures) ]
MOTIF : Secours financier ou alimentaire d'urgence de proximit : Attribution d'aides extra-lgales par la mairie.
CONTACT : 04 94 88 50 70

ACTION : [ DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social) ]
MOTIF : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
CONTACT : 04 94 35 32 01

ACTION : [ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ]
MOTIF : [/!\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
CONTACT : 04 83 95 83 10

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Gautier (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Jeanne Gautier (Trs Complexe) ---

1. Extraction IA pour le cas trs complexe...

--- DEBUG : ANALYSE EXPERTE ---
La situation clinique est caractrise par une grave dpression clinique avec des ides noires, un diabte de type 2, une insuffisance cardiaque et une arthrose dformante. L'usager souffre galement d'une polymdication importante et prsente des troubles cognitifs majeurs.
Ville extraite : Toulon
Mdecin : identifie
Malveillance : aucune
Hospitalisation : aucun
tat Logement : insalubre
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
  "usager.cadre_de_vie.etat_logement": "insalubre",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 40,
    "aidant_regulier": 40,
    "medecin_traitant": 100,
    "malveillance": 100,
    "urgence": 70,
    "hospitalisation": 90,
    "motif": 80,
    "etat_logement": 60
  },
  "evaluation.comid.justifications": [
    {
      "code": "multimorbidite",
      "justification": "diabte de type 2, d'une insuffisance cardiaque et d'une arthrose dformante",
      "confiance": 95
    },
    {
      "code": "douleurs",
      "justification": "souffre d'un diabte de type 2, d'une insuffisance cardiaque et d'une arthrose dformante",
      "confiance": 95
    },
    {
      "code": "troubles_cognitifs",
      "justification": "prsente des troubles cognitifs majeurs avec une perte de mmoire et une dsorientation temporelle",
      "confiance": 95
    },
    {
      "code": "precarite_financiere",
      "justification": "sa retraite de 800  ne lui permet plus de faire face  ses factures d'lectricit",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "elle vit seule dans un logement insalubre et inadapt",
      "confiance": 95
    },
    {
      "code": "logement_inadapte",
      "justification": "son logement est situ au 3me tage sans ascenseur",
      "confiance": 95
    },
    {
      "code": "depression",
      "justification": "elle traverse une priode de transition majeure suite au dcs rcent de son poux, ce qui a dclench une grave dpression clinique avec des ides noires",
      "confiance": 95
    },
    {
      "code": "anxiete",
      "justification": "elle est trs angoisse par sa sant",
      "confiance": 95
    },
    {
      "code": "perte_autonomie_recente",
      "justification": "elle prsente une perte d'autonomie rcente pour toutes les activits de la vie quotidienne",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "multimorbidite": 95,
    "douleurs": 95,
    "troubles_cognitifs": 95,
    "precarite_financiere": 95,
    "isolement_social": 95,
    "logement_inadapte": 100,
    "depression": 95,
    "anxiete": 95,
    "perte_autonomie_recente": 95,
    "opposition_soins": 0
  },
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": true,
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
Score Total : 10 (Situation complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION ---

[ DAC - Dispositif d'Appui  la Coordination ] - Priorite : 105
Objectif : Motifs d'orientation combins :
  - [Refus de soins ou d'aide (Priorit Absolue)] (Confiance : 40%) : Refus de soins ou opposition critique aux aides  domicile : Rupture critique de parcours ncessitant l'intervention immdiate du DAC pour dbloquer la situation.
    -> Justification confiance : variable 'motif' extraite avec certitude de 80%, critre COMID 'opposition_soins' dtect avec certitude de 0%
  - [Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)] (Confiance : 86%) : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
    -> Justification confiance : score complexit COMID estim  86% de certitude, score complexit COMID estim  86% de certitude
Contact : 04 94 35 32 01 | None

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorite : 70
Objectif : [/!\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
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
La patiente, ge de 82 ans, souffre de diabte et d'hypertension. Elle a dmnag et n'a plus de mdecin traitant. Elle est angoisse par cette rupture de suivi mdical.
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
  "usager.situation_actuelle.APA": "non",
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
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 40,
    "aidant_regulier": 40,
    "medecin_traitant": 90,
    "malveillance": 100,
    "urgence": 60,
    "hospitalisation": 80,
    "motif": 100,
    "etat_logement": 90
  },
  "evaluation.comid.justifications": [
    {
      "code": "multimorbidite",
      "justification": "souffre de diabte de type 2 et d'hypertension",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "elle vient de s'installer  Toulon pour se rapprocher de sa fille",
      "confiance": 70
    },
    {
      "code": "anxiete",
      "justification": "elle est trs angoisse par cette rupture de suivi mdical",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "multimorbidite": 95,
    "isolement_social": 70,
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
  "evaluation.comid.isolement_social": true,
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
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 3 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux...
Ville extraite par l'IA : Toulon

--- RESULTATS DE L'ORIENTATION (Territoire: Toulon - Canton 1, 2 et 3) ---

[ CPTS - Communaut Professionnelle Territoriale de Sant ] - Priorite : 50
Objectif : Accs aux soins : Recherche de mdecin traitant (justifie par retraite/dmnagement) et dispositif MISAS pour viter le renoncement aux soins.
Contact : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Michu (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Michu ---

1. Extraction IA pour : 'Mme Michu, 82 ans, vit seule  Toulon dans son app...'

--- DEBUG : ANALYSE EXPERTE ---

Ville extraite : Toulon
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : None
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 82,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "none",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "none",
  "usager.cadre_de_vie.aidant_regulier": "none",
  "usager.cadre_de_vie.etat_logement": null,
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 70,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 0,
    "aidant_regulier": 0,
    "medecin_traitant": 0,
    "malveillance": 100,
    "urgence": 90,
    "hospitalisation": 80,
    "motif": 70,
    "etat_logement": 0
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
    },
    {
      "code": "isolement_social",
      "justification": "elle vit seule  Toulon dans son appartement",
      "confiance": 70
    },
    {
      "code": "lourdeur_reseau",
      "justification": "sa fille est puise et trs inquite",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "troubles_cognitifs": 95,
    "perte_autonomie_recente": 95,
    "isolement_social": 70,
    "lourdeur_reseau": 95
  },
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": true,
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
  "evaluation.comid.lourdeur_reseau": true,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 4 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION ---

[ DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social) ] - Priorite : 72
Objectif : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
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
La situation clinique dcrite montre une personne ge de 83 ans, atteinte de la maladie de Parkinson depuis 5 ans. Elle ncessite un hbergement temporaire pour que son conjoint puisse se faire oprer du dos. La situation est critique car le conjoint est au bout du rouleau et craint pour sa propre sant.
Ville extraite : Toulon
Mdecin : identifie
Malveillance : aucune
Hospitalisation : aucun
tat Logement : propre
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": null,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "oui",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.confiance.variables": {
    "age": 0,
    "ville": 100,
    "apa": 100,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 40,
    "aidant_regulier": 40,
    "medecin_traitant": 90,
    "malveillance": 80,
    "urgence": 60,
    "hospitalisation": 50,
    "motif": 70,
    "etat_logement": 80
  },
  "evaluation.comid.justifications": [
    {
      "code": "multimorbidite",
      "justification": "la maladie de Parkinson",
      "confiance": 95
    },
    {
      "code": "douleurs",
      "justification": "des malaises",
      "confiance": 95
    },
    {
      "code": "epuisement_aidant",
      "justification": "je suis au bout du rouleau",
      "confiance": 90
    },
    {
      "code": "logement_inadapte",
      "justification": "on habite  Toulon au 3me tage sans ascenseur",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "je ne dors plus car elle crie la nuit",
      "confiance": 90
    },
    {
      "code": "anxiete",
      "justification": "je sens que je fatigue",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "multimorbidite": 95,
    "douleurs": 95,
    "epuisement_aidant": 90,
    "logement_inadapte": 95,
    "isolement_social": 90,
    "anxiete": 95
  },
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": true,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": true,
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
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 6 (Situation  risque de complexit)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- REPONSE D'ORIA POUR L'AIDANT ---
voici votre priorit :'

VOTRE PRIORIT ABSOLUE : [ PSCG SS APA - Ple Social de Solidarit et de Gestion (APA) ]
MISSION : [/!\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] Contacter votre rfrent APA au Conseil Dpartemental (PSCG SS APA) pour toute modification de plan d'aide ou besoin d'accompagnement social supplmentaire.
CONTACT : 04 83 95 79 51

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
L'usager est un homme de 52 ans rsidant  Toulon, bnficiaire de la PCH et en situation de handicap moteur. Il cherche des informations sur les logements adapts  son fauteuil roulant dans la commune et souhaiterait savoir s'il existe des prestataires spcialiss pour l'aide humaine le week-end.
Ville extraite : Toulon
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : propre
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 52,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "oui",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 100,
    "gir": 0,
    "professionnels_domicile": 40,
    "aidant_regulier": 40,
    "medecin_traitant": 0,
    "malveillance": 100,
    "urgence": 90,
    "hospitalisation": 80,
    "motif": 90,
    "etat_logement": 80
  },
  "evaluation.comid.justifications": [
    {
      "code": "logement_inadapte",
      "justification": "habite  Toulon et cherche des informations sur les logements adapts  son fauteuil roulant",
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

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 102
Objectif : Motifs d'orientation combins :
  - [Centre Local d'Information et de Coordination (Snior)] (Confiance : 72%) : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
    -> Justification confiance : variable 'apa' extraite avec certitude de 0%, variable 'age' extraite avec certitude de 100%, variable 'motif' extraite avec certitude de 90%
  - [Centre Local d'Information et de Coordination (Exception PCH)] (Confiance : 95%) : Maintien  domicile : Accompagnement spcialis PCH (Prestation de Compensation du Handicap) pour les moins de 60 ans.
    -> Justification confiance : variable 'pch' extraite avec certitude de 100%, variable 'motif' extraite avec certitude de 90%
Contact : 04 94 24 65 25 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Morel (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Morel (Hpital) ---

1. Extraction IA pour : 'Mme Morel, 80 ans, est actuellement hospitalise ...'

--- DEBUG : ANALYSE EXPERTE ---
La patiente, ge de 80 ans, est hospitalise suite  une mauvaise chute et s'inquite pour son retour  domicile car elle vit seule au 3me tage. Elle a besoin d'aide pour organiser sa sortie et remplir ses dossiers administratifs.
Ville extraite : None
Mdecin : identifie
Malveillance : aucune
Hospitalisation : en_cours
tat Logement : propre
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 80,
  "usager.localisation.commune_residence": null,
  "usager.situation_actuelle.APA": "inconnu",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "en_cours",
  "demande.motif_principal": "sortie_hospitalisation",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 0,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 90,
    "aidant_regulier": 30,
    "medecin_traitant": 80,
    "malveillance": 100,
    "urgence": 60,
    "hospitalisation": 100,
    "motif": 90,
    "etat_logement": 70
  },
  "evaluation.comid.justifications": [
    {
      "code": "isolement_social",
      "justification": "elle vit seule",
      "confiance": 95
    },
    {
      "code": "logement_inadapte",
      "justification": "elle vit au 3me tage",
      "confiance": 95
    },
    {
      "code": "perte_autonomie_recente",
      "justification": "a fait une mauvaise chute",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "isolement_social": 95,
    "logement_inadapte": 95,
    "perte_autonomie_recente": 95
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
Score Total : 3 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION (Hopital Sainte Musse) ---

[ Service Social de l'Hpital (Hospitalisation en cours) ] - Priorite : 95
Objectif : Accompagnement social en milieu hospitalier : Organisation de la sortie et lien direct avec le service social de l'tablissement.
Contact : Non trouve dans le referentiel territorial

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Pierre (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Antoinette (Nouveau Cas Complexe) ---

1. Extraction IA (Dterministe, Temp=0.0) pour : 'M. Pierre age de 88 ans vis seul  domicile polypathologie avais oubli ma visi...'

--- DEBUG : ANALYSE EXPERTE ---
Monsieur P. est un homme de 88 ans qui vit seul  domicile et a une polypathologie. Il a oubli sa visite et son rfrigrateur ne fonctionne plus. Il bnficie d'un mdecin traitant mais pas de visite  domicile. Il a besoin d'aide pour faire ses courses.
Ville extraite : Toulon
Mdecin : identifie
Malveillance : aucune
Hospitalisation : aucun
tat Logement : propre
--- FIN DEBUG ---

Donnes extraites (JSON) :
{
  "usager.identite.age_estime": 88,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 40,
    "aidant_regulier": 40,
    "medecin_traitant": 100,
    "malveillance": 100,
    "urgence": 90,
    "hospitalisation": 80,
    "motif": 90,
    "etat_logement": 70
  },
  "evaluation.comid.justifications": [
    {
      "code": "addiction",
      "justification": "addition  l'alcool",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "vit seul  domicile",
      "confiance": 95
    },
    {
      "code": "logement_inadapte",
      "justification": "refrigerateur ne fonctionne plus",
      "confiance": 95
    },
    {
      "code": "perte_autonomie_recente",
      "justification": "difficult  la marche",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "addiction": 100,
    "isolement_social": 95,
    "logement_inadapte": 95,
    "perte_autonomie_recente": 95,
    "multimorbidite": 100
  },
  "evaluation.comid.multimorbidite": true,
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
  "evaluation.comid.addiction": true,
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
Score Total : 5 (Situation non complexe)

3. valuation de l'orientation...

4. Recherche des contacts territoriaux (La Garde)...

--- RSULTATS DE L'ORIENTATION POUR MME ANTOINETTE ---

[ CLIC - Centre Local d'Information et de Coordination (Snior) ] - Priorit : 80
Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
Contact : 04 22 44 84 73 | None

[ DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social) ] - Priorit : 72
Objectif : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
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
La situation clinique concerne une personne ge de 88 ans, isole et victime de violences physiques.
Ville extraite : La Seyne-sur-Mer
Mdecin : incertain
Malveillance : violences_physiques
Hospitalisation : aucun
tat Logement : propre
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 88,
  "usager.localisation.commune_residence": "La Seyne-sur-Mer",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "violences_physiques",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
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
    "urgence": 50,
    "hospitalisation": 0,
    "motif": 90,
    "etat_logement": 80
  },
  "evaluation.comid.justifications": [
    {
      "code": "isolement_social",
      "justification": "Mme B. est trs isole",
      "confiance": 95
    },
    {
      "code": "precarite_financiere",
      "justification": "son compte est vide et elle n'a plus de quoi s'acheter  manger",
      "confiance": 95
    },
    {
      "code": "agressivite",
      "justification": "le petit-fils de Mme B. semble lui voler de l'argent",
      "confiance": 95
    },
    {
      "code": "anxiete",
      "justification": "elle est trs angoisse  l'ide de parler",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "isolement_social": 95,
    "precarite_financiere": 95,
    "agressivite": 95,
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
  "evaluation.comid.logement_inadapte": false,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": true,
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
Score Total : 5 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux...
Ville extraite par l'IA : La Seyne-sur-Mer

--- RESULTATS DE L'ORIENTATION (Territoire: La Seyne-sur-mer) ---

[ CEV - Cellule coute et Vigilance (Violences Physiques & Danger Immdiat) ] - Priorite : 107
Objectif : Mise en scurit immdiate et protection d'urgence des majeurs vulnrables en situation de violence physique active ou menace.
Contact : 04 83 95 16 01 | None

[ DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social) ] - Priorite : 72
Objectif : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
Contact : 04 94 35 32 01 | None

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorite : 70
Objectif : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
Contact : 04 83 95 48 30 ou 04 83 95 37 99 | rue Charles Gide 83500 La Seyne sur mer

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Dubois (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Dubois ---

1. Extraction IA pour : 'M. Dubois, 74 ans, vit  Toulon. Il souffre de dia...'

--- DEBUG : ANALYSE EXPERTE ---
M. D., 74 ans, souffre de diabte, d'hypertension et d'une insuffisance rnale chronique qui lui cause des douleurs permanentes dans les jambes. Il prend 8 mdicaments par jour. Il commence  avoir du mal  payer son loyer et ses factures. Son appartement est au 4me tage sans ascenseur, ce qui est devenu un calvaire depuis son opration du genou. Il est trs anxieux pour sa sant et appelle le cabinet infirmier plusieurs fois par jour pour demander s'il a bien pris ses cachets.
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
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 70,
    "aidant_regulier": 0,
    "medecin_traitant": 100,
    "malveillance": 90,
    "urgence": 60,
    "hospitalisation": 40,
    "motif": 80,
    "etat_logement": 70
  },
  "evaluation.comid.justifications": [
    {
      "code": "multimorbidite",
      "justification": "Il souffre de diabte, d'hypertension et d'une insuffisance rnale chronique",
      "confiance": 95
    },
    {
      "code": "douleurs",
      "justification": "Il souffre en permanence dans les jambes",
      "confiance": 95
    },
    {
      "code": "polymedication",
      "justification": "Il prend 8 mdicaments par jour",
      "confiance": 95
    },
    {
      "code": "precarite_financiere",
      "justification": "Il commence  avoir du mal  payer son loyer et ses factures",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "Il vit seul",
      "confiance": 70
    },
    {
      "code": "logement_inadapte",
      "justification": "Son appartement est au 4me tage sans ascenseur",
      "confiance": 95
    },
    {
      "code": "anxiete",
      "justification": "Il est trs anxieux pour sa sant",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "multimorbidite": 95,
    "douleurs": 95,
    "polymedication": 95,
    "precarite_financiere": 95,
    "isolement_social": 70,
    "logement_inadapte": 95,
    "anxiete": 95
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
Score Total : 7 (Situation  risque de complexit)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION ---

[ DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social) ] - Priorite : 72
Objectif : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
Contact : 04 94 35 32 01 | None

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorite : 70
Objectif : [/!\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
Contact : 04 83 95 24 42 | 100, traverse des minimes 83000 Toulon

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Mouton (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Georgette Mouton (Ollioules) ---

1. Extraction IA pour : 'Mme Georgette Mouton, 83 ans, vit seule  Ollioules dans un appartement devenu e...'

--- DEBUG : ANALYSE EXPERTE ---
Analyse manquante
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
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "diogene",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 100,
    "aidant_regulier": 100,
    "medecin_traitant": 70,
    "malveillance": 100,
    "urgence": 40,
    "hospitalisation": 0,
    "motif": 90,
    "etat_logement": 100
  },
  "evaluation.comid.justifications": [
    {
      "code": "isolement_social",
      "justification": "Elle est en situation de grand isolement social",
      "confiance": 95
    },
    {
      "code": "logement_inadapte",
      "justification": "Appartement devenu extrmement insalubre et encombr de dchets et d'objets accumuls (syndrome de Diogne)",
      "confiance": 95
    },
    {
      "code": "epuisement_aidant",
      "justification": "N'a aucun aidant  proximit",
      "confiance": 95
    },
    {
      "code": "troubles_cognitifs",
      "justification": "Oublis de mdicaments frquents",
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

[ DAC - Dispositif d'Appui  la Coordination ] - Priorit : 96
Objectif : Motifs d'orientation combins :
  - [Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)] (Confiance : 96%) : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
    -> Justification confiance : score complexit COMID estim  96% de certitude, score complexit COMID estim  96% de certitude
  - [Suspicion de Diogne ou incurie] (Confiance : 100%) : Insalubrit ou ngligence critique  domicile : Suspicion ou syndrome de Diogne/incurie avr ncessitant une coordination multidimensionnelle renforce par le DAC.
    -> Justification confiance : variable 'etat_logement' extraite avec certitude de 100%
Contact : 04 94 35 32 01 | None

[ UTS Littoral Sud Sainte Baume - OLLIOULES (Relais CLIC) ] - Priorit : 80
Objectif : La commune ne dispose pas de CLIC, se rapprocher de l'UTS. Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
Contact : 04 83 95 58 50 | Espace Pierre Puget 2 Place Marius Trotobas 83190 Ollioules

[ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ] - Priorit : 78
Objectif : Maintien  domicile renforc et intensif : Alternative  l'EHPAD pour les situations en perte d'autonomie importante ou complexit technique.
Contact : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chnes 83500 LA SEYNE SUR MER

[ CPTS - Communaut Professionnelle Territoriale de Sant ] - Priorit : 50
Objectif : Accs aux soins : Recherche de mdecin traitant (justifie par retraite/dmnagement) et dispositif MISAS pour viter le renoncement aux soins.
Contact : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

