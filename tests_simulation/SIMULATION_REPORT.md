# 📋 Rapport d'Évaluation Clinique ORIA

Généré automatiquement le : `2026-05-26 09:39:33`  
Nombre de cas exécutés : **20**  
Taux de succès : **20/20**  
Temps d'exécution total : **530.05 secondes**  

## 📊 Tableau récapitulatif des Orientations

| Patient | Status | Score COMID | Orientation Principale | Temps d'exécution |
| :--- | :---: | :---: | :--- | :---: |
| **Mme Huguette** | ✅ SUCCESS | 6 | `CCAS - Centre Communal d'Action Sociale` | 29.60s |
| **Mme Antoinette** | ✅ SUCCESS | 9 | `Service Social de l'Hôpital` | 27.05s |
| **Mme Rossi** | ✅ SUCCESS | 6 | `N/A` | 24.38s |
| **Mme Martin** | ✅ SUCCESS | 5 | `CRT - Centre de Ressources Territorial (Volet 2 - Accompagnement Renforcé)` | 25.43s |
| **Mme Durand** | ✅ SUCCESS | 7 | `N/A` | 25.99s |
| **Mme Michu** | ✅ SUCCESS | 4 | `N/A` | 25.19s |
| **Mr Martin** | ✅ SUCCESS | 5 | `CCAS - Centre Communal d'Action Sociale` | 25.98s |
| **Mme Vial** | ✅ SUCCESS | 4 | `N/A` | 26.99s |
| **Mme Morel** | ✅ SUCCESS | 2 | `N/A` | 26.08s |
| **Mr Petit** | ✅ SUCCESS | 6 | `CRT - Centre de Ressources Territorial (Volet 2 - Accompagnement Renforcé)` | 24.75s |
| **Mr Chen** | ✅ SUCCESS | 5 | `CCAS - Centre Communal d'Action Sociale` | 27.23s |
| **Mme Fontaine** | ✅ SUCCESS | 5 | `N/A` | 25.98s |
| **Mme Mouton** | ✅ SUCCESS | 7 | `N/A` | 27.57s |
| **Mr Vacek** | ✅ SUCCESS | 7 | `CEV - Cellule Écoute et Vigilance (Urgence & Danger)` | 26.28s |
| **Mr Dubois** | ✅ SUCCESS | 8 | `N/A` | 26.64s |
| **Mme Bernard** | ✅ SUCCESS | 7 | `CCAS - Centre Communal d'Action Sociale` | 27.62s |
| **Mme Petit** | ✅ SUCCESS | 2 | `CCAS - Centre Communal d'Action Sociale` | 25.16s |
| **Mme Lefebvre** | ✅ SUCCESS | 8 | `Service Social de l'Hôpital` | 30.27s |
| **Mr Lambert** | ✅ SUCCESS | 7 | `N/A` | 26.06s |
| **Mr Leroy** | ✅ SUCCESS | 10 | `CCAS - Centre Communal d'Action Sociale` | 25.79s |

---

## 📝 Détail des extractions et raisonnements

