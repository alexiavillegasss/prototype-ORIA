# 📋 Rapport d'Évaluation Clinique ORIA

Généré automatiquement le : `2026-06-11 14:50:24`  
Nombre de cas exécutés : **21**  
Taux de succès : **21/21**  
Temps d'exécution total : **278.56 secondes**  

## 📊 Tableau récapitulatif des Orientations

| Patient | Status | Score COMID | Orientation Principale | Temps d'exécution |
| :--- | :---: | :---: | :--- | :---: |
| **Mme Huguette** | ✅ SUCCESS | 6 | `DAC - Dispositif d'Appui  la Coordination` | 16.07s |
| **Mme Durand** | ✅ SUCCESS | 4 | `DAC - Dispositif d'Appui  la Coordination` | 12.02s |
| **Mr Vacek** | ✅ SUCCESS | 5 | `CEV - Cellule coute et Vigilance (Violences Physiques & Danger Immdiat)` | 13.97s |
| **Mr Lambert** | ✅ SUCCESS | 5 | `DAC - Dispositif d'Appui  la Coordination` | 15.90s |
| **Mme Petit** | ✅ SUCCESS | 2 | `CCAS - Secours d'Urgence (Alimentaire & Factures)` | 10.44s |
| **Mme Lefebvre** | ✅ SUCCESS | 6 | `DAC - Dispositif d'Appui  la Coordination` | 13.31s |
| **Mr Leroy** | ✅ SUCCESS | 5 | `DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)` | 14.39s |
| **Mme Rossi** | ✅ SUCCESS | 4 | `Police / Gendarmerie (Urgence Vitale & Intervention)` | 11.34s |
| **Mme Martin** | ✅ SUCCESS | 3 | `CLIC - Centre Local d'Information et de Coordination (Snior)` | 11.55s |
| **Mr Martin** | ✅ SUCCESS | 3 | `Informations insuffisantes pour orienter` | 12.14s |
| **Mme Fontaine** | ✅ SUCCESS | 6 | `DAC - Dispositif d'Appui  la Coordination` | 13.84s |
| **Mme Gautier** | ✅ SUCCESS | 10 | `DAC - Dispositif d'Appui  la Coordination` | 19.26s |
| **Mme Vial** | ✅ SUCCESS | 3 | `CPTS - Communaut Professionnelle Territoriale de Sant` | 12.05s |
| **Mme Michu** | ✅ SUCCESS | 4 | `DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)` | 11.50s |
| **Mr Petit** | ✅ SUCCESS | 6 | `PSCG SS APA - Ple Social de Solidarit et de Gestion (APA)` | 13.60s |
| **Mr Chen** | ✅ SUCCESS | 2 | `CLIC - Centre Local d'Information et de Coordination` | 12.26s |
| **Mme Morel** | ✅ SUCCESS | 3 | `Service Social de l'Hpital (Hospitalisation en cours)` | 11.76s |
| **Mr Pierre** | ✅ SUCCESS | 5 | `DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)` | 12.46s |
| **Mme Bernard** | ✅ SUCCESS | 5 | `CEV - Cellule coute et Vigilance (Violences Physiques & Danger Immdiat)` | 11.78s |
| **Mr Dubois** | ✅ SUCCESS | 7 | `DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)` | 15.90s |
| **Mme Mouton** | ✅ SUCCESS | 4 | `DAC - Dispositif d'Appui  la Coordination` | 13.02s |

---

## 📝 Détail des extractions et raisonnements

