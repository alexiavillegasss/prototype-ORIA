# 📋 Rapport d'Évaluation Clinique ORIA

Généré automatiquement le : `2026-07-02 12:54:31`  
Nombre de cas exécutés : **21**  
Taux de succès : **21/21**  
Temps d'exécution total : **4461.93 secondes**  

## 📊 Tableau récapitulatif des Orientations

| Patient | Status | Score COMID | Orientation Principale | Temps d'exécution |
| :--- | :---: | :---: | :--- | :---: |
| **Mme Durand** | ✅ SUCCESS | 4 | `DAC - Orientation complexe (APA + Problmatique de Sant)` | 132.33s |
| **Mme Huguette** | ✅ SUCCESS | 7 | `CLIC - Centre Local d'Information et de Coordination (Snior)` | 169.13s |
| **Mr Vacek** | ✅ SUCCESS | 5 | `Police / Gendarmerie (Urgence Vitale & Intervention)` | 162.81s |
| **Mr Lambert** | ✅ SUCCESS | 6 | `CLIC - Centre Local d'Information et de Coordination (Snior)` | 173.73s |
| **Mme Petit** | ✅ SUCCESS | 2 | `CCAS - Secours d'Urgence (Alimentaire & Factures)` | 128.06s |
| **Mme Lefebvre** | ✅ SUCCESS | 6 | `Les Compagnons Btisseurs (Diogne ou Incurie unique/principale)` | 151.66s |
| **Mr Leroy** | ✅ SUCCESS | 5 | `CLIC - Centre Local d'Information et de Coordination (Snior)` | 160.00s |
| **Mme Rossi** | ✅ SUCCESS | 5 | `Les Compagnons Btisseurs (Diogne ou Incurie unique/principale)` | 139.30s |
| **Mme Martin** | ✅ SUCCESS | 4 | `CLIC - Centre Local d'Information et de Coordination (Snior)` | 159.34s |
| **Mr Martin** | ✅ SUCCESS | 3 | `CLIC - Centre Local d'Information et de Coordination (Snior)` | 145.67s |
| **Mme Fontaine** | ✅ SUCCESS | 4 | `CEV - Cellule coute et Vigilance (Spoliation & Autres Dangers)` | 152.63s |
| **Mme Gautier** | ✅ SUCCESS | 10 | `CLIC - Centre Local d'Information et de Coordination (Snior)` | 200.04s |
| **Mme Vial** | ✅ SUCCESS | 3 | `CPTS - Communaut Professionnelle Territoriale de Sant` | 181.80s |
| **Mme Michu** | ✅ SUCCESS | 3 | `CLIC - Centre Local d'Information et de Coordination (Snior)` | 159.14s |
| **Mr Petit** | ✅ SUCCESS | 6 | `DAC - Orientation complexe (APA + Problmatique de Sant)` | 197.34s |
| **Mr Chen** | ✅ SUCCESS | 2 | `CLIC - Centre Local d'Information et de Coordination` | 171.38s |
| **Mme Morel** | ✅ SUCCESS | 3 | `Service Social de l'Hpital (Hospitalisation en cours)` | 171.10s |
| **Mr Pierre** | ✅ SUCCESS | 2 | `CLIC - Centre Local d'Information et de Coordination (Snior)` | 169.61s |
| **Mme Bernard** | ✅ SUCCESS | 5 | `CEV - Cellule coute et Vigilance (Violences Physiques & Danger Immdiat)` | 179.81s |
| **Mr Dubois** | ✅ SUCCESS | 7 | `CLIC - Centre Local d'Information et de Coordination (Snior)` | 205.81s |
| **Mme Mouton** | ✅ SUCCESS | 5 | `UTS Littoral Sud Sainte Baume - OLLIOULES (Relais CLIC)` | 1151.24s |

---

## 📝 Détail des extractions et raisonnements

