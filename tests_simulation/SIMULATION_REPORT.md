# 📋 Rapport d'Évaluation Clinique ORIA

Généré automatiquement le : `2026-05-28 09:33:13`  
Nombre de cas exécutés : **21**  
Taux de succès : **21/21**  
Temps d'exécution total : **311.62 secondes**  

## 📊 Tableau récapitulatif des Orientations

| Patient | Status | Score COMID | Orientation Principale | Temps d'exécution |
| :--- | :---: | :---: | :--- | :---: |
| **Mme Fontaine** | ✅ SUCCESS | 3 | `N/A` | 16.09s |
| **Mme Antoinette** | ✅ SUCCESS | 3 | `"refus_de_soins", "refus_aide_domicile"` | 16.67s |
| **Mr Vacek** | ✅ SUCCESS | 2 | `N/A` | 12.54s |
| **Mr Dubois** | ✅ SUCCESS | 4 | `N/A` | 14.73s |
| **Mme Mouton** | ✅ SUCCESS | 3 | `DAC - Suspicion de Diogne ou incurie` | 16.34s |
| **Mme Huguette** | ✅ SUCCESS | 2 | `N/A` | 14.19s |
| **Mr Lambert** | ✅ SUCCESS | 3 | `Suspicion de Diogne ou incurie` | 15.82s |
| **Mme Petit** | ✅ SUCCESS | 2 | `N/A` | 15.46s |
| **Mme Lefebvre** | ✅ SUCCESS | 3 | `DAC - Suspicion de Diogne ou incurie` | 13.98s |
| **Mr Leroy** | ✅ SUCCESS | 4 | `N/A` | 18.33s |
| **Mme Bernard** | ✅ SUCCESS | 2 | `N/A` | 14.54s |
| **Mme Durand** | ✅ SUCCESS | 3 | `Suspicion de Diogne ou incurie` | 15.11s |
| **Mme Rossi** | ✅ SUCCESS | 2 | `N/A` | 13.91s |
| **Mme Martin** | ✅ SUCCESS | 3 | `N/A` | 13.28s |
| **Mr Martin** | ✅ SUCCESS | 2 | `N/A` | 15.07s |
| **Mme Vial** | ✅ SUCCESS | 2 | `"absent", "non_identifie_avec_certitude"` | 15.53s |
| **Mme Michu** | ✅ SUCCESS | 3 | `"refus_de_soins", "refus_aide_domicile"` | 13.42s |
| **Mr Petit** | ✅ SUCCESS | 3 | `N/A` | 15.38s |
| **Clarification And Validation** | ✅ SUCCESS | N/A | `DEBUG : extracted_data` | 11.82s |
| **Mr Chen** | ✅ SUCCESS | 1 | `N/A` | 10.91s |
| **Mme Morel** | ✅ SUCCESS | 3 | `N/A` | 18.50s |

---

## 📝 Détail des extractions et raisonnements