<details>
<summary>🔍 Cas Mme Huguette (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Huguette (Urgence Sociale / Protection) ---

1. Extraction IA (Temp=0.0) pour : 'Mme Huguette, 79 ans, vit seule dans un logement insalubre et humide  La Valett...'

--- DEBUG : ANALYSE EXPERTE ---
La situation est critique car Mme H. vit seule dans un logement insalubre et humide, sans l'APA et vivant sous le seuil de pauvret. Son neveu procdure des retraits d'argent massifs et rpts sans justification, laissant Mme H. sans ressources pour s'acheter  manger.
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
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "insalubre",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 70,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 90,
    "aidant_regulier": 30,
    "medecin_traitant": 0,
    "malveillance": 100,
    "urgence": 80,
    "hospitalisation": 50,
    "motif": 90,
    "etat_logement": 70
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
    "lourdeur_reseau": 100,
    "opposition_soins": 0
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
  "evaluation.comid.lourdeur_reseau": true,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 6 (Situation  risque de complexit)

3. valuation de l'orientation...

4. Recherche des contacts territoriaux (La Valette)...

--- RSULTATS DE L'ORIENTATION POUR MME HUGUETTE ---

[ DAC - Dispositif d'Appui  la Coordination ] - Priorit : 105 | Confiance : 50%
Justification confiance : score complexite COMID estime a 80% de certitude (Penalite de pseudo-complexite de -30% appliquee), score complexite COMID estime a 80% de certitude (Penalite de pseudo-complexite de -30% appliquee)
Objectif : Motifs d'orientation combins :
  - [Refus de soins ou d'aide (Priorit Absolue)] (Confiance : 45%) : Refus de soins ou opposition critique aux aides  domicile : Rupture critique de parcours ncessitant l'intervention immdiate du DAC pour dbloquer la situation.
    -> Justification confiance : variable 'motif' extraite avec certitude de 90%, critre COMID 'opposition_soins' dtect avec certitude de 0%
  - [Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)] (Confiance : 50%) : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
    -> Justification confiance : score complexite COMID estime a 80% de certitude (Penalite de pseudo-complexite de -30% appliquee), score complexite COMID estime a 80% de certitude (Penalite de pseudo-complexite de -30% appliquee)
Contact : 04 94 35 32 01 | None

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorit : 70 | Confiance : 41%
Justification confiance : variable 'motif' extraite avec certitude de 90%, critre COMID 'precarite_financiere' dtect avec certitude de 95%, donne 'vulnerabilites.social.precarite' manquante (Pnalit de compltude applique de -20% pour 1 variable(s) manquante(s))
Objectif : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
Contact : 04 83 95 56 90 | 427 Avenue Duchatel 83130 La Valette du Var

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Durand (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Durand ---

1. Extraction IA pour : 'Mme Durand, 88 ans, vit  Hyres. Elle est trs co...'

--- DEBUG : ANALYSE EXPERTE ---
La situation clinique est critique car Mme D. est trs confuse et agressive avec les infirmiers qui viennent pour son diabte, ce qui rend difficile la prise en charge de sa sant.
Ville extraite : Hyres
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : non_renseigne
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": null,
  "usager.localisation.commune_residence": "Hyres",
  "usager.situation_actuelle.APA": "oui",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "eleve",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "inconnu",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
  "evaluation.confiance.variables": {
    "age": 0,
    "ville": 100,
    "apa": 100,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 30,
    "aidant_regulier": 0,
    "medecin_traitant": 0,
    "malveillance": 90,
    "urgence": 80,
    "hospitalisation": 70,
    "motif": 90,
    "etat_logement": 0
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
  - [Refus de soins ou d'aide (Priorit Absolue)] (Confiance : 92%) : Refus de soins ou opposition critique aux aides  domicile : Rupture critique de parcours ncessitant l'intervention immdiate du DAC pour dbloquer la situation.
    -> Justification confiance : critre COMID 'opposition_soins' dtect avec certitude de 95%, variable 'motif' extraite avec certitude de 90%
  - [Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)] (Confiance : 18%) : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
    -> Justification confiance : score complexite COMID estime a 88% de certitude (Penalite de situation non complexe de -70% appliquee), score complexite COMID estime a 88% de certitude (Penalite de situation non complexe de -70% appliquee)
Contact : Non trouve dans le referentiel territorial

[ PSCG SS APA - Ple Social de Solidarit et de Gestion (APA) ] - Priorite : 100
Objectif : [/!\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] Contacter votre rfrent APA au Conseil Dpartemental (PSCG SS APA) pour toute modification de plan d'aide ou besoin d'accompagnement social supplmentaire.
Contact : Non trouve dans le referentiel territorial

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Vacek (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Vacek (Habitat Indigne & Danger) ---

1. Extraction IA pour la situation de pril...

--- DEBUG : ANALYSE EXPERTE ---
M. V., 65 ans, vit dans un appartement insalubre  Toulon, sans eau courante depuis 3 mois et avec des problmes respiratoires srieux.
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
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "insalubre",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 70,
    "aidant_regulier": 0,
    "medecin_traitant": 0,
    "malveillance": 90,
    "urgence": 50,
    "hospitalisation": 0,
    "motif": 80,
    "etat_logement": 100
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
MISSION : [/!\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Lambert (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Lambert (Appel Infirmire) ---

1. Extraction IA pour le rcit de l'infirmire...

--- DEBUG : ANALYSE EXPERTE ---
Le patient est un homme de 78 ans qui vit  La Seyne. Il a des difficults pour se prendre en charge et son logement est dans un tat dplorable. Il refuse les soins mdicaux et il y a urgence pour intervenir.
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
    "professionnels_domicile": 70,
    "aidant_regulier": 30,
    "medecin_traitant": 0,
    "malveillance": 90,
    "urgence": 80,
    "hospitalisation": 50,
    "motif": 100,
    "etat_logement": 100
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

CONTACTER : [ DAC - Dispositif d'Appui  la Coordination ]
POURQUOI : Motifs d'orientation combins :
  - [Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)] (Confiance : 21%) : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
    -> Justification confiance : score complexite COMID estime a 91% de certitude (Penalite de situation non complexe de -70% appliquee), score complexite COMID estime a 91% de certitude (Penalite de situation non complexe de -70% appliquee)
  - [Suspicion de Diogne ou incurie] (Confiance : 100%) : Insalubrit ou ngligence critique  domicile : Suspicion ou syndrome de Diogne/incurie avr ncessitant une coordination multidimensionnelle renforce par le DAC.
    -> Justification confiance : variable 'etat_logement' extraite avec certitude de 100%
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
La personne ge de 78 ans, vivant seule  La Garde, est en situation financire prcaire et demande de l'aide pour s'acheter  manger.
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
    "professionnels_domicile": 70,
    "aidant_regulier": 0,
    "medecin_traitant": 100,
    "malveillance": 100,
    "urgence": 40,
    "hospitalisation": 0,
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

[ CCAS - Secours d'Urgence (Alimentaire & Factures) ] - Priorite : 85
Objectif : Secours financier ou alimentaire d'urgence de proximit : Attribution d'aides extra-lgales par la mairie.
Contact : 04 94 08 98 34 | 81 Rue Marius Tardivier 83130 La garde

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
La personne est suivie pour une bipolarit mais a arrt son traitement le mois dernier. Elle consomme beaucoup d'alcool et vit dans un appartement encombr avec des odeurs fortes.
Ville extraite : La Garde
Mdecin : absent
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
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "diogene",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 70,
    "aidant_regulier": 0,
    "medecin_traitant": 90,
    "malveillance": 80,
    "urgence": 60,
    "hospitalisation": 50,
    "motif": 90,
    "etat_logement": 100
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
    "anxiete": 95,
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
Score Total : 6 (Situation  risque de complexit)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (La Garde)...

--- RESULTATS DE L'ORIENTATION ---

[ DAC - Dispositif d'Appui  la Coordination ] - Priorite : 105
Objectif : Motifs d'orientation combins :
  - [Refus de soins ou d'aide (Priorit Absolue)] (Confiance : 45%) : Refus de soins ou opposition critique aux aides  domicile : Rupture critique de parcours ncessitant l'intervention immdiate du DAC pour dbloquer la situation.
    -> Justification confiance : variable 'motif' extraite avec certitude de 90%, critre COMID 'opposition_soins' dtect avec certitude de 0%
  - [Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)] (Confiance : 50%) : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
    -> Justification confiance : score complexite COMID estime a 80% de certitude (Penalite de pseudo-complexite de -30% appliquee), score complexite COMID estime a 80% de certitude (Penalite de pseudo-complexite de -30% appliquee)
  - [Suspicion de Diogne ou incurie] (Confiance : 100%) : Insalubrit ou ngligence critique  domicile : Suspicion ou syndrome de Diogne/incurie avr ncessitant une coordination multidimensionnelle renforce par le DAC.
    -> Justification confiance : variable 'etat_logement' extraite avec certitude de 100%
Contact : 04 94 35 32 01 | None

[ CPTS - Communaut Professionnelle Territoriale de Sant ] - Priorite : 50
Objectif : Accs aux soins : Recherche de mdecin traitant (justifie par retraite/dmnagement) et dispositif MISAS pour viter le renoncement aux soins.
Contact : 06 63 63 63 91 | 3 Rue Aspirant Franois Philippe 83260 La Crau

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Leroy (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Leroy (Moins de 60 ans) ---

1. Extraction IA pour : 'M. Leroy, 45 ans, habite  Toulon. Il est atteint ...'

--- DEBUG : ANALYSE EXPERTE ---
L'usager est un homme de 45 ans, atteint d'une Sclrose en Plaques (SEP) diagnostique il y a 2 ans. Il vit seul et ses revenus ont chut, ce qui rend difficile le paiement de son loyer. Il se sent perdu dans son parcours de soins entre les diffrents spcialistes et son moral est au plus bas.
Ville extraite : Toulon
Mdecin : identifie
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
    "malveillance": 100,
    "urgence": 40,
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
Objectif : [/!\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
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
La situation est critique car la patiente a d quitter son domicile en urgence en raison de violences physiques et verbales exerces par son mari.
Ville extraite : Toulon
Mdecin : incertain
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
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
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
    "medecin_traitant": 0,
    "malveillance": 90,
    "urgence": 100,
    "hospitalisation": 0,
    "motif": 80,
    "etat_logement": 60
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
Objectif : [/!\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
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
    "professionnels_domicile": 90,
    "aidant_regulier": 40,
    "medecin_traitant": 0,
    "malveillance": 80,
    "urgence": 50,
    "hospitalisation": 30,
    "motif": 70,
    "etat_logement": 90
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
      "justification": "Je ne dors plus, je pleure tout le temps au travail.",
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
Le patient est un homme de 75 ans qui vit  La Seyne-sur-Mer et a des problmes de vue. Il se retrouve seul aprs l'hospitalisation de sa femme, ce qui le rend incapable de prparer ses repas ni de prendre ses mdicaments.
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
    "malveillance": 90,
    "urgence": 20,
    "hospitalisation": 100,
    "motif": 80,
    "etat_logement": 60
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
La situation clinique est proccupante car la patiente perd du poids, oublie ses mdicaments et est victime de malveillance financire. Il est important d'intervenir pour protger la patiente.
Ville extraite : Sanary
Mdecin : identifie
Malveillance : spoliation_financiere
Hospitalisation : aucun
tat Logement : propre
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": null,
  "usager.localisation.commune_residence": "Sanary",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "spoliation_financiere",
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "oui",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.confiance.variables": {
    "age": 0,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 90,
    "aidant_regulier": 80,
    "medecin_traitant": 100,
    "malveillance": 100,
    "urgence": 70,
    "hospitalisation": 60,
    "motif": 90,
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
    "opposition_soins": 0,
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
  "evaluation.comid.lourdeur_reseau": true,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexit COMID...
Score Total : 6 (Situation  risque de complexit)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Sanary-sur-Mer)...

--- REPONSE D'ORIA POUR LE KINE ---
ORIA : 'Situation identifie comme Situation  risque de complexit. Voici les actions prioritaires :'

ACTION : [ DAC - Dispositif d'Appui  la Coordination ]
MOTIF : Motifs d'orientation combins :
  - [Refus de soins ou d'aide (Priorit Absolue)] (Confiance : 45%) : Refus de soins ou opposition critique aux aides  domicile : Rupture critique de parcours ncessitant l'intervention immdiate du DAC pour dbloquer la situation.
    -> Justification confiance : variable 'motif' extraite avec certitude de 90%, critre COMID 'opposition_soins' dtect avec certitude de 0%
  - [Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)] (Confiance : 50%) : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
    -> Justification confiance : score complexite COMID estime a 80% de certitude (Penalite de pseudo-complexite de -30% appliquee), score complexite COMID estime a 80% de certitude (Penalite de pseudo-complexite de -30% appliquee)
CONTACT : 04 94 35 32 01

ACTION : [ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ]
MOTIF : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
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
La situation clinique est caractrise par une grave dpression clinique avec des ides noires, un tat de sant instable et prcaire. La personne souffre de plusieurs pathologies chroniques et ncessite une aide rgulire.
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
  "usager.cadre_de_vie.aidant_regulier": "oui",
  "usager.cadre_de_vie.etat_logement": "insalubre",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 40,
    "aidant_regulier": 90,
    "medecin_traitant": 100,
    "malveillance": 70,
    "urgence": 60,
    "hospitalisation": 80,
    "motif": 90,
    "etat_logement": 80
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
  - [Refus de soins ou d'aide (Priorit Absolue)] (Confiance : 45%) : Refus de soins ou opposition critique aux aides  domicile : Rupture critique de parcours ncessitant l'intervention immdiate du DAC pour dbloquer la situation.
    -> Justification confiance : variable 'motif' extraite avec certitude de 90%, critre COMID 'opposition_soins' dtect avec certitude de 0%
  - [Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)] (Confiance : 86%) : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
    -> Justification confiance : score complexite COMID estime a 86% de certitude (Situation complexe), score complexite COMID estime a 86% de certitude (Situation complexe)
Contact : 04 94 35 32 01 | None

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorite : 70
Objectif : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
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
La personne, ge de 82 ans, souffre de diabte et d'hypertension. Elle a dmnag et n'a plus de mdecin traitant. Elle cherche un nouveau mdecin.
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
  "usager.cadre_de_vie.aidant_regulier": "oui",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 70,
    "aidant_regulier": 90,
    "medecin_traitant": 80,
    "malveillance": 100,
    "urgence": 60,
    "hospitalisation": 50,
    "motif": 90,
    "etat_logement": 80
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
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": null,
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 70,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 40,
    "aidant_regulier": 40,
    "medecin_traitant": 0,
    "malveillance": 90,
    "urgence": 60,
    "hospitalisation": 80,
    "motif": 100,
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
Objectif : [/!\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
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
La situation est critique pour la personne et son conjoint, qui ncessite un hbergement temporaire pour permettre l'opration du dos.
Ville extraite : Toulon
Mdecin : identifie
Malveillance : aucune
Hospitalisation : aucun
tat Logement : propre
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
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 100,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 70,
    "aidant_regulier": 70,
    "medecin_traitant": 100,
    "malveillance": 100,
    "urgence": 90,
    "hospitalisation": 80,
    "motif": 90,
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
MISSION : Contacter votre rfrent APA au Conseil Dpartemental (PSCG SS APA) pour toute modification de plan d'aide ou besoin d'accompagnement social supplmentaire.
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
L'usager, g de 52 ans, habite  Toulon et bnficie de la PCH. Il cherche des informations sur les logements adapts  son fauteuil roulant dans la commune et souhaiterait savoir s'il existe des prestataires spcialiss pour l'aide humaine le week-end.
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
    "malveillance": 90,
    "urgence": 60,
    "hospitalisation": 80,
    "motif": 100,
    "etat_logement": 90
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
  - [Centre Local d'Information et de Coordination (Snior)] (Confiance : 75%) : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
    -> Justification confiance : variable 'motif' extraite avec certitude de 100%, variable 'age' extraite avec certitude de 100%, variable 'apa' extraite avec certitude de 0%
  - [Centre Local d'Information et de Coordination (Exception PCH)] (Confiance : 100%) : Maintien  domicile : Accompagnement spcialis PCH (Prestation de Compensation du Handicap) pour les moins de 60 ans.
    -> Justification confiance : variable 'motif' extraite avec certitude de 100%, variable 'pch' extraite avec certitude de 100%
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
Mdecin : incertain
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
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "en_cours",
  "demande.motif_principal": "sortie_hospitalisation",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 0,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 90,
    "aidant_regulier": 80,
    "medecin_traitant": 0,
    "malveillance": 100,
    "urgence": 50,
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
Monsieur P., un homme de 88 ans, vit seul  domicile et a une polypathologie. Il a oubli sa visite prvue et son rfrigrateur ne fonctionne plus. Il bnficie d'un mdecin traitant qui ne fait pas de visites  domicile.
Ville extraite : Toulon
Mdecin : incertain
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
    "professionnels_domicile": 40,
    "aidant_regulier": 40,
    "medecin_traitant": 0,
    "malveillance": 90,
    "urgence": 80,
    "hospitalisation": 100,
    "motif": 70,
    "etat_logement": 90
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

[ DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social) ] - Priorit : 72
Objectif : [/!\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
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
    "malveillance": 90,
    "urgence": 50,
    "hospitalisation": 0,
    "motif": 80,
    "etat_logement": 60
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
Objectif : [/!\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
Contact : 04 94 35 32 01 | None

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorite : 70
Objectif : [/!\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
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
L'usager souffre de diabte, d'hypertension et d'une insuffisance rnale chronique qui lui cause des douleurs permanentes dans les jambes. Il prend 8 mdicaments par jour. Il est trs anxieux pour sa sant et appelle le cabinet infirmier plusieurs fois par jour pour demander s'il a bien pris ses cachets.
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
    "aidant_regulier": 40,
    "medecin_traitant": 90,
    "malveillance": 80,
    "urgence": 60,
    "hospitalisation": 50,
    "motif": 80,
    "etat_logement": 90
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
La situation clinique est marque par un grand isolement social, une rsidence insalubre et encombre, ainsi qu'un risque majeur de chute et d'oubli de mdicaments.
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
    "professionnels_domicile": 0,
    "aidant_regulier": 0,
    "medecin_traitant": 70,
    "malveillance": 90,
    "urgence": 50,
    "hospitalisation": 0,
    "motif": 80,
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
  - [Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social)] (Confiance : 26%) : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
    -> Justification confiance : score complexite COMID estime a 96% de certitude (Penalite de situation non complexe de -70% appliquee), score complexite COMID estime a 96% de certitude (Penalite de situation non complexe de -70% appliquee)
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