<details>
<summary>🔍 Cas Mme Durand (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Durand ---

1. Extraction IA pour : 'Mme Durand, 88 ans, vit  Hyres. Elle est trs co...'

--- DEBUG : ANALYSE EXPERTE ---
La situation est critique car Mme D. refuse les soins mdicaux et dambule la nuit, ce qui pose un risque pour sa scurit.
Ville extraite : Hyres
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : non_renseigne
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
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "none",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
  "demande.proposition_mail": "Bonjour, nous avons signal une situation de refus de soins chez Mme D., 88 ans, rsidente  Hyres. Elle est confuse et agressive avec les infirmiers. Nous demandons votre aide pour trouver une solution.",
  "demande.resume_structur": "La situation est critique car Mme D. refuse les soins mdicaux et dambule la nuit, ce qui pose un risque pour sa scurit.",
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
    "hospitalisation": 100,
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
      "code": "isolement_social",
      "justification": "elle vit  Hyres",
      "confiance": 70
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
    }
  ],
  "evaluation.confiance.comid": {
    "troubles_cognitifs": 95,
    "isolement_social": 70,
    "agressivite": 95,
    "opposition_soins": 95
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

[ DAC - Orientation complexe (APA + Problmatique de Sant) ] - Priorite : 105
Objectif : Patient bnficiant dj de l'APA mais prsentant une problmatique de sant/dgradation clinique : Ncessite une coordination intensive par le DAC pour rvaluer et scuriser le maintien  domicile.
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
  "demande.proposition_mail": "Bonjour, nous sommes proccups par la situation de Mme H., 79 ans, qui vit seule dans un logement insalubre et humide  La Valette du Var. Son neveu procdure des retraits d'argent massifs et rpts sans justification, laissant Mme H. sans ressources pour s'acheter  manger. Nous demandons votre aide pour valuer cette situation et proposer une solution.",
  "demande.resume_structur": "La situation est critique car Mme H. vit seule dans un logement insalubre et humide, sans l'APA et vivant sous le seuil de pauvret. Son neveu procdure des retraits d'argent massifs et rpts sans justification, laissant Mme H. sans ressources pour s'acheter  manger.",
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
    "hospitalisation": 10,
    "motif": 70,
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
      "code": "anxiete",
      "justification": "Huguette est terrifie par son neveu et n'ose rien dire par peur de reprsailles.",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "isolement_social": 95,
    "precarite_financiere": 95,
    "logement_inadapte": 100,
    "conflit_reseau": 95,
    "anxiete": 95,
    "opposition_soins": 0,
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
Score Total : 7 (Situation  risque de complexit)

3. valuation de l'orientation...

4. Recherche des contacts territoriaux (La Valette)...

--- RSULTATS DE L'ORIENTATION POUR MME HUGUETTE ---

[ CLIC - Centre Local d'Information et de Coordination (Snior) ] - Priorit : 80 | Confiance : 67%
Justification confiance : variable 'age' extraite avec certitude de 100%, variable 'apa' extraite avec certitude de 0%, variable 'motif' extraite avec certitude de 70%
Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
Contact : 04 22 44 84 73 | None

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorit : 70 | Confiance : 35%
Justification confiance : critre COMID 'precarite_financiere' dtect avec certitude de 95%, donne 'vulnerabilites.social.precarite' manquante, variable 'motif' extraite avec certitude de 70% (Pnalit de compltude applique de -20% pour 1 variable(s) manquante(s))
Objectif : [/!\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
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
M. V., 65 ans, vit dans un appartement insalubre  Toulon. Il n'a plus d'eau courante depuis 3 mois et le plafond de sa chambre menace de s'effondrer suite  une infiltration. Il est terrifi et a des problmes respiratoires srieux.
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
  "adresseur.degre_urgence_percu": "critique",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "secours_urgence",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "insalubre",
  "demande.proposition_mail": "Bonjour, nous sommes proccups par la situation de M. V., 65 ans, qui vit dans un appartement insalubre  Toulon. Il n'a plus d'eau courante depuis 3 mois et le plafond de sa chambre menace de s'effondrer. Nous demandons votre aide pour valuer les besoins de M. V. et proposer des solutions.",
  "demande.resume_structur": "M. V., 65 ans, vit dans un appartement insalubre  Toulon. Il n'a plus d'eau courante depuis 3 mois et le plafond de sa chambre menace de s'effondrer suite  une infiltration. Il est terrifi et a des problmes respiratoires srieux.",
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

VOTRE PRIORIT ABSOLUE : [ Police / Gendarmerie (Urgence Vitale & Intervention) ]
MISSION : Intervention immdiate des forces de l'ordre en cas d'agression physique active et en cours ou danger vital imminent.
CONTACT : N/A

ENSUITE (VOLET SOCIAL) : [ CEV - Cellule coute et Vigilance (Violences Physiques & Danger Immdiat) ]
MISSION : Mise en scurit immdiate et protection d'urgence des majeurs vulnrables en situation de violence physique active ou menace.

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Lambert (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Lambert (Appel Infirmire) ---

1. Extraction IA pour le rcit de l'infirmire...

--- DEBUG : ANALYSE EXPERTE ---
Le patient, un homme de 78 ans, est en situation de crise. Il refuse les soins et les mdicaments, ce qui peut tre li  une dcompensation psy ou un dbut d'Alzheimer. Il est isol et son appartement est dans un tat dsastreux.
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
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "diogene",
  "demande.proposition_mail": "Bonjour, je vous appelle pour signaler la situation critique de mon patient, M. L., g de 78 ans. Il refuse les soins et les mdicaments, et son appartement est dans un tat dsastreux. Je suis perdue quant  savoir qui appeler : le mdecin, les services sociaux ou la mairie. Aide-moi.",
  "demande.resume_structur": "Le patient, un homme de 78 ans, est en situation de crise. Il refuse les soins et les mdicaments, ce qui peut tre li  une dcompensation psy ou un dbut d'Alzheimer. Il est isol et son appartement est dans un tat dsastreux.",
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
    "motif": 90,
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
    "inquietude_sante": 70,
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
Score Total : 6 (Situation  risque de complexit)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (La Seyne-sur-Mer)...

--- REPONSE D'ORIA POUR L'INFIRMIERE ---
ORIA : 'D'aprs votre description, la situation de M. Lambert est Situation  risque de complexit. Voici les priorits d'appel :'

CONTACTER : [ CLIC - Centre Local d'Information et de Coordination (Snior) ]
POURQUOI : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
CONTACT : 04 94 06 97 04 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Petit (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Petit (Urgence CCAS) ---

1. Extraction IA pour : 'Mme Petit, 78 ans, habite  La Garde. Elle vit seu...'

--- DEBUG : ANALYSE EXPERTE ---
La patiente, ge de 78 ans, vit seule  La Garde et a une petite retraite. Elle est en difficult financire et demande de l'aide pour s'acheter  manger.
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
  "demande.proposition_mail": "Bonjour, nous avons signal la situation suivante : Mme P., ge de 78 ans, vit seule  La Garde et a une petite retraite. Elle est en difficult financire et demande de l'aide pour s'acheter  manger. Nous sommes  votre disposition.",
  "demande.resume_structur": "La patiente, ge de 78 ans, vit seule  La Garde et a une petite retraite. Elle est en difficult financire et demande de l'aide pour s'acheter  manger.",
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
    "urgence": 30,
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
La patiente, 65 ans, vit  La Garde et a arrt son traitement pour sa bipolarit. Elle consomme beaucoup d'alcool pour 'calmer ses angoisses' et vit dans un appartement trs encombr (Syndrome de Diogne suspect). Ses voisins se plaignent d'odeurs fortes.
Ville extraite : La Garde
Mdecin : incertain
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
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "diogene",
  "demande.proposition_mail": "Bonjour, nous sommes proccups par la situation de Mme L., 65 ans, qui a arrt son traitement pour sa bipolarit et vit dans un appartement trs encombr. Elle consomme beaucoup d'alcool et ses voisins se plaignent d'odeurs fortes. Nous demandons votre aide pour l'aider  trouver une solution.",
  "demande.resume_structur": "La patiente, 65 ans, vit  La Garde et a arrt son traitement pour sa bipolarit. Elle consomme beaucoup d'alcool pour 'calmer ses angoisses' et vit dans un appartement trs encombr (Syndrome de Diogne suspect). Ses voisins se plaignent d'odeurs fortes.",
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
      "justification": "appartement trs encombr (Syndrome de Diogne suspect)",
      "confiance": 95
    },
    {
      "code": "anxiete",
      "justification": "trs angoisse",
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

[ Les Compagnons Btisseurs (Diogne ou Incurie unique/principale) ] - Priorite : 90
Objectif : [/!\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] Accompagnement auto-rhabilitation et nettoyage/amnagement du logement pour syndrome de Diogne ou incurie sans complexit sanitaire ou sociale majeure.
Contact : Non trouve dans le referentiel territorial

[ CLIC - Centre Local d'Information et de Coordination (Snior) ] - Priorite : 80
Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
Contact : 04 22 44 84 73 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Leroy (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Leroy (Moins de 60 ans) ---

1. Extraction IA pour : 'M. Leroy, 45 ans, habite  Toulon. Il est atteint ...'

--- DEBUG : ANALYSE EXPERTE ---
L'usager est un homme de 45 ans, atteint d'une Sclrose en Plaques (SEP) diagnostique il y a 2 ans. Sa sant se dgrade rapidement et il a d arrter son activit professionnelle. Il vit seul, ses revenus ont chut et il a du mal  payer son loyer. Il se sent perdu dans son parcours de soins entre les diffrents spcialistes et son moral est au plus bas, il exprime des ides noires.
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
  "demande.proposition_mail": "Bonjour, je vous cris pour signaler la situation critique de M. L., atteint d'une Sclrose en Plaques (SEP) diagnostique il y a 2 ans. Sa sant se dgrade rapidement et il a du mal  payer son loyer. Il vit seul et se sent perdu dans son parcours de soins. Je vous prie de prendre en compte sa situation.",
  "demande.resume_structur": "L'usager est un homme de 45 ans, atteint d'une Sclrose en Plaques (SEP) diagnostique il y a 2 ans. Sa sant se dgrade rapidement et il a d arrter son activit professionnelle. Il vit seul, ses revenus ont chut et il a du mal  payer son loyer. Il se sent perdu dans son parcours de soins entre les diffrents spcialistes et son moral est au plus bas, il exprime des ides noires.",
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

[ CLIC - Centre Local d'Information et de Coordination (Snior) ] - Priorite : 80
Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
Contact : 04 94 24 65 25 | None

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
La situation est critique car la personne a d quitter son domicile en urgence en raison de violences physiques et verbales exerces par son mari. Elle a besoin d'une protection immdiate et d'un hbergement d'urgence.
Ville extraite : Toulon
Mdecin : incertain
Malveillance : violences_physiques
Hospitalisation : aucun
tat Logement : diogene
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
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "diogene",
  "demande.proposition_mail": "Bonjour, nous avons une situation urgente  Toulon. Madame R., 70 ans, a quitt son domicile en urgence en raison de violences physiques et verbales exerces par son mari. Elle a besoin d'une protection immdiate et d'un hbergement d'urgence.",
  "demande.resume_structur": "La situation est critique car la personne a d quitter son domicile en urgence en raison de violences physiques et verbales exerces par son mari. Elle a besoin d'une protection immdiate et d'un hbergement d'urgence.",
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
    "logement_inadapte": 100,
    "depression": 95,
    "opposition_soins": 0,
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
Score Total : 5 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION (Protection / Violences) ---

[ Les Compagnons Btisseurs (Diogne ou Incurie unique/principale) ] - Priorite : 90
Objectif : [/!\ INFORMATIONS INSUFFISANTES : Il est vivement conseille de recueillir plus de precisions sur la situation du patient pour fiabiliser cette orientation] Accompagnement auto-rhabilitation et nettoyage/amnagement du logement pour syndrome de Diogne ou incurie sans complexit sanitaire ou sociale majeure.
Contact : Non trouve dans le referentiel territorial

[ CLIC - Centre Local d'Information et de Coordination (Snior) ] - Priorite : 80
Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
Contact : 04 94 24 65 25 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Martin (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Martin (Dtresse Aidant) ---

1. Extraction IA pour le rcit de l'aidante...

--- DEBUG : ANALYSE EXPERTE ---
La fille de Mme M. (82 ans) est  bout, travaillant  temps plein et passant toutes ses soires et week-ends chez sa mre qui perd la tte, laisse le gaz allum, se relve la nuit et a dj tombe deux fois. La fille craque et a peur de devenir mchante avec sa mre.
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
  "demande.proposition_mail": "Bonjour, nous sommes proccups par la situation de Mme M. (82 ans) qui perd la tte, laisse le gaz allum, se relve la nuit et a dj tombe deux fois. Nous demandons votre aide pour trouver des solutions pour qu'elle soit en scurit et que sa fille puisse enfin souffler un peu.",
  "demande.resume_structur": "La fille de Mme M. (82 ans) est  bout, travaillant  temps plein et passant toutes ses soires et week-ends chez sa mre qui perd la tte, laisse le gaz allum, se relve la nuit et a dj tombe deux fois. La fille craque et a peur de devenir mchante avec sa mre.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 70,
    "aidant_regulier": 40,
    "medecin_traitant": 0,
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
      "code": "logement_inadapte",
      "justification": "On n'a aucune aide  part l'infirmire le matin.",
      "confiance": 70
    },
    {
      "code": "anxiete",
      "justification": "Je pleure tout le temps au travail.",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "epuisement_aidant": 95,
    "isolement_social": 95,
    "logement_inadapte": 70,
    "anxiete": 95
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
Score Total : 4 (Situation non complexe)

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
L'usager est un homme de 75 ans, vivant  La Seyne-sur-Mer. Il a des problmes de vue graves et sa femme, qui s'occupait de tout, vient d'tre hospitalise. Il se retrouve seul et n'arrive plus  prparer ses repas ni  prendre ses mdicaments.
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
  "demande.proposition_mail": "Bonjour, nous avons un usager g de 75 ans vivant  La Seyne-sur-Mer qui a des problmes de vue graves et est isol depuis l'hospitalisation de sa femme. Il a besoin d'aide pour prparer ses repas et prendre ses mdicaments.",
  "demande.resume_structur": "L'usager est un homme de 75 ans, vivant  La Seyne-sur-Mer. Il a des problmes de vue graves et sa femme, qui s'occupait de tout, vient d'tre hospitalise. Il se retrouve seul et n'arrive plus  prparer ses repas ni  prendre ses mdicaments.",
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
    "hospitalisation": 90,
    "motif": 80,
    "etat_logement": 90
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

[ CLIC - Centre Local d'Information et de Coordination (Snior) ] - Priorite : 80
Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
Contact : 04 94 06 97 04 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Fontaine (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Fontaine (Alerte Kin) ---

1. Extraction IA pour l'alerte du kin...

--- DEBUG : ANALYSE EXPERTE ---
La patiente de 85 ans, rsidente  Sanary, est en situation critique. Elle a perdu 5 kg en un mois et oublie ses mdicaments contre la douleur. Son frigo est vide et elle est terrorise par son fils qui lui demande de l'argent de faon insistante.
Ville extraite : Sanary
Mdecin : identifie
Malveillance : spoliation_financiere
Hospitalisation : aucun
tat Logement : insalubre
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
  "usager.cadre_de_vie.etat_logement": "insalubre",
  "demande.proposition_mail": "Bonjour, nous sommes proccups par la situation de Mme F., 85 ans, rsidente  Sanary. Elle a perdu 5 kg en un mois et oublie ses mdicaments contre la douleur. Son frigo est vide et elle est terrorise par son fils qui lui demande de l'argent de faon insistante. Nous demandons votre aide pour valuer sa situation et trouver une solution.",
  "demande.resume_structur": "La patiente de 85 ans, rsidente  Sanary, est en situation critique. Elle a perdu 5 kg en un mois et oublie ses mdicaments contre la douleur. Son frigo est vide et elle est terrorise par son fils qui lui demande de l'argent de faon insistante.",
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
    "urgence": 80,
    "hospitalisation": 0,
    "motif": 90,
    "etat_logement": 60
  },
  "evaluation.comid.justifications": [
    {
      "code": "precarite_financiere",
      "justification": "son frigo est littralement vide",
      "confiance": 95
    },
    {
      "code": "epuisement_aidant",
      "justification": "il est trs agressif, il lui crie dessus et j'ai remarqu qu'il lui demande de l'argent de faon trs insistante  chaque fois que je suis l",
      "confiance": 95
    },
    {
      "code": "anxiete",
      "justification": "elle a l'air terrorise",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "precarite_financiere": 95,
    "epuisement_aidant": 0,
    "anxiete": 95,
    "logement_inadapte": 100,
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
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": true,
  "vulnerabilites.social.isolement_relationnel": null
}

2. Calcul du score de complexit COMID...
Score Total : 4 (Situation non complexe)

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
La situation clinique est complexe avec une dpression grave, des troubles cognitifs majeurs et une perte d'autonomie rcente. La personne refuse les soins et l'aide  domicile.
Ville extraite : Toulon
Mdecin : incertain
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
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "insalubre",
  "demande.proposition_mail": "Bonjour, nous sommes proccups par la situation de Mme G. qui traverse une priode difficile suite au dcs de son poux. Elle souffre de dpression grave et refuse les soins mdicaux. Nous demandons votre aide pour valuer sa situation et proposer des solutions.",
  "demande.resume_structur": "La situation clinique est complexe avec une dpression grave, des troubles cognitifs majeurs et une perte d'autonomie rcente. La personne refuse les soins et l'aide  domicile.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 40,
    "aidant_regulier": 40,
    "medecin_traitant": 0,
    "malveillance": 100,
    "urgence": 90,
    "hospitalisation": 80,
    "motif": 100,
    "etat_logement": 90
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

[ CLIC - Centre Local d'Information et de Coordination (Snior) ] - Priorite : 80
Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
Contact : 04 94 24 65 25 | None

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
<summary>🔍 Cas Mme Vial (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Vial (Recherche Mdecin Traitant) ---

1. Extraction IA pour : 'Mme Vial, 82 ans, vient de s'installer  Toulon po...'

--- DEBUG : ANALYSE EXPERTE ---
La patiente de 82 ans, installe  Toulon, souffre de diabte et d'hypertension. Elle cherche un mdecin traitant aprs avoir dmnag et ne plus avoir accs  son ancien cabinet.
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
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "demande.proposition_mail": "Bonjour, je me permets de vous contacter pour demander votre aide dans la recherche d'un mdecin traitant pour ma mre de 82 ans. Elle a dmnag rcemment et n'a plus accs  son ancien cabinet. Je serais reconnaissant si vous pouviez nous aider  trouver un mdecin qui accepte de nouveaux patients.",
  "demande.resume_structur": "La patiente de 82 ans, installe  Toulon, souffre de diabte et d'hypertension. Elle cherche un mdecin traitant aprs avoir dmnag et ne plus avoir accs  son ancien cabinet.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 90,
    "aidant_regulier": 40,
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
  "demande.proposition_mail": "",
  "demande.resume_structur": "",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 70,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 40,
    "aidant_regulier": 40,
    "medecin_traitant": 0,
    "malveillance": 100,
    "urgence": 70,
    "hospitalisation": 90,
    "motif": 80,
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
    }
  ],
  "evaluation.confiance.comid": {
    "troubles_cognitifs": 95,
    "perte_autonomie_recente": 95,
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

--- RESULTATS DE L'ORIENTATION ---

[ CLIC - Centre Local d'Information et de Coordination (Snior) ] - Priorite : 80
Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
Contact : 04 94 24 65 25 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mr Petit (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Petit (Aidant Conjoint Epuis) ---

1. Extraction IA pour le rcit du conjoint aidant...

--- DEBUG : ANALYSE EXPERTE ---
La situation est critique pour la personne ge de 83 ans, vivant  Toulon avec un conjoint qui ncessite une aide importante. Elle a la maladie de Parkinson et ne peut plus sortir du logement sans ascenseur. Le conjoint est au bout du rouleau et craint pour son propre cur.
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
  "usager.situation_actuelle.PCH": "none",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "demande.proposition_mail": "Bonjour, je suis le conjoint d'une personne ge de 83 ans atteinte de la maladie de Parkinson qui ncessite une aide importante pour sortir du logement. Nous avons dj l'APA mais les quelques heures de mnage ne suffisent plus. Je suis au bout du rouleau et craint pour mon propre cur.",
  "demande.resume_structur": "La situation est critique pour la personne ge de 83 ans, vivant  Toulon avec un conjoint qui ncessite une aide importante. Elle a la maladie de Parkinson et ne peut plus sortir du logement sans ascenseur. Le conjoint est au bout du rouleau et craint pour son propre cur.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 100,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 40,
    "aidant_regulier": 40,
    "medecin_traitant": 100,
    "malveillance": 100,
    "urgence": 70,
    "hospitalisation": 0,
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
      "justification": "on habite seule",
      "confiance": 90
    },
    {
      "code": "anxiete",
      "justification": "je suis trs angoiss",
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

VOTRE PRIORIT ABSOLUE : [ DAC - Orientation complexe (APA + Problmatique de Sant) ]
MISSION : Patient bnficiant dj de l'APA mais prsentant une problmatique de sant/dgradation clinique : Ncessite une coordination intensive par le DAC pour rvaluer et scuriser le maintien  domicile.
CONTACT : 04 94 35 32 01

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
L'usager de 52 ans, rsidant  Toulon, bnficie de la PCH et cherche des informations sur les logements adapts  son fauteuil roulant dans la commune. Il souhaite galement savoir si des prestataires spcialiss sont disponibles pour l'aide humaine le week-end.
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
  "demande.proposition_mail": "Bonjour, je suis un usager de 52 ans rsidant  Toulon qui bnficie de la PCH et cherche des informations sur les logements adapts  mon fauteuil roulant dans la commune. Je souhaite galement savoir si des prestataires spcialiss sont disponibles pour l'aide humaine le week-end. Merci.",
  "demande.resume_structur": "L'usager de 52 ans, rsidant  Toulon, bnficie de la PCH et cherche des informations sur les logements adapts  son fauteuil roulant dans la commune. Il souhaite galement savoir si des prestataires spcialiss sont disponibles pour l'aide humaine le week-end.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 100,
    "gir": 0,
    "professionnels_domicile": 0,
    "aidant_regulier": 0,
    "medecin_traitant": 0,
    "malveillance": 100,
    "urgence": 70,
    "hospitalisation": 0,
    "motif": 90,
    "etat_logement": 80
  },
  "evaluation.comid.justifications": [
    {
      "code": "logement_inadapte",
      "justification": "Il est en situation de handicap moteur et bnficie de la PCH.",
      "confiance": 95
    },
    {
      "code": "isolement_social",
      "justification": "Il habite  Toulon.",
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
    -> Justification confiance : variable 'motif' extraite avec certitude de 90%, variable 'apa' extraite avec certitude de 0%, variable 'age' extraite avec certitude de 100%
  - [Centre Local d'Information et de Coordination (Exception PCH)] (Confiance : 95%) : Maintien  domicile : Accompagnement spcialis PCH (Prestation de Compensation du Handicap) pour les moins de 60 ans.
    -> Justification confiance : variable 'motif' extraite avec certitude de 90%, variable 'pch' extraite avec certitude de 100%
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
La patiente de 80 ans est hospitalise suite  une mauvaise chute et s'inquite pour son retour  domicile car elle vit seule au 3me tage. Elle a besoin d'aide pour organiser sa sortie et remplir ses dossiers administratifs.
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
  "demande.proposition_mail": "Bonjour, nous avons une patiente de 80 ans hospitalise suite  une mauvaise chute qui s'inquite pour son retour  domicile. Elle a besoin d'aide pour organiser sa sortie et remplir ses dossiers administratifs. Merci de votre aide.",
  "demande.resume_structur": "La patiente de 80 ans est hospitalise suite  une mauvaise chute et s'inquite pour son retour  domicile car elle vit seule au 3me tage. Elle a besoin d'aide pour organiser sa sortie et remplir ses dossiers administratifs.",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 0,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 70,
    "aidant_regulier": 70,
    "medecin_traitant": 0,
    "malveillance": 100,
    "urgence": 90,
    "hospitalisation": 100,
    "motif": 80,
    "etat_logement": 90
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
  "demande.proposition_mail": "Bonjour, nous sommes inquiets pour le bien-tre de Monsieur P., un homme de 88 ans qui vit seul  domicile et a une polypathologie. Il a oubli sa visite prvue et son rfrigrateur ne fonctionne plus. Nous demandons votre aide pour l'aider  rester chez lui.",
  "demande.resume_structur": "Monsieur P., un homme de 88 ans, vit seul  domicile et a une polypathologie. Il a oubli sa visite prvue et son rfrigrateur ne fonctionne plus. Il bnficie d'un mdecin traitant qui ne fait pas de visites  domicile.",
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
      "code": "multimorbidite",
      "justification": "polypathologie",
      "confiance": 95
    },
    {
      "code": "addiction",
      "justification": "addition  l'alcool",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "multimorbidite": 100,
    "addiction": 100
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
  "vulnerabilites.social.isolement_relationnel": null
}

2. Calcul du score de complexit COMID...
Score Total : 2 (Situation non complexe)

3. valuation de l'orientation...

4. Recherche des contacts territoriaux (La Garde)...

--- RSULTATS DE L'ORIENTATION POUR MME ANTOINETTE ---

[ CLIC - Centre Local d'Information et de Coordination (Snior) ] - Priorit : 80
Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
Contact : 04 22 44 84 73 | None

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

<details>
<summary>🔍 Cas Mme Bernard (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Bernard (Suspicion de maltraitance) ---

1. Extraction IA pour : 'Mme Bernard, 88 ans, habite  La Seyne-sur-Mer. El...'

--- DEBUG : ANALYSE EXPERTE ---
La situation clinique concerne une personne ge de 88 ans, isole et victime de vol d'argent par son petit-fils. Elle est terrorise  l'ide de parler et prsente des ecchymoses suspectes sur les bras.
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
  "demande.motif_principal": "aide_alimentaire",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "demande.proposition_mail": "Bonjour, nous sommes proccups par la situation de Mme B., 88 ans, isole et victime de vol d'argent par son petit-fils. Elle a besoin d'aide pour s'acheter  manger et demande une orientation.",
  "demande.resume_structur": "La situation clinique concerne une personne ge de 88 ans, isole et victime de vol d'argent par son petit-fils. Elle est terrorise  l'ide de parler et prsente des ecchymoses suspectes sur les bras.",
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
    "urgence": 30,
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

[ CCAS - Secours d'Urgence (Alimentaire & Factures) ] - Priorite : 85
Objectif : Secours financier ou alimentaire d'urgence de proximit : Attribution d'aides extra-lgales par la mairie.
Contact : 04 94 06 97 18 | Espace Herms 2 avenue Charles-Gide 83500 La Seyne-sur-Mer

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
M. D., 74 ans, souffre de diabte, d'hypertension et d'une insuffisance rnale chronique qui lui cause des douleurs permanentes dans les jambes. Il prend 8 mdicaments par jour. Il est trs anxieux pour sa sant et appelle le cabinet infirmier plusieurs fois par jour pour demander s'il a bien pris ses cachets.
Ville extraite : Toulon
Mdecin : identifie
Malveillance : aucune
Hospitalisation : aucun
tat Logement : insalubre
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
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "insalubre",
  "demande.proposition_mail": "Bonjour, nous sommes proccups par la situation de M. D., g de 74 ans, qui souffre de diabte, d'hypertension et d'une insuffisance rnale chronique. Il est anxieux pour sa sant et a besoin d'aide pour maintenir son autonomie  domicile.",
  "demande.resume_structur": "M. D., 74 ans, souffre de diabte, d'hypertension et d'une insuffisance rnale chronique qui lui cause des douleurs permanentes dans les jambes. Il prend 8 mdicaments par jour. Il est trs anxieux pour sa sant et appelle le cabinet infirmier plusieurs fois par jour pour demander s'il a bien pris ses cachets.",
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
    "etat_logement": 60
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
    "logement_inadapte": 100,
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

[ CLIC - Centre Local d'Information et de Coordination (Snior) ] - Priorite : 80
Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
Contact : 04 94 24 65 25 | None

[ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ] - Priorite : 70
Objectif : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
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
  "usager.situation_actuelle.PCH": "none",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "evaluation_globale",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "diogene",
  "demande.proposition_mail": "",
  "demande.resume_structur": "",
  "evaluation.confiance.variables": {
    "age": 100,
    "ville": 100,
    "apa": 0,
    "pch": 0,
    "gir": 0,
    "professionnels_domicile": 0,
    "aidant_regulier": 0,
    "medecin_traitant": 70,
    "malveillance": 100,
    "urgence": 40,
    "hospitalisation": 0,
    "motif": 100,
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
    },
    {
      "code": "perte_autonomie_recente",
      "justification": "Risque majeur de chute",
      "confiance": 95
    }
  ],
  "evaluation.confiance.comid": {
    "isolement_social": 95,
    "logement_inadapte": 100,
    "epuisement_aidant": 95,
    "troubles_cognitifs": 95,
    "perte_autonomie_recente": 95
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

4. Recherche des contacts territoriaux (Ollioules)...

--- RSULTATS DE L'ORIENTATION POUR MME GEORGETTE MOUTON ---

[ UTS Littoral Sud Sainte Baume - OLLIOULES (Relais CLIC) ] - Priorit : 80
Objectif : La commune ne dispose pas de CLIC, se rapprocher de l'UTS. Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
Contact : 04 83 95 58 50 | Espace Pierre Puget 2 Place Marius Trotobas 83190 Ollioules

[ CPTS - Communaut Professionnelle Territoriale de Sant ] - Priorit : 50
Objectif : Accs aux soins : Recherche de mdecin traitant (justifie par retraite/dmnagement) et dispositif MISAS pour viter le renoncement aux soins.
Contact : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

BDD - Dossier sauvegard avec succs en base de donnes de manire anonymise.

```

</details>