<details>
<summary>🔍 Cas Mme Fontaine (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Fontaine (Alerte Kin) ---

1. Extraction IA pour l'alerte du kin...

--- DEBUG : ANALYSE EXPERTE ---
La situation est critique car la patiente perd son autonomie et est victime de spoliation financire par son fils. Il est important d'intervenir pour protger la patiente et assurer sa scurit.
Ville extraite : Sanary
Mdecin : identifie
Malveillance : spoliation_financiere
Hospitalisation : aucun
tat Logement : insalubre
--- FIN DEBUG ---

Donnes extraites (JSON) :
{
  "usager.identite.age_estime": 85,
  "usager.localisation.commune_residence": "Sanary",
  "usager.situation_actuelle.APA": "inconnu",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "spoliation_financiere",
  "adresseur.degre_urgence_percu": "eleve",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "insalubre",
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": true,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": true,
  "evaluation.comid.epuisement_aidant": true,
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
Score Total : 3 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Sanary-sur-Mer)...

--- REPONSE D'ORIA POUR LE KINE ---
ORIA : 'Situation identifie comme Situation non complexe. Voici les actions prioritaires :'

=================================================================
  [ CEV - Cellule coute et Vigilance (Spoliation & Autres Dangers) ]    Priorite : 107
=================================================================
  Objectif : Mise en scurit immdiate, protection juridique et physique des majeurs vulnrables en situation de danger social ou maltraitance financire.
  Contact  : 04 83 95 16 01 | None

  Pourquoi cette orientation :
    -> Suspicion de malveillance = "spoliation_financiere"  (est parmi ["violences_psychologiques", "violences_sexuelles", "negligence", "spoliation_financiere", ... +3])

=================================================================
  [ UTS Littoral Sud Sainte Baume - SANARY (Relais CLIC) ]    Priorite : 80
=================================================================
  Objectif : La commune ne dispose pas de CLIC, se rapprocher de l'UTS. Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
  Contact  : 04 83 95 83 10 | CCAS Picotires 281 avenue Marchal LeClerc 83110 Sanary sur mer

  Pourquoi cette orientation :
    -> puisement de l'aidant = OUI  (est OUI)

=================================================================
  [ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ]    Priorite : 78
=================================================================
  Objectif : Maintien  domicile renforc et intensif : Alternative  l'EHPAD pour les situations en perte d'autonomie importante ou complexit technique.
  Contact  : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chnes 83500 LA SEYNE SUR MER

  Pourquoi cette orientation :
    -> puisement de l'aidant = OUI  (est OUI)

=================================================================
  [ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ]    Priorite : 70
=================================================================
  Objectif : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
  Contact  : 04 83 95 83 10 | CCAS Picotires 281 avenue Marchal LeClerc 83110 Sanary sur mer

  Pourquoi cette orientation :
    -> Prcarit financire = OUI  (est OUI)

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

<details>
<summary>🔍 Cas Mme Antoinette (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Antoinette (Nouveau Cas Complexe) ---

1. Extraction IA (Dterministe, Temp=0.0) pour : 'Mme Antoinette, 92 ans, rside  La Garde. Elle vit avec son mari M. Pierre (89 ...'

--- DEBUG : ANALYSE EXPERTE ---
La situation est critique car la personne refuse catgoriquement l'aide des auxiliaires de vie du SAAD, ce qui met en pril sa sant et son bien-tre. Il est essentiel d'organiser une aide  domicile pour maintenir sa scurit et sa dignit.
Ville extraite : La Garde
Mdecin : identifie
Malveillance : aucune
Hospitalisation : recente
tat Logement : non_renseigne
--- FIN DEBUG ---

Donnes extraites (JSON) :
{
  "usager.identite.age_estime": 92,
  "usager.localisation.commune_residence": "La Garde",
  "usager.situation_actuelle.APA": "oui",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": 2,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "recente",
  "demande.motif_principal": "refus_aide_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "oui",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": true,
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

3. valuation de l'orientation...

4. Recherche des contacts territoriaux (La Garde)...

--- RSULTATS DE L'ORIENTATION POUR MME ANTOINETTE ---

=================================================================
  [ DAC - Refus de soins ou d'aide (Priorit Absolue) ]    Priorite : 105
=================================================================
  Objectif : Refus de soins ou opposition critique aux aides  domicile : Rupture critique de parcours ncessitant l'intervention immdiate du DAC pour dbloquer la situation.
  Contact  : 04 94 35 32 01 | None

  Pourquoi cette orientation :
    -> Motif principal de la demande = "refus_aide_domicile"  (est parmi ["refus_de_soins", "refus_aide_domicile"])

=================================================================
  [ PSCG SS APA - Ple Social de Solidarit et de Gestion (APA) ]    Priorite : 100
=================================================================
  Objectif : Contacter votre rfrent APA au Conseil Dpartemental (PSCG SS APA) pour toute modification de plan d'aide ou besoin d'accompagnement social supplmentaire.
  Contact  : 04 83 95 79 51 | None

  Pourquoi cette orientation :
    -> Statut APA = "oui"  (est "oui")

=================================================================
  [ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ]    Priorite : 78
=================================================================
  Objectif : Maintien  domicile renforc et intensif : Alternative  l'EHPAD pour les situations en perte d'autonomie importante ou complexit technique.
  Contact  : 06 83 38 39 39 | 421 Av 1er Bataillon Infanterie de Marine du Pacifique 83130 La Garde

  Pourquoi cette orientation :
    -> puisement de l'aidant = OUI  (est OUI)

=================================================================
  [ Service Social de l'Hpital (Hospitalisation rcente) ]    Priorite : 75
=================================================================
  Objectif : Transition hospitalire sociale : Organisation de la sortie rcente et suivi de l'accompagnement social post-hospitalisation.
  Contact  : Non trouve dans le referentiel territorial

  Pourquoi cette orientation :
    -> Statut d'hospitalisation = "recente"  (est "recente")

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

<details>
<summary>🔍 Cas Mr Vacek (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Vacek (Habitat Indigne & Danger) ---

1. Extraction IA pour la situation de pril...

--- DEBUG : ANALYSE EXPERTE ---
Analyse manquante
Ville extraite : Toulon
Mdecin : incertain
Malveillance : spoliation_financiere
Hospitalisation : aucun
tat Logement : insalubre
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 65,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "inconnu",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "spoliation_financiere",
  "adresseur.degre_urgence_percu": "critique",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "insalubre",
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

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- REPONSE D'ORIA (URGENCE HABITAT) ---
ORIA : 'La situation de M. Vacek presente un DANGER IMMINENT.'

=================================================================
  [ CEV - Cellule coute et Vigilance (Spoliation & Autres Dangers) ]    Priorite : 107
=================================================================
  Objectif : Mise en scurit immdiate, protection juridique et physique des majeurs vulnrables en situation de danger social ou maltraitance financire.
  Contact  : 04 83 95 16 01 | None

  Pourquoi cette orientation :
    -> Suspicion de malveillance = "spoliation_financiere"  (est parmi ["violences_psychologiques", "violences_sexuelles", "negligence", "spoliation_financiere", ... +3])

=================================================================
  [ CLIC - Centre Local d'Information et de Coordination (Snior) ]    Priorite : 80
=================================================================
  Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
  Contact  : 04 94 24 65 25 | None

  Pourquoi cette orientation :
    -> Motif principal de la demande = "maintien_a_domicile"  (contient l'un de ["maintien_a_domicile", "renforcement_domicile", "aide_a_domicile", "information_aides", ... +3])

=================================================================
  [ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ]    Priorite : 70
=================================================================
  Objectif : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
  Contact  : 04 83 95 24 42 | 100, traverse des minimes 83000 Toulon

  Pourquoi cette orientation :
    -> Prcarit financire = OUI  (est OUI)

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

<details>
<summary>🔍 Cas Mr Dubois (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Dubois ---

1. Extraction IA pour : 'M. Dubois, 74 ans, vit  Toulon. Il souffre de dia...'

--- DEBUG : ANALYSE EXPERTE ---
Analyse manquante
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
  "usager.situation_actuelle.APA": "inconnu",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "insalubre",
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": true,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": true,
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
Score Total : 4 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION ---

=================================================================
  [ CLIC - Centre Local d'Information et de Coordination (Snior) ]    Priorite : 80
=================================================================
  Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
  Contact  : 04 94 24 65 25 | None

  Pourquoi cette orientation :
    -> Motif principal de la demande = "maintien_a_domicile"  (contient l'un de ["maintien_a_domicile", "renforcement_domicile", "aide_a_domicile", "information_aides", ... +3])

=================================================================
  [ DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social) ]    Priorite : 72
=================================================================
  Objectif : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
  Contact  : 04 94 35 32 01 | None

  Pourquoi cette orientation :
    -> Score COMID total = "4"  (est >= "4")

=================================================================
  [ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ]    Priorite : 70
=================================================================
  Objectif : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
  Contact  : 04 83 95 24 42 | 100, traverse des minimes 83000 Toulon

  Pourquoi cette orientation :
    -> Prcarit financire = OUI  (est OUI)

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

<details>
<summary>🔍 Cas Mme Mouton (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Georgette Mouton (Ollioules) ---

1. Extraction IA pour : 'Mme Georgette Mouton, 83 ans, vit seule  Ollioules dans un appartement devenu e...'

--- DEBUG : ANALYSE EXPERTE ---
La situation clinique est critique en raison de l'isolement social, du risque de chute et des frquents oublis de mdicaments. Il est essentiel d'intervenir pour amliorer la prise en charge de cette personne.
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
  "adresseur.degre_urgence_percu": "eleve",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "diogene",
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

3. valuation de l'orientation...

4. Recherche des contacts territoriaux (Ollioules)...

--- RSULTATS DE L'ORIENTATION POUR MME GEORGETTE MOUTON ---

=================================================================
  [ DAC - Suspicion de Diogne ou incurie ]    Priorite : 96
=================================================================
  Objectif : Insalubrit ou ngligence critique  domicile : Suspicion ou syndrome de Diogne/incurie avr ncessitant une coordination multidimensionnelle renforce par le DAC.
  Contact  : 04 94 35 32 01 | None

  Pourquoi cette orientation :
    -> usager.cadre_de_vie.etat_logement = "diogene"  (est parmi ["diogene", "incurie"])

=================================================================
  [ UTS Littoral Sud Sainte Baume - OLLIOULES (Relais CLIC) ]    Priorite : 80
=================================================================
  Objectif : La commune ne dispose pas de CLIC, se rapprocher de l'UTS. Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
  Contact  : 04 83 95 58 50 | Espace Pierre Puget 2 Place Marius Trotobas 83190 Ollioules

  Pourquoi cette orientation :
    -> Motif principal de la demande = "maintien_a_domicile"  (contient l'un de ["maintien_a_domicile", "renforcement_domicile", "aide_a_domicile", "information_aides", ... +3])

=================================================================
  [ CPTS - Communaut Professionnelle Territoriale de Sant ]    Priorite : 50
=================================================================
  Objectif : Accs aux soins : Recherche de mdecin traitant (justifie par retraite/dmnagement) et dispositif MISAS pour viter le renoncement aux soins.
  Contact  : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

  Pourquoi cette orientation :
    -> Mdecin traitant = "absent"  (est parmi ["absent", "non_identifie_avec_certitude"])

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

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
  "adresseur.degre_urgence_percu": "eleve",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "insalubre",
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

3. valuation de l'orientation...

4. Recherche des contacts territoriaux (La Valette)...

--- RSULTATS DE L'ORIENTATION POUR MME HUGUETTE ---

=================================================================
  [ CEV - Cellule coute et Vigilance (Spoliation & Autres Dangers) ]    Priorite : 107
=================================================================
  Objectif : Mise en scurit immdiate, protection juridique et physique des majeurs vulnrables en situation de danger social ou maltraitance financire.
  Contact  : 04 83 95 16 01 | None

  Pourquoi cette orientation :
    -> Suspicion de malveillance = "spoliation_financiere"  (est parmi ["violences_psychologiques", "violences_sexuelles", "negligence", "spoliation_financiere", ... +3])

=================================================================
  [ CLIC - Centre Local d'Information et de Coordination (Snior) ]    Priorite : 80
=================================================================
  Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
  Contact  : 04 22 44 84 73 | None

  Pourquoi cette orientation :
    -> Motif principal de la demande = "maintien_a_domicile"  (contient l'un de ["maintien_a_domicile", "renforcement_domicile", "aide_a_domicile", "information_aides", ... +3])

=================================================================
  [ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ]    Priorite : 70
=================================================================
  Objectif : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
  Contact  : 04 83 95 56 90 | 427 Avenue Duchatel 83130 La Valette du Var

  Pourquoi cette orientation :
    -> Prcarit financire = OUI  (est OUI)

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

<details>
<summary>🔍 Cas Mr Lambert (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Lambert (Appel Infirmire) ---

1. Extraction IA pour le rcit de l'infirmire...

--- DEBUG : ANALYSE EXPERTE ---
La situation est proccupante, le patient refuse les soins et il y a une perte d'autonomie importante. Il est important de trouver un moyen pour aider ce patient  maintenir son indpendance et sa dignit.
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
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "diogene",
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
Score Total : 3 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (La Seyne-sur-Mer)...

--- REPONSE D'ORIA POUR L'INFIRMIERE ---
ORIA : 'D'aprs votre description, la situation de M. Lambert est Situation non complexe. Voici les priorits d'appel :'

=================================================================
  [ DAC - Dispositif d'Appui  la Coordination ]    Priorite : 105
=================================================================
  Objectif : Motifs d'orientation combins :
  - [Refus de soins ou d'aide (Priorit Absolue)] : Refus de soins ou opposition critique aux aides  domicile : Rupture critique de parcours ncessitant l'intervention immdiate du DAC pour dbloquer la situation.
  - [Suspicion de Diogne ou incurie] : Insalubrit ou ngligence critique  domicile : Suspicion ou syndrome de Diogne/incurie avr ncessitant une coordination multidimensionnelle renforce par le DAC.
  Contact  : 04 94 35 32 01 | None

  Pourquoi cette orientation :
    -> Opposition aux soins = OUI  (est OUI)
    -> usager.cadre_de_vie.etat_logement = "diogene"  (est parmi ["diogene", "incurie"])

=================================================================
  [ CLIC - Centre Local d'Information et de Coordination (Snior) ]    Priorite : 80
=================================================================
  Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
  Contact  : 04 94 06 97 04 | None

  Pourquoi cette orientation :
    -> Motif principal de la demande = "maintien_a_domicile"  (contient l'un de ["maintien_a_domicile", "renforcement_domicile", "aide_a_domicile", "information_aides", ... +3])

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

<details>
<summary>🔍 Cas Mme Petit (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Petit (Urgence CCAS) ---

1. Extraction IA pour : 'Mme Petit, 78 ans, habite  La Garde. Elle vit seu...'

--- DEBUG : ANALYSE EXPERTE ---
La personne ge de 78 ans, vivant seule  La Garde, est en situation de prcarit financire et alimentaire. Elle a reu une lettre de rappel pour sa facture d'lectricit et demande de l'aide pour ses courses. Il s'agit d'une urgence modre car la personne est menace par la faim et le dcouvert bancaire.
Ville extraite : La Garde
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : non_renseigne
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
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "aide_alimentaire",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
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

=================================================================
  [ CCAS - Secours d'Urgence (Alimentaire & Factures) ]    Priorite : 85
=================================================================
  Objectif : Secours financier ou alimentaire d'urgence de proximit : Attribution d'aides extra-lgales par la mairie.
  Contact  : 04 94 08 98 34 | 81 Rue Marius Tardivier 83130 La garde

  Pourquoi cette orientation :
    -> Motif principal de la demande = "aide_alimentaire"  (est parmi ["aide_alimentaire", "secours_urgence", "factures"])

=================================================================
  [ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ]    Priorite : 70
=================================================================
  Objectif : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
  Contact  : 04 83 95 56 50 | 53 Impasse Blriot Immeuble Le Frdric 83130 La Garde

  Pourquoi cette orientation :
    -> Prcarit financire = OUI  (est OUI)

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

<details>
<summary>🔍 Cas Mme Lefebvre (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Lefebvre ---

1. Extraction IA pour : 'Mme Lefebvre, 65 ans, vit  La Garde. Elle est sui...'

--- DEBUG : ANALYSE EXPERTE ---
Analyse manquante
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
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "diogene",
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": false,
  "evaluation.comid.logement_inadapte": true,
  "evaluation.comid.depression": false,
  "evaluation.comid.psychiatrie": false,
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
  "vulnerabilites.social.isolement_relationnel": null
}

2. Calcul du score de complexit COMID...
Score Total : 3 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (La Garde)...

--- RESULTATS DE L'ORIENTATION ---

=================================================================
  [ DAC - Suspicion de Diogne ou incurie ]    Priorite : 96
=================================================================
  Objectif : Insalubrit ou ngligence critique  domicile : Suspicion ou syndrome de Diogne/incurie avr ncessitant une coordination multidimensionnelle renforce par le DAC.
  Contact  : 04 94 35 32 01 | None

  Pourquoi cette orientation :
    -> usager.cadre_de_vie.etat_logement = "diogene"  (est parmi ["diogene", "incurie"])

=================================================================
  [ CLIC - Centre Local d'Information et de Coordination (Snior) ]    Priorite : 80
=================================================================
  Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
  Contact  : 04 22 44 84 73 | None

  Pourquoi cette orientation :
    -> Motif principal de la demande = "maintien_a_domicile"  (contient l'un de ["maintien_a_domicile", "renforcement_domicile", "aide_a_domicile", "information_aides", ... +3])

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

<details>
<summary>🔍 Cas Mr Leroy (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Leroy (Moins de 60 ans) ---

1. Extraction IA pour : 'M. Leroy, 45 ans, habite  Toulon. Il est atteint ...'

--- DEBUG : ANALYSE EXPERTE ---
La situation est critique car l'usager est atteint d'une Sclrose en Plaques (SEP) diagnostique il y a 2 ans et vit seul, ce qui le rend vulnrable. Il a du mal  payer son loyer et se sent perdu dans son parcours de soins entre les diffrents spcialistes. Il exprime des ides noires et il est important de fournir une aide immdiate pour viter une situation critique.
Ville extraite : Toulon
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : insalubre
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
  "adresseur.degre_urgence_percu": "eleve",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "insalubre",
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
  "evaluation.comid.degradation_recente": true,
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

--- RESULTATS DE L'ORIENTATION (Age: 45 ans) ---

=================================================================
  [ CLIC - Centre Local d'Information et de Coordination (Snior) ]    Priorite : 80
=================================================================
  Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
  Contact  : 04 94 24 65 25 | None

  Pourquoi cette orientation :
    -> Motif principal de la demande = "maintien_a_domicile"  (contient l'un de ["maintien_a_domicile", "renforcement_domicile", "aide_a_domicile", "information_aides", ... +3])

=================================================================
  [ DAC - Situation de complexit multidimensionnelle (Sanitaire, Social, Mdico-social) ]    Priorite : 72
=================================================================
  Objectif : Situation de forte complexit multidimensionnelle (sanitaire, social et mdico-social) : valuation globale et coordination intensive par le DAC pour dbloquer le parcours de vie  domicile.
  Contact  : 04 94 35 32 01 | None

  Pourquoi cette orientation :
    -> Score COMID total = "4"  (est >= "4")

=================================================================
  [ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ]    Priorite : 70
=================================================================
  Objectif : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
  Contact  : 04 83 95 24 42 | 100, traverse des minimes 83000 Toulon

  Pourquoi cette orientation :
    -> Prcarit financire = OUI  (est OUI)

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

<details>
<summary>🔍 Cas Mme Bernard (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Bernard (Suspicion de maltraitance) ---

1. Extraction IA pour : 'Mme Bernard, 88 ans, habite  La Seyne-sur-Mer. El...'

--- DEBUG : ANALYSE EXPERTE ---
La situation est critique car la personne est trs isole et victime de spoliation financire par son petit-fils. Elle a des ecchymoses suspectes sur les bras et semble terrorise  l'ide de parler.
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
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "spoliation_financiere",
  "adresseur.degre_urgence_percu": "eleve",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "secours_urgence",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
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

4. Recherche des contacts territoriaux...
Ville extraite par l'IA : La Seyne-sur-Mer

--- RESULTATS DE L'ORIENTATION (Territoire: La Seyne-sur-mer) ---

=================================================================
  [ CEV - Cellule coute et Vigilance (Spoliation & Autres Dangers) ]    Priorite : 107
=================================================================
  Objectif : Mise en scurit immdiate, protection juridique et physique des majeurs vulnrables en situation de danger social ou maltraitance financire.
  Contact  : 04 83 95 16 01 | None

  Pourquoi cette orientation :
    -> Suspicion de malveillance = "spoliation_financiere"  (est parmi ["violences_psychologiques", "violences_sexuelles", "negligence", "spoliation_financiere", ... +3])

=================================================================
  [ CCAS - Secours d'Urgence (Alimentaire & Factures) ]    Priorite : 85
=================================================================
  Objectif : Secours financier ou alimentaire d'urgence de proximit : Attribution d'aides extra-lgales par la mairie.
  Contact  : 04 94 06 97 18 | Espace Herms 2 avenue Charles-Gide 83500 La Seyne-sur-Mer

  Pourquoi cette orientation :
    -> Motif principal de la demande = "secours_urgence"  (est parmi ["aide_alimentaire", "secours_urgence", "factures"])

=================================================================
  [ CLIC - Centre Local d'Information et de Coordination (Snior) ]    Priorite : 80
=================================================================
  Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
  Contact  : 04 94 06 97 04 | None

  Pourquoi cette orientation :
    -> Motif principal de la demande = "secours_urgence"  (contient l'un de ["maintien_a_domicile", "renforcement_domicile", "aide_a_domicile", "information_aides", ... +3])

=================================================================
  [ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ]    Priorite : 70
=================================================================
  Objectif : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
  Contact  : 04 83 95 48 30 ou 04 83 95 37 99 | rue Charles Gide 83500 La Seyne sur mer

  Pourquoi cette orientation :
    -> Prcarit financire = OUI  (est OUI)

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

<details>
<summary>🔍 Cas Mme Durand (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Durand ---

1. Extraction IA pour : 'Mme Durand, 88 ans, vit  Hyres. Elle est trs co...'

--- DEBUG : ANALYSE EXPERTE ---
La situation est critique car l'usager refuse les soins mdicaux et prsente une perte d'autonomie importante. Il est important de trouver un plan d'aide adapt pour maintenir son autonomie et viter des situations dangereuses.
Ville extraite : Hyres
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : incurie
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 88,
  "usager.localisation.commune_residence": "Hyres",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "eleve",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "incurie",
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
Score Total : 3 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Hyres)...

--- RESULTATS DE L'ORIENTATION ---

=================================================================
  [ DAC - Dispositif d'Appui  la Coordination ]    Priorite : 105
=================================================================
  Objectif : Motifs d'orientation combins :
  - [Refus de soins ou d'aide (Priorit Absolue)] : Refus de soins ou opposition critique aux aides  domicile : Rupture critique de parcours ncessitant l'intervention immdiate du DAC pour dbloquer la situation.
  - [Suspicion de Diogne ou incurie] : Insalubrit ou ngligence critique  domicile : Suspicion ou syndrome de Diogne/incurie avr ncessitant une coordination multidimensionnelle renforce par le DAC.
  Contact  : Non trouve dans le referentiel territorial

  Pourquoi cette orientation :
    -> Motif principal de la demande = "refus_de_soins"  (est parmi ["refus_de_soins", "refus_aide_domicile"])
    -> usager.cadre_de_vie.etat_logement = "incurie"  (est parmi ["diogene", "incurie"])

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

<details>
<summary>🔍 Cas Mme Rossi (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Rossi (Violences Conjugales) ---

1. Extraction IA pour : 'Mme Rossi, 70 ans, habite  Toulon. Elle vient d'a...'

--- DEBUG : ANALYSE EXPERTE ---
La situation est critique car la personne a d quitter son domicile en urgence suite  des violences physiques graves et ncessite une protection immdiate.
Ville extraite : Toulon
Mdecin : incertain
Malveillance : violences_physiques
Hospitalisation : aucun
tat Logement : non_renseigne
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
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
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

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION (Protection / Violences) ---

=================================================================
  [ Police / Gendarmerie (Urgence Vitale & Intervention) ]    Priorite : 110
=================================================================
  Objectif : Intervention immdiate des forces de l'ordre en cas d'agression physique active et en cours ou danger vital imminent.
  Contact  : Non trouve dans le referentiel territorial

  Pourquoi cette orientation :
    -> Urgence perue = "critique"  (est "critique")
    -> Motif principal de la demande = "secours_urgence"  (est "secours_urgence")

=================================================================
  [ CEV - Cellule coute et Vigilance (Violences Physiques & Danger Immdiat) ]    Priorite : 107
=================================================================
  Objectif : Mise en scurit immdiate et protection d'urgence des majeurs vulnrables en situation de violence physique active ou menace.
  Contact  : 04 83 95 16 01 | None

  Pourquoi cette orientation :
    -> Suspicion de malveillance = "violences_physiques"  (est "violences_physiques")

=================================================================
  [ CCAS - Secours d'Urgence (Alimentaire & Factures) ]    Priorite : 85
=================================================================
  Objectif : Secours financier ou alimentaire d'urgence de proximit : Attribution d'aides extra-lgales par la mairie.
  Contact  : 04 94 24 65 00 | 100 rue des remparts - CS 20813 83051 Toulon Cedex

  Pourquoi cette orientation :
    -> Motif principal de la demande = "secours_urgence"  (est parmi ["aide_alimentaire", "secours_urgence", "factures"])

=================================================================
  [ CLIC - Centre Local d'Information et de Coordination (Snior) ]    Priorite : 80
=================================================================
  Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
  Contact  : 04 94 24 65 25 | None

  Pourquoi cette orientation :
    -> Motif principal de la demande = "secours_urgence"  (contient l'un de ["maintien_a_domicile", "renforcement_domicile", "aide_a_domicile", "information_aides", ... +3])

=================================================================
  [ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ]    Priorite : 70
=================================================================
  Objectif : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
  Contact  : 04 83 95 24 42 | 100, traverse des minimes 83000 Toulon

  Pourquoi cette orientation :
    -> Prcarit financire = OUI  (est OUI)

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

<details>
<summary>🔍 Cas Mme Martin (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Martin (Dtresse Aidant) ---

1. Extraction IA pour le rcit de l'aidante...

--- DEBUG : ANALYSE EXPERTE ---
Analyse manquante
Ville extraite : Toulon
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : non_renseigne
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 82,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "inconnu",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": true,
  "evaluation.comid.litteratie_faible": true,
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
Score Total : 3 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...
ORIA : 'Je comprends votre epuisement. La situation de votre mere est Situation non complexe.'

=================================================================
  [ CLIC - Centre Local d'Information et de Coordination (Snior) ]    Priorite : 80
=================================================================
  Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
  Contact  : 04 94 24 65 25 | None

  Pourquoi cette orientation :
    -> puisement de l'aidant = OUI  (est OUI)

=================================================================
  [ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ]    Priorite : 78
=================================================================
  Objectif : Maintien  domicile renforc et intensif : Alternative  l'EHPAD pour les situations en perte d'autonomie importante ou complexit technique.
  Contact  : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chnes 83500 LA SEYNE SUR MER

  Pourquoi cette orientation :
    -> puisement de l'aidant = OUI  (est OUI)

CONSEIL POUR VOUS : 'Pensez egalement a contacter une plateforme de repit pour aidants. Ces structures proposent du soutien psychologique pour vous permettre de souffler.'

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

<details>
<summary>🔍 Cas Mr Martin (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Martin ---

1. Extraction IA pour : 'M. Martin, 75 ans, habite  La Seyne-sur-Mer. Il a...'

--- DEBUG : ANALYSE EXPERTE ---
La situation est proccupante car l'usager est seul et a des problmes de vue, ce qui rend difficile son quotidien. Il y a galement une hospitalisation rcente de sa femme, ce qui ajoute  la complexit de la situation.
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
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": true,
  "evaluation.comid.epuisement_aidant": true,
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

4. Recherche des contacts territoriaux (La Seyne-sur-Mer)...

--- RESULTATS DE L'ORIENTATION ---

=================================================================
  [ CLIC - Centre Local d'Information et de Coordination (Snior) ]    Priorite : 80
=================================================================
  Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
  Contact  : 04 94 06 97 04 | None

  Pourquoi cette orientation :
    -> puisement de l'aidant = OUI  (est OUI)

=================================================================
  [ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ]    Priorite : 78
=================================================================
  Objectif : Maintien  domicile renforc et intensif : Alternative  l'EHPAD pour les situations en perte d'autonomie importante ou complexit technique.
  Contact  : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chnes 83500 LA SEYNE SUR MER

  Pourquoi cette orientation :
    -> puisement de l'aidant = OUI  (est OUI)

=================================================================
  [ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ]    Priorite : 70
=================================================================
  Objectif : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
  Contact  : 04 83 95 48 30 ou 04 83 95 37 99 | rue Charles Gide 83500 La Seyne sur mer

  Pourquoi cette orientation :
    -> Prcarit financire = OUI  (est OUI)

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

<details>
<summary>🔍 Cas Mme Vial (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Vial (Recherche Mdecin Traitant) ---

1. Extraction IA pour : 'Mme Vial, 82 ans, vient de s'installer  Toulon po...'

--- DEBUG : ANALYSE EXPERTE ---
La personne ge de 82 ans, installe  Toulon, souffre de diabte et d'hypertension. Elle n'a plus de mdecin traitant et cherche un nouveau mdecin pour obtenir des soins mdicaux. La situation est proccupante car elle manque de mdicaments et est angoisse par la rupture de suivi mdical.
Ville extraite : Toulon
Mdecin : absent
Malveillance : aucune
Hospitalisation : aucun
tat Logement : non_renseigne
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 82,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "inconnu",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "recherche_medecin",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
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

=================================================================
  [ CPTS - Communaut Professionnelle Territoriale de Sant ]    Priorite : 50
=================================================================
  Objectif : Accs aux soins : Recherche de mdecin traitant (justifie par retraite/dmnagement) et dispositif MISAS pour viter le renoncement aux soins.
  Contact  : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

  Pourquoi cette orientation :
    -> Mdecin traitant = "absent"  (est parmi ["absent", "non_identifie_avec_certitude"])

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

<details>
<summary>🔍 Cas Mme Michu (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Michu ---

1. Extraction IA pour : 'Mme Michu, 82 ans, vit seule  Toulon dans son app...'

--- DEBUG : ANALYSE EXPERTE ---
Analyse manquante
Ville extraite : Toulon
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : non_renseigne
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
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "refus_aide_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
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

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION ---

=================================================================
  [ DAC - Refus de soins ou d'aide (Priorit Absolue) ]    Priorite : 105
=================================================================
  Objectif : Refus de soins ou opposition critique aux aides  domicile : Rupture critique de parcours ncessitant l'intervention immdiate du DAC pour dbloquer la situation.
  Contact  : 04 94 35 32 01 | None

  Pourquoi cette orientation :
    -> Motif principal de la demande = "refus_aide_domicile"  (est parmi ["refus_de_soins", "refus_aide_domicile"])

=================================================================
  [ CLIC - Centre Local d'Information et de Coordination (Snior) ]    Priorite : 80
=================================================================
  Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
  Contact  : 04 94 24 65 25 | None

  Pourquoi cette orientation :
    -> puisement de l'aidant = OUI  (est OUI)

=================================================================
  [ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ]    Priorite : 78
=================================================================
  Objectif : Maintien  domicile renforc et intensif : Alternative  l'EHPAD pour les situations en perte d'autonomie importante ou complexit technique.
  Contact  : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chnes 83500 LA SEYNE SUR MER

  Pourquoi cette orientation :
    -> puisement de l'aidant = OUI  (est OUI)

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

<details>
<summary>🔍 Cas Mr Petit (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Petit (Aidant Conjoint Epuis) ---

1. Extraction IA pour le rcit du conjoint aidant...

--- DEBUG : ANALYSE EXPERTE ---
Analyse manquante
Ville extraite : Toulon
Mdecin : identifie
Malveillance : aucune
Hospitalisation : aucun
tat Logement : insalubre
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
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "insalubre",
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
  "vulnerabilites.social.isolement_relationnel": null
}

2. Calcul du score de complexit COMID...
Score Total : 3 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- REPONSE D'ORIA POUR L'AIDANT ---
voici votre priorite :'

=================================================================
  [ PSCG SS APA - Ple Social de Solidarit et de Gestion (APA) ]    Priorite : 100
=================================================================
  Objectif : Contacter votre rfrent APA au Conseil Dpartemental (PSCG SS APA) pour toute modification de plan d'aide ou besoin d'accompagnement social supplmentaire.
  Contact  : 04 83 95 79 51 | None

  Pourquoi cette orientation :
    -> Statut APA = "oui"  (est "oui")

=================================================================
  [ CRT - Centre de Ressources Territorial (Accompagnement Renforc) ]    Priorite : 78
=================================================================
  Objectif : Maintien  domicile renforc et intensif : Alternative  l'EHPAD pour les situations en perte d'autonomie importante ou complexit technique.
  Contact  : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chnes 83500 LA SEYNE SUR MER

  Pourquoi cette orientation :
    -> puisement de l'aidant = OUI  (est OUI)

CONSEIL POUR VOUS : 'Prenez soin de vous egalement. En plus de votre referent APA, sachez que les plateformes de repit peuvent vous soutenir pendant votre hospitalisation.'

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

<details>
<summary>🔍 Cas Clarification And Validation (Détail des logs)</summary>

```text
--- Lancement du test : Moteur de Clarification & Validation Humaine ---

1. Rcit initial : 'Mme Antoinette, 82 ans, vit seule  La Garde. Son fils habite loin et ne peut pas l'aider. Elle a de grosses difficults  faire ses courses et  prparer ses repas. Elle refuse pour l'instant toute aide professionnelle  domicile.'

--- TAPE A : ANALYSE INITIALE (INFORMATIONS INCOMPLTES) ---

--- DEBUG : ANALYSE EXPERTE ---
Analyse manquante
Ville extraite : La Garde
Mdecin : incertain
Malveillance : aucune
Hospitalisation : aucun
tat Logement : non_renseigne
--- FIN DEBUG ---


[ DEBUG : extracted_data ]
{
  "usager.identite.age_estime": 82,
  "usager.localisation.commune_residence": "La Garde",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
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
Statut de l'analyse : en_attente_clarification

[ Orientations Suggres (Base IA) ] :
  - CLIC - Centre Local d'Information et de Coordination (Snior) (Priorit : 80)
  - UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) (Priorit : 70)

[ Questions de Clarification Gnres ] :
  [?] GIR (Niveau de dpendance) : Quel est le GIR (Groupe Iso-Ressources) estim ou officiel du patient (1  6) ?
      Impact : Un GIR entre 1 et 4 permet de valider l'ligibilit au CRT (Accompagnement Renforc) ou au DAC pour dpendance lourde.
  [?] Mdecin traitant : Le patient a-t-il un mdecin traitant identifi ?
      Impact : L'absence de mdecin traitant est ncessaire pour dclencher un accompagnement par la CPTS (accs aux soins).

--- TAPE B : APPLICATION DES CORRECTIONS HUMAINES (OVERRIDES) ---
Saisie du travailleur social : L'APA n'est pas encore en place ('non'), son GIR est estim  4, et elle n'a pas d'aidant rgulier ('non').

Nouveau Statut de l'analyse : en_attente_clarification

[ Orientations Affines & Valides ] :
  - CLIC - Centre Local d'Information et de Coordination (Snior) (Priorit : 80)
    Objectif : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
    Contact : 04 22 44 84 73 | None
  - UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) (Priorit : 70)
    Objectif : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
    Contact : 04 83 95 56 50 | 53 Impasse Blriot Immeuble Le Frdric 83130 La Garde

```

</details>

<details>
<summary>🔍 Cas Mr Chen (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Chen (PCH / Handicap) ---

1. Extraction IA pour : 'M. Chen, 52 ans, habite  Toulon. Il est en situat...'

--- DEBUG : ANALYSE EXPERTE ---
Analyse manquante
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
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "oui",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "inconnu",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": false,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": false,
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
  "vulnerabilites.social.isolement_relationnel": null
}

2. Calcul du score de complexit COMID...
Score Total : 1 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION (Cas Handicap / PCH) ---

=================================================================
  [ CLIC - Centre Local d'Information et de Coordination ]    Priorite : 102
=================================================================
  Objectif : Motifs d'orientation combins :
  - [Centre Local d'Information et de Coordination (Snior)] : Maintien  domicile : Information, valuation, ouverture des droits (APA, CARSAT) et aide administrative (impts, retraite). UNIQUEMENT si l'APA n'est pas dj en place.
  - [Centre Local d'Information et de Coordination (Exception PCH)] : Maintien  domicile : Accompagnement spcialis PCH (Prestation de Compensation du Handicap) pour les moins de 60 ans.
  Contact  : 04 94 24 65 25 | None

  Pourquoi cette orientation :
    -> Motif principal de la demande = "maintien_a_domicile"  (contient l'un de ["maintien_a_domicile", "renforcement_domicile", "aide_a_domicile", "information_aides", ... +3])
    -> Statut PCH = "oui"  (est "oui")

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

<details>
<summary>🔍 Cas Mme Morel (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Morel (Hpital) ---

1. Extraction IA pour : 'Mme Morel, 80 ans, est actuellement hospitalise ...'

--- DEBUG : ANALYSE EXPERTE ---
La patiente, ge de 80 ans, est hospitalise suite  une mauvaise chute. Elle s'inquite pour son retour  domicile car elle vit seule au 3me tage et a besoin d'aide pour organiser sa sortie et remplir ses dossiers administratifs. Elle a perdu ses papiers lors de son admission en urgence.
Ville extraite : None
Mdecin : incertain
Malveillance : aucune
Hospitalisation : en_cours
tat Logement : non_renseigne
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
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "en_cours",
  "demande.motif_principal": "sortie_hospitalisation",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
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

=================================================================
  [ Service Social de l'Hpital (Hospitalisation en cours) ]    Priorite : 95
=================================================================
  Objectif : Accompagnement social en milieu hospitalier : Organisation de la sortie et lien direct avec le service social de l'tablissement.
  Contact  : Non trouve dans le referentiel territorial

  Pourquoi cette orientation :
    -> Statut d'hospitalisation = "en_cours"  (est "en_cours")

=================================================================
  [ UTS / ASPI - Unit Territoriale Sociale (Action Sociale Prvention Insertion) ]    Priorite : 70
=================================================================
  Objectif : PAS (Premier Accueil Social) : valuation, ouverture de droits, aides financires ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
  Contact  : 04 83 95 24 42 | 100, traverse des minimes 83000 Toulon

  Pourquoi cette orientation :
    -> Prcarit financire = OUI  (est OUI)

BDD - Erreur de sauvegarde : table dossiers_patients has no column named details_complet

```

</details>