<details>
<summary>🔍 Cas Mme Huguette (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Huguette (Urgence Sociale / Protection) ---

1. Extraction IA (Temp=0.0) pour : 'Mme Huguette, 79 ans, vit seule dans un logement insalubre et humide à La Valett...'

--- DEBUG : ANALYSE EXPERTE ---
Situation de Mme H. : solitude, mauvaise santé financière et risque de malveillance.
Ville extraite : La Valette du Var
Médecin : absent
Malveillance : spoliation_financiere
Hospitalisation : None
--- FIN DEBUG ---

Données extraites (JSON) :
{
  "usager.identite.age_estime": 79,
  "usager.localisation.commune_residence": "La Valette du Var",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "spoliation_financiere",
  "adresseur.degre_urgence_percu": "critique",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "secours_urgence",
  "vulnerabilites.sante.professionnels_domicile": "inconnu",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": true,
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
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": true,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": true,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexité COMID...
Score Total : 6 (Situation à risque de complexité)

3. Évaluation de l'orientation...

4. Recherche des contacts territoriaux (La Valette)...

--- RÉSULTATS DE L'ORIENTATION POUR MME HUGUETTE ---

[ CEV - Cellule Écoute et Vigilance (Urgence & Danger) ] - Priorité : 95
Objectif : protection_et_mise_en_securite (Peut faire l'objet d'un signalement au pénal avec copie au Procureur de la République)
Contact : 04 83 95 16 01 | None

[ DAC - Dispositif d'Appui à la Coordination (Dernier Recours) ] - Priorité : 85
Objectif : Coordination de haut niveau : Évaluation multidimensionnelle et déblocage de situations complexes (sanitaire, social, médico-social). Plan Personnalisé de Coordination.
Contact : 04 94 35 32 01 | None

[ CLIC - Centre Local d'Information et de Coordination ] - Priorité : 80
Objectif : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : 04 22 44 84 73 | None

[ UTS / ASPI - Unité Territoriale Sociale (Action Sociale Prévention Insertion) ] - Priorité : 70
Objectif : PAS (Premier Accueil Social) : Évaluation, ouverture de droits, aides financières ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
Contact : 04 83 95 56 90 | 427 Avenue Duchatel 83130 La Valette du Var

[ CPTS - Communauté Professionnelle Territoriale de Santé ] - Priorité : 65
Objectif : Accès aux soins : Recherche de médecin traitant (justifiée par retraite/déménagement) et dispositif MISAS pour éviter le renoncement aux soins.
Contact : 06 63 63 63 91 | 3 Rue Aspirant François Philippe 83260 La Crau

[ CCAS - Centre Communal d'Action Sociale ] - Priorité : 60
Objectif : Information et premier accueil social : Se renseigner sur les aides légales (RSA), les secours d'urgence (alimentaire, factures) et les logements seniors de la commune.
Contact : 04 94 20 92 70 | place Général de Gaulle 83160 la Valette du Var

```

</details>

<details>
<summary>🔍 Cas Mme Antoinette (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Antoinette (Nouveau Cas Complexe) ---

1. Extraction IA (Déterministe, Temp=0.0) pour : 'Mme Antoinette, 92 ans, réside à La Garde. Elle vit avec son mari M. Pierre (89 ...'

--- DEBUG : ANALYSE EXPERTE ---
Situation de Mme A. dégradée, opposition aux soins et risques de chute.
Ville extraite : La Garde
Médecin : identifie
Malveillance : negligence
Hospitalisation : recente
--- FIN DEBUG ---

Données extraites (JSON) :
{
  "usager.identite.age_estime": 92,
  "usager.localisation.commune_residence": "La Garde",
  "usager.situation_actuelle.APA": "oui",
  "usager.situation_actuelle.PCH": "en_cours",
  "usager.situation_actuelle.GIR": 2,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "negligence",
  "adresseur.degre_urgence_percu": "eleve",
  "vulnerabilites.sante.hospitalisation.statut": "recente",
  "demande.motif_principal": "opposition_soins",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "oui",
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
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
  "evaluation.comid.sollicitations_recurrentes": true,
  "evaluation.comid.conflit_reseau": true,
  "evaluation.comid.inquietude_sante": true,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": true,
  "evaluation.comid.degradation_recente": true,
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

2. Calcul du score de complexité COMID...
Score Total : 9 (Situation à risque de complexité)

3. Évaluation de l'orientation...

4. Recherche des contacts territoriaux (La Garde)...

--- RÉSULTATS DE L'ORIENTATION POUR MME ANTOINETTE ---

[ PSCG SS APA - Pôle Social de Solidarité et de Gestion (APA) ] - Priorité : 100
Objectif : Contacter votre référent APA au Conseil Départemental (PSCG SS APA) pour toute modification de plan d'aide ou besoin d'accompagnement social supplémentaire.
Contact : 04 83 95 79 51 | None

[ CEV - Cellule Écoute et Vigilance (Urgence & Danger) ] - Priorité : 95
Objectif : protection_et_mise_en_securite (Peut faire l'objet d'un signalement au pénal avec copie au Procureur de la République)
Contact : 04 83 95 16 01 | None

[ Service Social de l'Hôpital ] - Priorité : 95
Objectif : Accompagnement social en milieu hospitalier : Organisation de la sortie, aide aux démarches et lien avec les services extérieurs.
Contact : Non trouvé dans le référentiel territorial

[ CRT - Centre de Ressources Territorial (Volet 2 - Accompagnement Renforcé) ] - Priorité : 90
Objectif : Maintien à domicile renforcé : Alternative à l'EHPAD pour les situations en perte d'autonomie importante ou complexité technique.
Contact : 06 83 38 39 39 | 421 Av 1er Bataillon Infanterie de Marine du Pacifique 83130 La Garde

[ DAC - Dispositif d'Appui à la Coordination (Dernier Recours) ] - Priorité : 85
Objectif : Coordination de haut niveau : Évaluation multidimensionnelle et déblocage de situations complexes (sanitaire, social, médico-social). Plan Personnalisé de Coordination.
Contact : 04 94 35 32 01 | None

[ CPTS - Communauté Professionnelle Territoriale de Santé ] - Priorité : 65
Objectif : Accès aux soins : Recherche de médecin traitant (justifiée par retraite/déménagement) et dispositif MISAS pour éviter le renoncement aux soins.
Contact : 06 63 63 63 91 | 3 Rue Aspirant François Philippe 83260 La Crau

```

</details>

<details>
<summary>🔍 Cas Mme Rossi (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Rossi (Violences Conjugales) ---

1. Extraction IA pour : 'Mme Rossi, 70 ans, habite à Toulon. Elle vient d'a...'

--- DEBUG : ANALYSE EXPERTE ---
Situation de violence conjugale
Ville extraite : Toulon
Médecin : absent
Malveillance : violences_physiques
Hospitalisation : None
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 70,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": 4,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "violences_physiques",
  "adresseur.degre_urgence_percu": "critique",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maltraitance",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": false,
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
  "evaluation.comid.anxiete": true,
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
  "evaluation.comid.probleme_assurance": true,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": null
}

2. Calcul du score de complexité COMID...
Score Total : 6 (Situation à risque de complexité)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION (Protection / Violences) ---

[ CEV - Cellule Écoute et Vigilance (Urgence & Danger) ] - Priorite : 95
Objectif : protection_et_mise_en_securite (Peut faire l'objet d'un signalement au pénal avec copie au Procureur de la République)
Contact : 04 83 95 16 01 | None

[ CRT - Centre de Ressources Territorial (Volet 2 - Accompagnement Renforcé) ] - Priorite : 90
Objectif : Maintien à domicile renforcé : Alternative à l'EHPAD pour les situations en perte d'autonomie importante ou complexité technique.
Contact : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chênes 83500 LA SEYNE SUR MER

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 80
Objectif : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : 04 94 24 65 25 | None

[ UTS / ASPI - Unité Territoriale Sociale (Action Sociale Prévention Insertion) ] - Priorite : 70
Objectif : PAS (Premier Accueil Social) : Évaluation, ouverture de droits, aides financières ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
Contact : 04 83 95 24 42 | 100, traverse des minimes 83000 Toulon

[ CPTS - Communauté Professionnelle Territoriale de Santé ] - Priorite : 65
Objectif : Accès aux soins : Recherche de médecin traitant (justifiée par retraite/déménagement) et dispositif MISAS pour éviter le renoncement aux soins.
Contact : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

```

</details>

<details>
<summary>🔍 Cas Mme Martin (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Martin (Détresse Aidant) ---

1. Extraction IA pour le récit de l'aidante...

--- DEBUG : ANALYSE EXPERTE ---
Mémoire de la mère fragile, dépendance croissante.
Ville extraite : Toulon
Médecin : absent
Malveillance : aucune
Hospitalisation : None
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 82,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": 4,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "recherche_medecin",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
  "evaluation.comid.troubles_cognitifs": false,
  "evaluation.comid.precarite_financiere": false,
  "evaluation.comid.epuisement_aidant": false,
  "evaluation.comid.litteratie_faible": false,
  "evaluation.comid.isolement_social": false,
  "evaluation.comid.logement_inadapte": false,
  "evaluation.comid.depression": true,
  "evaluation.comid.psychiatrie": false,
  "evaluation.comid.addiction": false,
  "evaluation.comid.anxiete": false,
  "evaluation.comid.fluctuation_mentale": false,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": true,
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
  "vulnerabilites.social.isolement_relationnel": null
}

2. Calcul du score de complexité COMID...
Score Total : 5 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- REPONSE D'ORIA POUR L'AIDANTE ---
ORIA : 'Je comprends votre épuisement. La situation de votre mère est Situation non complexe.'

VOTRE PRIORITÉ ABSOLUE : [ CRT - Centre de Ressources Territorial (Volet 2 - Accompagnement Renforcé) ]
MISSION : Maintien à domicile renforcé : Alternative à l'EHPAD pour les situations en perte d'autonomie importante ou complexité technique.
CONTACT : 06 84 99 32 49

```

</details>

<details>
<summary>🔍 Cas Mme Durand (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Durand ---

1. Extraction IA pour : 'Mme Durand, 88 ans, vit à Hyères. Elle est très co...'

--- DEBUG : ANALYSE EXPERTE ---
Situation critique, risque de blessure ou de mort
Ville extraite : Hyères
Médecin : absent
Malveillance : violences_physiques
Hospitalisation : None
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 88,
  "usager.localisation.commune_residence": "Hyères",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "violences_physiques",
  "adresseur.degre_urgence_percu": "critique",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "recherche_medecin",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
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
  "evaluation.comid.fluctuation_mentale": true,
  "evaluation.comid.sollicitations_recurrentes": false,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": true,
  "evaluation.comid.opposition_soins": true,
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
  "vulnerabilites.social.isolement_relationnel": null
}

2. Calcul du score de complexité COMID...
Score Total : 7 (Situation à risque de complexité)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Hyères)...

--- RESULTATS DE L'ORIENTATION ---

[ CEV - Cellule Écoute et Vigilance (Urgence & Danger) ] - Priorite : 95
Objectif : protection_et_mise_en_securite (Peut faire l'objet d'un signalement au pénal avec copie au Procureur de la République)
Contact : Non trouve dans le referentiel territorial

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 80
Objectif : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : Non trouve dans le referentiel territorial

[ CPTS - Communauté Professionnelle Territoriale de Santé ] - Priorite : 65
Objectif : Accès aux soins : Recherche de médecin traitant (justifiée par retraite/déménagement) et dispositif MISAS pour éviter le renoncement aux soins.
Contact : Non trouve dans le referentiel territorial

```

</details>

<details>
<summary>🔍 Cas Mme Michu (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Michu ---

1. Extraction IA pour : 'Mme Michu, 82 ans, vit seule à Toulon dans son app...'

--- DEBUG : ANALYSE EXPERTE ---
Mme M. présente des difficultés de santé et d'aide à domicile.
Ville extraite : Toulon
Médecin : absent
Malveillance : aucune
Hospitalisation : None
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 82,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": 4,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "recherche_medecin",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
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
  "evaluation.comid.sollicitations_recurrentes": true,
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

2. Calcul du score de complexité COMID...
Score Total : 4 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION ---

[ CRT - Centre de Ressources Territorial (Volet 2 - Accompagnement Renforcé) ] - Priorite : 90
Objectif : Maintien à domicile renforcé : Alternative à l'EHPAD pour les situations en perte d'autonomie importante ou complexité technique.
Contact : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chênes 83500 LA SEYNE SUR MER

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 80
Objectif : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : 04 94 24 65 25 | None

[ CPTS - Communauté Professionnelle Territoriale de Santé ] - Priorite : 65
Objectif : Accès aux soins : Recherche de médecin traitant (justifiée par retraite/déménagement) et dispositif MISAS pour éviter le renoncement aux soins.
Contact : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

```

</details>

<details>
<summary>🔍 Cas Mr Martin (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Martin ---

1. Extraction IA pour : 'M. Martin, 75 ans, habite à La Seyne-sur-Mer. Il a...'

--- DEBUG : ANALYSE EXPERTE ---
Situation critique de M. M.
Ville extraite : La Seyne-sur-Mer
Médecin : absent
Malveillance : aucune
Hospitalisation : None
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 75,
  "usager.localisation.commune_residence": "La Seyne-sur-Mer",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "critique",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "secours_urgence",
  "vulnerabilites.sante.professionnels_domicile": "inconnu",
  "usager.cadre_de_vie.aidant_regulier": "aucun",
  "evaluation.comid.multimorbidite": false,
  "evaluation.comid.douleurs": true,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
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
  "evaluation.comid.inquietude_sante": true,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": true,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexité COMID...
Score Total : 5 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (La Seyne-sur-Mer)...

--- RESULTATS DE L'ORIENTATION ---

[ CEV - Cellule Écoute et Vigilance (Urgence & Danger) ] - Priorite : 95
Objectif : protection_et_mise_en_securite (Peut faire l'objet d'un signalement au pénal avec copie au Procureur de la République)
Contact : 04 83 95 16 01 | None

[ DAC - Dispositif d'Appui à la Coordination (Dernier Recours) ] - Priorite : 85
Objectif : Coordination de haut niveau : Évaluation multidimensionnelle et déblocage de situations complexes (sanitaire, social, médico-social). Plan Personnalisé de Coordination.
Contact : 04 94 35 32 01 | None

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 80
Objectif : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : 04 94 06 97 04 | None

[ CPTS - Communauté Professionnelle Territoriale de Santé ] - Priorite : 65
Objectif : Accès aux soins : Recherche de médecin traitant (justifiée par retraite/déménagement) et dispositif MISAS pour éviter le renoncement aux soins.
Contact : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

[ CCAS - Centre Communal d'Action Sociale ] - Priorite : 60
Objectif : Information et premier accueil social : Se renseigner sur les aides légales (RSA), les secours d'urgence (alimentaire, factures) et les logements seniors de la commune.
Contact : 04 94 06 97 18 | Espace Hermès 2 avenue Charles-Gide 83500 La Seyne-sur-Mer

```

</details>

<details>
<summary>🔍 Cas Mme Vial (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Vial (Recherche Médecin Traitant) ---

1. Extraction IA pour : 'Mme Vial, 82 ans, vient de s'installer à Toulon po...'

--- DEBUG : ANALYSE EXPERTE ---
Mme V. a besoin d'un suivi médical régulier.
Ville extraite : Toulon
Médecin : absent
Malveillance : aucune
Hospitalisation : None
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 82,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": 4,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "recherche_medecin",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
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
  "evaluation.comid.inquietude_sante": true,
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

2. Calcul du score de complexité COMID...
Score Total : 4 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux...
Ville extraite par l'IA : Toulon

--- RESULTATS DE L'ORIENTATION (Territoire: Toulon - Canton 1, 2 et 3) ---

[ CRT - Centre de Ressources Territorial (Volet 2 - Accompagnement Renforcé) ] - Priorite : 90
Objectif : Maintien à domicile renforcé : Alternative à l'EHPAD pour les situations en perte d'autonomie importante ou complexité technique.
Contact : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chênes 83500 LA SEYNE SUR MER

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 80
Objectif : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : 04 94 24 65 25 | None

[ CPTS - Communauté Professionnelle Territoriale de Santé ] - Priorite : 65
Objectif : Accès aux soins : Recherche de médecin traitant (justifiée par retraite/déménagement) et dispositif MISAS pour éviter le renoncement aux soins.
Contact : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

```

</details>

<details>
<summary>🔍 Cas Mme Morel (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Morel (Hôpital) ---

1. Extraction IA pour : 'Mme Morel, 80 ans, est actuellement hospitalisée à...'

--- DEBUG : ANALYSE EXPERTE ---
Mme M. a besoin d'aide pour organiser sa sortie et remplir ses dossiers administratifs.
Ville extraite : Toulon
Médecin : absent
Malveillance : aucune
Hospitalisation : None
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 82,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": 4,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "recherche_medecin",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
  "evaluation.comid.troubles_cognitifs": false,
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

2. Calcul du score de complexité COMID...
Score Total : 2 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION (Hopital Sainte Musse) ---

[ CRT - Centre de Ressources Territorial (Volet 2 - Accompagnement Renforcé) ] - Priorite : 90
Objectif : Maintien à domicile renforcé : Alternative à l'EHPAD pour les situations en perte d'autonomie importante ou complexité technique.
Contact : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chênes 83500 LA SEYNE SUR MER

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 80
Objectif : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : 04 94 24 65 25 | None

[ CPTS - Communauté Professionnelle Territoriale de Santé ] - Priorite : 65
Objectif : Accès aux soins : Recherche de médecin traitant (justifiée par retraite/déménagement) et dispositif MISAS pour éviter le renoncement aux soins.
Contact : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

```

</details>

<details>
<summary>🔍 Cas Mr Petit (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Petit (Aidant Conjoint Epuisé) ---

1. Extraction IA pour le récit du conjoint aidant...

--- DEBUG : ANALYSE EXPERTE ---
Résumé de la situation de M. P.
Ville extraite : Toulon
Médecin : absent
Malveillance : aucune
Hospitalisation : None
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 82,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": 4,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "recherche_medecin",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
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
  "evaluation.comid.inquietude_sante": true,
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
  "vulnerabilites.social.isolement_relationnel": null
}

2. Calcul du score de complexité COMID...
Score Total : 6 (Situation à risque de complexité)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- REPONSE D'ORIA POUR L'AIDANT ---
voici votre priorité :'

VOTRE PRIORITÉ ABSOLUE : [ CRT - Centre de Ressources Territorial (Volet 2 - Accompagnement Renforcé) ]
MISSION : Maintien à domicile renforcé : Alternative à l'EHPAD pour les situations en perte d'autonomie importante ou complexité technique.
CONTACT : 06 84 99 32 49

CONSEIL POUR VOUS : 'Prenez soin de vous également. En plus de votre référent APA, sachez que les plateformes de répit peuvent vous soutenir pendant votre hospitalisation.'

```

</details>

<details>
<summary>🔍 Cas Mr Chen (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Chen (PCH / Handicap) ---

1. Extraction IA pour : 'M. Chen, 52 ans, habite à Toulon. Il est en situat...'

--- DEBUG : ANALYSE EXPERTE ---
Personne en situation de handicap moteur à Toulon
Ville extraite : Toulon
Médecin : identifie
Malveillance : aucune
Hospitalisation : aucun
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 52,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "oui",
  "usager.situation_actuelle.PCH": "oui",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "identifie",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "faible",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "information_aides",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "inconnu",
  "evaluation.comid.multimorbidite": false,
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
  "evaluation.comid.inquietude_sante": true,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": true,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexité COMID...
Score Total : 5 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION (Cas Handicap / PCH) ---

[ PSCG SS APA - Pôle Social de Solidarité et de Gestion (APA) ] - Priorite : 100
Objectif : Contacter votre référent APA au Conseil Départemental (PSCG SS APA) pour toute modification de plan d'aide ou besoin d'accompagnement social supplémentaire.
Contact : 04 83 95 79 51 | None

[ DAC - Dispositif d'Appui à la Coordination (Dernier Recours) ] - Priorite : 85
Objectif : Coordination de haut niveau : Évaluation multidimensionnelle et déblocage de situations complexes (sanitaire, social, médico-social). Plan Personnalisé de Coordination.
Contact : 04 94 35 32 01 | None

[ CCAS - Centre Communal d'Action Sociale ] - Priorite : 60
Objectif : Information et premier accueil social : Se renseigner sur les aides légales (RSA), les secours d'urgence (alimentaire, factures) et les logements seniors de la commune.
Contact : 04 94 24 65 00 | 100 rue des remparts - CS 20813 83051 Toulon Cedex

```

</details>

<details>
<summary>🔍 Cas Mme Fontaine (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Fontaine (Alerte Kiné) ---

1. Extraction IA pour l'alerte du kiné...

--- DEBUG : ANALYSE EXPERTE ---
Mme F. présente des difficultés financières et une situation de malveillance.
Ville extraite : Sanary
Médecin : absent
Malveillance : spoliation_financiere
Hospitalisation : None
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 82,
  "usager.localisation.commune_residence": "Sanary",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": 4,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "spoliation_financiere",
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "recherche_medecin",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": false,
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
  "evaluation.comid.sollicitations_recurrentes": true,
  "evaluation.comid.conflit_reseau": false,
  "evaluation.comid.inquietude_sante": false,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": true,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": null
}

2. Calcul du score de complexité COMID...
Score Total : 5 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Sanary-sur-Mer)...

--- REPONSE D'ORIA POUR LE KINE ---
ORIA : 'Situation identifiée comme Situation non complexe. Voici les actions prioritaires :'

ACTION : [ CEV - Cellule Écoute et Vigilance (Urgence & Danger) ]
MOTIF : protection_et_mise_en_securite (Peut faire l'objet d'un signalement au pénal avec copie au Procureur de la République)
CONTACT : 04 83 95 16 01

ACTION : [ CRT - Centre de Ressources Territorial (Volet 2 - Accompagnement Renforcé) ]
MOTIF : Maintien à domicile renforcé : Alternative à l'EHPAD pour les situations en perte d'autonomie importante ou complexité technique.
CONTACT : 06 84 99 32 49

ACTION : [ UTS Littoral Sud Sainte Baume - SANARY (Relais CLIC) ]
MOTIF : La commune ne dispose pas de CLIC, se rapprocher de l'UTS. Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
CONTACT : 04 83 95 83 10

ACTION : [ UTS / ASPI - Unité Territoriale Sociale (Action Sociale Prévention Insertion) ]
MOTIF : PAS (Premier Accueil Social) : Évaluation, ouverture de droits, aides financières ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
CONTACT : 04 83 95 83 10

ACTION : [ CPTS - Communauté Professionnelle Territoriale de Santé ]
MOTIF : Accès aux soins : Recherche de médecin traitant (justifiée par retraite/déménagement) et dispositif MISAS pour éviter le renoncement aux soins.
CONTACT : 06 44 18 95 44

```

</details>

<details>
<summary>🔍 Cas Mme Mouton (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Georgette Mouton (Ollioules) ---

1. Extraction IA pour : 'Mme Georgette Mouton, 83 ans, vit seule à Ollioules dans un appartement devenu e...'

--- DEBUG : ANALYSE EXPERTE ---
Mme G. M. vit seule dans un logement inadapté avec risque de chute et fréquents oublis de médicaments.
Ville extraite : Ollioules
Médecin : absent
Malveillance : negligence
Hospitalisation : None
--- FIN DEBUG ---

Données extraites (JSON) :
{
  "usager.identite.age_estime": 83,
  "usager.localisation.commune_residence": "Ollioules",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": 4,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "negligence",
  "adresseur.degre_urgence_percu": "critique",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "sortie_hospitalisation",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "aucun",
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
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
  "evaluation.comid.inquietude_sante": true,
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
  "evaluation.comid.lourdeur_reseau": true,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexité COMID...
Score Total : 7 (Situation à risque de complexité)

3. Évaluation de l'orientation...

4. Recherche des contacts territoriaux (Ollioules)...

--- RÉSULTATS DE L'ORIENTATION POUR MME GEORGETTE MOUTON ---

[ CEV - Cellule Écoute et Vigilance (Urgence & Danger) ] - Priorité : 95
Objectif : protection_et_mise_en_securite (Peut faire l'objet d'un signalement au pénal avec copie au Procureur de la République)
Contact : 04 83 95 16 01 | None

[ CRT - Centre de Ressources Territorial (Volet 2 - Accompagnement Renforcé) ] - Priorité : 90
Objectif : Maintien à domicile renforcé : Alternative à l'EHPAD pour les situations en perte d'autonomie importante ou complexité technique.
Contact : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chênes 83500 LA SEYNE SUR MER

[ DAC - Dispositif d'Appui à la Coordination (Dernier Recours) ] - Priorité : 85
Objectif : Coordination de haut niveau : Évaluation multidimensionnelle et déblocage de situations complexes (sanitaire, social, médico-social). Plan Personnalisé de Coordination.
Contact : 04 94 35 32 01 | None

[ UTS Littoral Sud Sainte Baume - OLLIOULES (Relais CLIC) ] - Priorité : 80
Objectif : La commune ne dispose pas de CLIC, se rapprocher de l'UTS. Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : 04 83 95 58 50 | Espace Pierre Puget 2 Place Marius Trotobas 83190 Ollioules

[ CPTS - Communauté Professionnelle Territoriale de Santé ] - Priorité : 65
Objectif : Accès aux soins : Recherche de médecin traitant (justifiée par retraite/déménagement) et dispositif MISAS pour éviter le renoncement aux soins.
Contact : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

```

</details>

<details>
<summary>🔍 Cas Mr Vacek (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Vacek (Habitat Indigne & Danger) ---

1. Extraction IA pour la situation de péril...

--- DEBUG : ANALYSE EXPERTE ---
Situation critique de santé et sécurité
Ville extraite : Toulon
Médecin : absent
Malveillance : negligence
Hospitalisation : recente
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 65,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": 4,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "negligence",
  "adresseur.degre_urgence_percu": "critique",
  "vulnerabilites.sante.hospitalisation.statut": "recente",
  "demande.motif_principal": "secours_urgence",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "aucun",
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
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
  "evaluation.comid.inquietude_sante": true,
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
  "evaluation.comid.probleme_assurance": true,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": null
}

2. Calcul du score de complexité COMID...
Score Total : 7 (Situation à risque de complexité)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- REPONSE D'ORIA (URGENCE HABITAT) ---
ORIA : 'La situation de M. Vacek présente un DANGER IMMINENT.'

VOTRE PRIORITÉ ABSOLUE : [ CEV - Cellule Écoute et Vigilance (Urgence & Danger) ]
MISSION : protection_et_mise_en_securite (Peut faire l'objet d'un signalement au pénal avec copie au Procureur de la République)
CONTACT : 04 83 95 16 01

ENSUITE (VOLET SOCIAL) : [ Service Social de l'Hôpital ]
MISSION : Accompagnement social en milieu hospitalier : Organisation de la sortie, aide aux démarches et lien avec les services extérieurs.

```

</details>

<details>
<summary>🔍 Cas Mr Dubois (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Dubois ---

1. Extraction IA pour : 'M. Dubois, 74 ans, vit à Toulon. Il souffre de dia...'

--- DEBUG : ANALYSE EXPERTE ---
Personne vulnérable, besoin d'aide médicale et sociale.
Ville extraite : Toulon
Médecin : absent
Malveillance : aucune
Hospitalisation : aucun
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 74,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "inconnu",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": true,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
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
  "evaluation.comid.inquietude_sante": true,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": false,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": true,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": null
}

2. Calcul du score de complexité COMID...
Score Total : 8 (Situation à risque de complexité)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION ---

[ CRT - Centre de Ressources Territorial (Volet 2 - Accompagnement Renforcé) ] - Priorite : 90
Objectif : Maintien à domicile renforcé : Alternative à l'EHPAD pour les situations en perte d'autonomie importante ou complexité technique.
Contact : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chênes 83500 LA SEYNE SUR MER

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 80
Objectif : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : 04 94 24 65 25 | None

[ UTS / ASPI - Unité Territoriale Sociale (Action Sociale Prévention Insertion) ] - Priorite : 70
Objectif : PAS (Premier Accueil Social) : Évaluation, ouverture de droits, aides financières ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
Contact : 04 83 95 24 42 | 100, traverse des minimes 83000 Toulon

[ CPTS - Communauté Professionnelle Territoriale de Santé ] - Priorite : 65
Objectif : Accès aux soins : Recherche de médecin traitant (justifiée par retraite/déménagement) et dispositif MISAS pour éviter le renoncement aux soins.
Contact : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

```

</details>

<details>
<summary>🔍 Cas Mme Bernard (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Bernard (Suspicion de maltraitance) ---

1. Extraction IA pour : 'Mme Bernard, 88 ans, habite à La Seyne-sur-Mer. El...'

--- DEBUG : ANALYSE EXPERTE ---
Mme B. est isolée et victime de vol d'argent, avec dégradation santé récente.
Ville extraite : La Seyne-sur-Mer
Médecin : absent
Malveillance : spoliation_financiere
Hospitalisation : None
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 88,
  "usager.localisation.commune_residence": "La Seyne-sur-Mer",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "spoliation_financiere",
  "adresseur.degre_urgence_percu": "critique",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "secours_urgence",
  "vulnerabilites.sante.professionnels_domicile": "inconnu",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
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
  "evaluation.comid.inquietude_sante": true,
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
  "evaluation.comid.lourdeur_reseau": true,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexité COMID...
Score Total : 7 (Situation à risque de complexité)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux...
Ville extraite par l'IA : La Seyne-sur-Mer

--- RESULTATS DE L'ORIENTATION (Territoire: La Seyne-sur-mer) ---

[ CEV - Cellule Écoute et Vigilance (Urgence & Danger) ] - Priorite : 95
Objectif : protection_et_mise_en_securite (Peut faire l'objet d'un signalement au pénal avec copie au Procureur de la République)
Contact : 04 83 95 16 01 | None

[ DAC - Dispositif d'Appui à la Coordination (Dernier Recours) ] - Priorite : 85
Objectif : Coordination de haut niveau : Évaluation multidimensionnelle et déblocage de situations complexes (sanitaire, social, médico-social). Plan Personnalisé de Coordination.
Contact : 04 94 35 32 01 | None

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 80
Objectif : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : 04 94 06 97 04 | None

[ UTS / ASPI - Unité Territoriale Sociale (Action Sociale Prévention Insertion) ] - Priorite : 70
Objectif : PAS (Premier Accueil Social) : Évaluation, ouverture de droits, aides financières ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
Contact : 04 83 95 48 30 ou 04 83 95 37 99 | rue Charles Gide 83500 La Seyne sur mer

[ CPTS - Communauté Professionnelle Territoriale de Santé ] - Priorite : 65
Objectif : Accès aux soins : Recherche de médecin traitant (justifiée par retraite/déménagement) et dispositif MISAS pour éviter le renoncement aux soins.
Contact : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

[ CCAS - Centre Communal d'Action Sociale ] - Priorite : 60
Objectif : Information et premier accueil social : Se renseigner sur les aides légales (RSA), les secours d'urgence (alimentaire, factures) et les logements seniors de la commune.
Contact : 04 94 06 97 18 | Espace Hermès 2 avenue Charles-Gide 83500 La Seyne-sur-Mer

```

</details>

<details>
<summary>🔍 Cas Mme Petit (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Petit (Urgence CCAS) ---

1. Extraction IA pour : 'Mme Petit, 78 ans, habite à La Garde. Elle vit seu...'

--- DEBUG : ANALYSE EXPERTE ---
Mme P. est en situation de précarité financière et d'isolement social.
Ville extraite : La Garde
Médecin : inconnu
Malveillance : aucune
Hospitalisation : None
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 78,
  "usager.localisation.commune_residence": "La Garde",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "inconnu",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "critique",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "aide_alimentaire",
  "vulnerabilites.sante.professionnels_domicile": "inconnu",
  "usager.cadre_de_vie.aidant_regulier": "aucun",
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

2. Calcul du score de complexité COMID...
Score Total : 2 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (La Garde)...

--- RESULTATS DE L'ORIENTATION (Territoire: La Garde) ---

[ CEV - Cellule Écoute et Vigilance (Urgence & Danger) ] - Priorite : 95
Objectif : protection_et_mise_en_securite (Peut faire l'objet d'un signalement au pénal avec copie au Procureur de la République)
Contact : 04 83 95 16 01 | None

[ DAC - Dispositif d'Appui à la Coordination (Dernier Recours) ] - Priorite : 85
Objectif : Coordination de haut niveau : Évaluation multidimensionnelle et déblocage de situations complexes (sanitaire, social, médico-social). Plan Personnalisé de Coordination.
Contact : 04 94 35 32 01 | None

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 80
Objectif : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : 04 22 44 84 73 | None

[ UTS / ASPI - Unité Territoriale Sociale (Action Sociale Prévention Insertion) ] - Priorite : 70
Objectif : PAS (Premier Accueil Social) : Évaluation, ouverture de droits, aides financières ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
Contact : 04 83 95 56 50 | 53 Impasse Blériot Immeuble Le Frédéric 83130 La Garde

[ CPTS - Communauté Professionnelle Territoriale de Santé ] - Priorite : 65
Objectif : Accès aux soins : Recherche de médecin traitant (justifiée par retraite/déménagement) et dispositif MISAS pour éviter le renoncement aux soins.
Contact : 06 63 63 63 91 | 3 Rue Aspirant François Philippe 83260 La Crau

[ CCAS - Centre Communal d'Action Sociale ] - Priorite : 60
Objectif : Information et premier accueil social : Se renseigner sur les aides légales (RSA), les secours d'urgence (alimentaire, factures) et les logements seniors de la commune.
Contact : 04 94 08 98 34 | 81 Rue Marius Tardivier 83130 La garde

```

</details>

<details>
<summary>🔍 Cas Mme Lefebvre (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Lefebvre ---

1. Extraction IA pour : 'Mme Lefebvre, 65 ans, vit à La Garde. Elle est sui...'

--- DEBUG : ANALYSE EXPERTE ---
Situation critique, risque de dégradation
Ville extraite : La Garde
Médecin : absent
Malveillance : aucune
Hospitalisation : recente
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
  "adresseur.degre_urgence_percu": "critique",
  "vulnerabilites.sante.hospitalisation.statut": "recente",
  "demande.motif_principal": "secours_urgence",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
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

2. Calcul du score de complexité COMID...
Score Total : 8 (Situation à risque de complexité)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (La Garde)...

--- RESULTATS DE L'ORIENTATION ---

[ CEV - Cellule Écoute et Vigilance (Urgence & Danger) ] - Priorite : 95
Objectif : protection_et_mise_en_securite (Peut faire l'objet d'un signalement au pénal avec copie au Procureur de la République)
Contact : 04 83 95 16 01 | None

[ Service Social de l'Hôpital ] - Priorite : 95
Objectif : Accompagnement social en milieu hospitalier : Organisation de la sortie, aide aux démarches et lien avec les services extérieurs.
Contact : Non trouve dans le referentiel territorial

[ DAC - Dispositif d'Appui à la Coordination (Dernier Recours) ] - Priorite : 85
Objectif : Coordination de haut niveau : Évaluation multidimensionnelle et déblocage de situations complexes (sanitaire, social, médico-social). Plan Personnalisé de Coordination.
Contact : 04 94 35 32 01 | None

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 80
Objectif : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : 04 22 44 84 73 | None

[ CPTS - Communauté Professionnelle Territoriale de Santé ] - Priorite : 65
Objectif : Accès aux soins : Recherche de médecin traitant (justifiée par retraite/déménagement) et dispositif MISAS pour éviter le renoncement aux soins.
Contact : 06 63 63 63 91 | 3 Rue Aspirant François Philippe 83260 La Crau

[ CCAS - Centre Communal d'Action Sociale ] - Priorite : 60
Objectif : Information et premier accueil social : Se renseigner sur les aides légales (RSA), les secours d'urgence (alimentaire, factures) et les logements seniors de la commune.
Contact : 04 94 08 98 34 | 81 Rue Marius Tardivier 83130 La garde

```

</details>

<details>
<summary>🔍 Cas Mr Lambert (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Lambert (Appel Infirmière) ---

1. Extraction IA pour le récit de l'infirmière...

--- DEBUG : ANALYSE EXPERTE ---
Situation de décompensation psychologique et isolement social
Ville extraite : La Seyne
Médecin : absent
Malveillance : negligence
Hospitalisation : None
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 78,
  "usager.localisation.commune_residence": "La Seyne",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": 4,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "negligence",
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": false,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
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
  "evaluation.comid.inquietude_sante": true,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": true,
  "evaluation.comid.degradation_recente": true,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": false,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": true,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": false,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexité COMID...
Score Total : 7 (Situation à risque de complexité)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (La Seyne-sur-Mer)...

--- REPONSE D'ORIA POUR L'INFIRMIERE ---
ORIA : 'D'après votre description, la situation de M. Lambert est Situation à risque de complexité. Voici les priorités d'appel :'

CONTACTER : [ CEV - Cellule Écoute et Vigilance (Urgence & Danger) ]
POURQUOI : protection_et_mise_en_securite (Peut faire l'objet d'un signalement au pénal avec copie au Procureur de la République)
CONTACT : 04 83 95 16 01 | None

CONTACTER : [ CRT - Centre de Ressources Territorial (Volet 2 - Accompagnement Renforcé) ]
POURQUOI : Maintien à domicile renforcé : Alternative à l'EHPAD pour les situations en perte d'autonomie importante ou complexité technique.
CONTACT : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chênes 83500 LA SEYNE SUR MER

CONTACTER : [ DAC - Dispositif d'Appui à la Coordination (Dernier Recours) ]
POURQUOI : Coordination de haut niveau : Évaluation multidimensionnelle et déblocage de situations complexes (sanitaire, social, médico-social). Plan Personnalisé de Coordination.
CONTACT : 04 94 35 32 01 | None

CONTACTER : [ CLIC - Centre Local d'Information et de Coordination ]
POURQUOI : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
CONTACT : 04 94 06 97 04 | None

CONTACTER : [ CPTS - Communauté Professionnelle Territoriale de Santé ]
POURQUOI : Accès aux soins : Recherche de médecin traitant (justifiée par retraite/déménagement) et dispositif MISAS pour éviter le renoncement aux soins.
CONTACT : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

```

</details>

<details>
<summary>🔍 Cas Mr Leroy (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Leroy (Moins de 60 ans) ---

1. Extraction IA pour : 'M. Leroy, 45 ans, habite à Toulon. Il est atteint ...'

--- DEBUG : ANALYSE EXPERTE ---
Situation critique, besoin d'aide immédiate
Ville extraite : Toulon
Médecin : absent
Malveillance : aucune
Hospitalisation : None
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 45,
  "usager.localisation.commune_residence": "Toulon",
  "usager.situation_actuelle.APA": "non",
  "usager.situation_actuelle.PCH": "non",
  "usager.situation_actuelle.GIR": 6,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "absent",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "critique",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "secours_urgence",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": true,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
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
  "evaluation.comid.inquietude_sante": true,
  "evaluation.comid.agressivite": false,
  "evaluation.comid.opposition_soins": false,
  "evaluation.comid.degradation_recente": true,
  "evaluation.comid.perte_autonomie_recente": false,
  "evaluation.comid.transition_parcours": true,
  "evaluation.comid.trouble_cognitif_aigu": false,
  "evaluation.comid.imprevisibilite": false,
  "evaluation.comid.multitude_intervenants": false,
  "evaluation.comid.manque_partenariat": false,
  "evaluation.comid.incoherence_soins": false,
  "evaluation.comid.probleme_assurance": false,
  "evaluation.comid.lourdeur_reseau": true,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexité COMID...
Score Total : 10 (Situation complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION (Age: 45 ans) ---

[ CEV - Cellule Écoute et Vigilance (Urgence & Danger) ] - Priorite : 95
Objectif : protection_et_mise_en_securite (Peut faire l'objet d'un signalement au pénal avec copie au Procureur de la République)
Contact : 04 83 95 16 01 | None

[ DAC - Dispositif d'Appui à la Coordination ] - Priorite : 85
Objectif : Motifs d'orientation combinés :
  • [Dispositif d'Appui à la Coordination (Dernier Recours)] : Coordination de haut niveau : Évaluation multidimensionnelle et déblocage de situations complexes (sanitaire, social, médico-social). Plan Personnalisé de Coordination.
  • [Échec ou saturation des aides professionnelles] : Professionnels (SAAD, IDEL) déjà présents au domicile mais en situation de saturation ou d'échec face à une complexité systémique.
Contact : 04 94 35 32 01 | None

[ UTS / ASPI - Unité Territoriale Sociale (Action Sociale Prévention Insertion) ] - Priorite : 70
Objectif : PAS (Premier Accueil Social) : Évaluation, ouverture de droits, aides financières ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
Contact : 04 83 95 24 42 | 100, traverse des minimes 83000 Toulon

[ CPTS - Communauté Professionnelle Territoriale de Santé ] - Priorite : 65
Objectif : Accès aux soins : Recherche de médecin traitant (justifiée par retraite/déménagement) et dispositif MISAS pour éviter le renoncement aux soins.
Contact : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

[ CCAS - Centre Communal d'Action Sociale ] - Priorite : 60
Objectif : Information et premier accueil social : Se renseigner sur les aides légales (RSA), les secours d'urgence (alimentaire, factures) et les logements seniors de la commune.
Contact : 04 94 24 65 00 | 100 rue des remparts - CS 20813 83051 Toulon Cedex

```

</details>

