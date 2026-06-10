# 📋 Rapport d'Évaluation Clinique ORIA

Généré automatiquement le : `2026-06-09 14:13:01`  
Nombre de cas exécutés : **21**  
Taux de succès : **21/21**  
Temps d'exécution total : **241.78 secondes**  

## 📊 Tableau récapitulatif des Orientations

| Patient | Status | Score COMID | Orientation Principale | Temps d'exécution |
| :--- | :---: | :---: | :--- | :---: |
| **Mme Durand** | ✅ SUCCESS | 5 | `DAC - Dispositif d'Appui à la Coordination` | 10.43s |
| **Mme Huguette** | ✅ SUCCESS | 6 | `CEV - Cellule Écoute et Vigilance (Spoliation & Autres Dangers)` | 14.10s |
| **Mr Vacek** | ✅ SUCCESS | 5 | `Police / Gendarmerie (Urgence Vitale & Intervention)` | 11.53s |
| **Mr Lambert** | ✅ SUCCESS | 4 | `DAC - Dispositif d'Appui à la Coordination` | 12.70s |
| **Mme Petit** | ✅ SUCCESS | 2 | `CLIC - Centre Local d'Information et de Coordination (Sénior)` | 8.85s |
| **Mme Lefebvre** | ✅ SUCCESS | 6 | `DAC - Dispositif d'Appui à la Coordination` | 12.40s |
| **Mr Leroy** | ✅ SUCCESS | 4 | `DAC - Dispositif d'Appui à la Coordination` | 10.54s |
| **Mme Rossi** | ✅ SUCCESS | 4 | `Police / Gendarmerie (Urgence Vitale & Intervention)` | 9.69s |
| **Mme Martin** | ✅ SUCCESS | 4 | `CLIC - Centre Local d'Information et de Coordination (Sénior)` | 12.01s |
| **Mr Martin** | ✅ SUCCESS | 3 | `CLIC - Centre Local d'Information et de Coordination (Sénior)` | 10.13s |
| **Mme Fontaine** | ✅ SUCCESS | 5 | `CEV - Cellule Écoute et Vigilance (Spoliation & Autres Dangers)` | 11.64s |
| **Mme Gautier** | ✅ SUCCESS | 11 | `DAC - Dispositif d'Appui à la Coordination` | 19.70s |
| **Mme Vial** | ✅ SUCCESS | 4 | `DAC - Situation de complexité multidimensionnelle (Sanitaire, Social, Médico-social)` | 10.12s |
| **Mme Michu** | ✅ SUCCESS | 4 | `DAC - Dispositif d'Appui à la Coordination` | 8.28s |
| **Mr Petit** | ✅ SUCCESS | 6 | `PSCG SS APA - Pôle Social de Solidarité et de Gestion (APA)` | 13.21s |
| **Mr Chen** | ✅ SUCCESS | 2 | `CLIC - Centre Local d'Information et de Coordination` | 10.23s |
| **Mme Morel** | ✅ SUCCESS | 3 | `Service Social de l'Hôpital (Hospitalisation en cours)` | 10.06s |
| **Mr Pierre** | ✅ SUCCESS | 5 | `CLIC - Centre Local d'Information et de Coordination (Sénior)` | 10.89s |
| **Mme Bernard** | ✅ SUCCESS | 4 | `CEV - Cellule Écoute et Vigilance (Violences Physiques & Danger Immédiat)` | 10.68s |
| **Mr Dubois** | ✅ SUCCESS | 6 | `CLIC - Centre Local d'Information et de Coordination (Sénior)` | 12.07s |
| **Mme Mouton** | ✅ SUCCESS | 5 | `DAC - Dispositif d'Appui à la Coordination` | 12.47s |

---

## 📝 Détail des extractions et raisonnements

<details>
<summary>🔍 Cas Mme Durand (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Durand ---

1. Extraction IA pour : 'Mme Durand, 88 ans, vit à Hyères. Elle est très co...'

--- DEBUG : ANALYSE EXPERTE ---
La situation est critique car l'usager est très confuse et agressive, ce qui rend difficile la prise en charge de son diabète. Il est important d'établir un plan d'aide adapté pour répondre à ses besoins.
Ville extraite : Hyères
Médecin : incertain
Malveillance : aucune
Hospitalisation : aucun
État Logement : non_renseigne
--- FIN DEBUG ---

Donnees extraites (JSON) :
{
  "usager.identite.age_estime": 88,
  "usager.localisation.commune_residence": "Hyères",
  "usager.situation_actuelle.APA": "oui",
  "usager.situation_actuelle.PCH": "none",
  "usager.situation_actuelle.GIR": null,
  "vulnerabilites.sante.suivi_medical.medecin_traitant": "incertain",
  "usager.situation_actuelle.suspicion_malveillance": "aucune",
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "none",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
  "evaluation.comid.justifications": [
    {
      "code": "troubles_cognitifs",
      "justification": "elle est très confuse"
    },
    {
      "code": "agressivite",
      "justification": "elle est agressive avec les infirmiers"
    },
    {
      "code": "isolement_social",
      "justification": "elle vit à Hyères, seule"
    },
    {
      "code": "logement_inadapte",
      "justification": "elle déambule la nuit dans l'immeuble"
    }
  ],
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

2. Calcul du score de complexité COMID...
Score Total : 5 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Hyères)...

--- RESULTATS DE L'ORIENTATION ---

[ DAC - Dispositif d'Appui à la Coordination ] - Priorite : 105
Objectif : Motifs d'orientation combinés :
  • [Refus de soins ou d'aide (Priorité Absolue)] : Refus de soins ou opposition critique aux aides à domicile : Rupture critique de parcours nécessitant l'intervention immédiate du DAC pour débloquer la situation.
  • [Situation de complexité multidimensionnelle (Sanitaire, Social, Médico-social)] : Situation de forte complexité multidimensionnelle (sanitaire, social et médico-social) : Évaluation globale et coordination intensive par le DAC pour débloquer le parcours de vie à domicile.
Contact : Non trouve dans le referentiel territorial

[ PSCG SS APA - Pôle Social de Solidarité et de Gestion (APA) ] - Priorite : 100
Objectif : Contacter votre référent APA au Conseil Départemental (PSCG SS APA) pour toute modification de plan d'aide ou besoin d'accompagnement social supplémentaire.
Contact : Non trouve dans le referentiel territorial

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mme Huguette (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Huguette (Urgence Sociale / Protection) ---

1. Extraction IA (Temp=0.0) pour : 'Mme Huguette, 79 ans, vit seule dans un logement insalubre et humide à La Valett...'

--- DEBUG : ANALYSE EXPERTE ---
La situation est préoccupante car Mme H. vit seule dans un logement insalubre et humide, sans ressources financières et avec des problèmes de santé. Son neveu procédure à des retraits d'argent massifs sans justification, laissant Mme H. sans le moindre sou pour s'acheter de quoi manger. Elle est terrifiée par son neveu et n'ose rien dire par peur de représailles.
Ville extraite : La Valette du Var
Médecin : incertain
Malveillance : spoliation_financiere
Hospitalisation : aucun
État Logement : insalubre
--- FIN DEBUG ---

Données extraites (JSON) :
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
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "oui",
  "usager.cadre_de_vie.etat_logement": "insalubre",
  "evaluation.comid.justifications": [
    {
      "code": "isolement_social",
      "justification": "Mme H. vit seule dans un logement insalubre et humide à La Valette du Var."
    },
    {
      "code": "precarite_financiere",
      "justification": "Elle n'a pas l'APA et vit sous le seuil de pauvreté avec une infime pension de retraite."
    },
    {
      "code": "logement_inadapte",
      "justification": "Le logement est insalubre et humide."
    },
    {
      "code": "conflit_reseau",
      "justification": "Un neveu d'Huguette, qui a procuration sur ses comptes bancaires, effectue des retraits d'argent massifs et répétés sans justification, laissant Huguette sans le moindre sou pour s'acheter de quoi manger."
    },
    {
      "code": "inquietude_sante",
      "justification": "Huguette est terrifiée par son neveu et n'ose rien dire par peur de représailles."
    }
  ],
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
  "evaluation.comid.lourdeur_reseau": true,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexité COMID...
Score Total : 6 (Situation à risque de complexité)

3. Évaluation de l'orientation...

4. Recherche des contacts territoriaux (La Valette)...

--- RÉSULTATS DE L'ORIENTATION POUR MME HUGUETTE ---

[ CEV - Cellule Écoute et Vigilance (Spoliation & Autres Dangers) ] - Priorité : 107
Objectif : Mise en sécurité immédiate, protection juridique et physique des majeurs vulnérables en situation de danger social ou maltraitance financière.
Contact : 04 83 95 16 01 | None

[ CLIC - Centre Local d'Information et de Coordination (Sénior) ] - Priorité : 80
Objectif : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : 04 22 44 84 73 | None

[ DAC - Situation de complexité multidimensionnelle (Sanitaire, Social, Médico-social) ] - Priorité : 72
Objectif : Situation de forte complexité multidimensionnelle (sanitaire, social et médico-social) : Évaluation globale et coordination intensive par le DAC pour débloquer le parcours de vie à domicile.
Contact : 04 94 35 32 01 | None

[ UTS / ASPI - Unité Territoriale Sociale (Action Sociale Prévention Insertion) ] - Priorité : 70
Objectif : PAS (Premier Accueil Social) : Évaluation, ouverture de droits, aides financières ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
Contact : 04 83 95 56 90 | 427 Avenue Duchatel 83130 La Valette du Var

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mr Vacek (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Vacek (Habitat Indigne & Danger) ---

1. Extraction IA pour la situation de péril...

--- DEBUG : ANALYSE EXPERTE ---
L'usager est victime de violences physiques et vit dans des conditions insalubres, ce qui nécessite une intervention urgente pour protéger sa santé et son bien-être.
Ville extraite : Toulon
Médecin : incertain
Malveillance : violences_physiques
Hospitalisation : aucun
État Logement : insalubre
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
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "insalubre",
  "evaluation.comid.justifications": [
    {
      "code": "logement_inadapte",
      "justification": "Son appartement est insalubre : il n'a plus d'eau courante depuis 3 mois et le plafond de sa chambre menace de s'effondrer suite à une infiltration."
    },
    {
      "code": "isolement_social",
      "justification": "Il vit dans l'humidité totale et il commence à avoir des problèmes respiratoires sérieux."
    },
    {
      "code": "precarite_financiere",
      "justification": "Son propriétaire est un marchand de sommeil qui le menace physiquement s'il appelle la mairie. Il n'a plus de revenus car son dossier de retraite est bloqué."
    },
    {
      "code": "anxiete",
      "justification": "Il est terrifié"
    }
  ],
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

2. Calcul du score de complexité COMID...
Score Total : 5 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- REPONSE D'ORIA (URGENCE HABITAT) ---
ORIA : 'La situation de M. Vacek présente un DANGER IMMINENT.'

VOTRE PRIORITÉ ABSOLUE : [ Police / Gendarmerie (Urgence Vitale & Intervention) ]
MISSION : Intervention immédiate des forces de l'ordre en cas d'agression physique active et en cours ou danger vital imminent.
CONTACT : N/A

ENSUITE (VOLET SOCIAL) : [ CEV - Cellule Écoute et Vigilance (Violences Physiques & Danger Immédiat) ]
MISSION : Mise en sécurité immédiate et protection d'urgence des majeurs vulnérables en situation de violence physique active ou menacée.

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mr Lambert (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Lambert (Appel Infirmière) ---

1. Extraction IA pour le récit de l'infirmière...

--- DEBUG : ANALYSE EXPERTE ---
Le patient, un homme de 78 ans, est en situation de crise psychique avec des comportements agressifs et refus de soins. Il est isolé et son logement est dans un état déplorable. Il est important d'intervenir pour évaluer la situation et proposer une aide adaptée.
Ville extraite : La Seyne
Médecin : incertain
Malveillance : aucune
Hospitalisation : aucun
État Logement : diogene
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
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "diogene",
  "evaluation.comid.justifications": [
    {
      "code": "isolement_social",
      "justification": "son appartement, qui était impeccable, est devenu un dépotoir : il y a des sacs poubelles partout et ça sent très fort l'urine"
    },
    {
      "code": "logement_inadapte",
      "justification": "son appartement, qui était impeccable, est devenu un dépotoir : il y a des sacs poubelles partout et ça sent très fort l'urine"
    },
    {
      "code": "perte_autonomie_recente",
      "justification": "c'est la chute libre. Il refuse que j'entre faire ses pansements, il me crie dessus et me dit que je veux l'empoisonner avec ses médicaments"
    },
    {
      "code": "isolement_social",
      "justification": "sa famille est à Paris et ils ne décrochent plus le téléphone"
    }
  ],
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

2. Calcul du score de complexité COMID...
Score Total : 4 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (La Seyne-sur-Mer)...

--- REPONSE D'ORIA POUR L'INFIRMIERE ---
ORIA : 'D'après votre description, la situation de M. Lambert est Situation non complexe. Voici les priorités d'appel :'

CONTACTER : [ DAC - Dispositif d'Appui à la Coordination ]
POURQUOI : Motifs d'orientation combinés :
  • [Refus de soins ou d'aide (Priorité Absolue)] : Refus de soins ou opposition critique aux aides à domicile : Rupture critique de parcours nécessitant l'intervention immédiate du DAC pour débloquer la situation.
  • [Situation de complexité multidimensionnelle (Sanitaire, Social, Médico-social)] : Situation de forte complexité multidimensionnelle (sanitaire, social et médico-social) : Évaluation globale et coordination intensive par le DAC pour débloquer le parcours de vie à domicile.
  • [Suspicion de Diogène ou incurie] : Insalubrité ou négligence critique à domicile : Suspicion ou syndrome de Diogène/incurie avéré nécessitant une coordination multidimensionnelle renforcée par le DAC.
CONTACT : 04 94 35 32 01 | None

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mme Petit (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Petit (Urgence CCAS) ---

1. Extraction IA pour : 'Mme Petit, 78 ans, habite à La Garde. Elle vit seu...'

--- DEBUG : ANALYSE EXPERTE ---
La patiente, âgée de 78 ans, vit seule et a une petite retraite. Elle est en difficulté financière et demande de l'aide pour ses courses. Elle bénéficie d'un médecin traitant et des professionnels passent régulièrement à domicile.
Ville extraite : La Garde
Médecin : identifie
Malveillance : aucune
Hospitalisation : aucun
État Logement : propre
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
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.comid.justifications": [
    {
      "code": "precarite_financiere",
      "justification": "son compte bancaire est à découvert"
    },
    {
      "code": "isolement_social",
      "justification": "elle vit seule"
    }
  ],
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

[ CLIC - Centre Local d'Information et de Coordination (Sénior) ] - Priorite : 80
Objectif : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : 04 22 44 84 73 | None

[ UTS / ASPI - Unité Territoriale Sociale (Action Sociale Prévention Insertion) ] - Priorite : 70
Objectif : PAS (Premier Accueil Social) : Évaluation, ouverture de droits, aides financières ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
Contact : 04 83 95 56 50 | 53 Impasse Blériot Immeuble Le Frédéric 83130 La Garde

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mme Lefebvre (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Lefebvre ---

1. Extraction IA pour : 'Mme Lefebvre, 65 ans, vit à La Garde. Elle est sui...'

--- DEBUG : ANALYSE EXPERTE ---
La patiente, âgée de 65 ans, vit à La Garde et est suivie pour une bipolarité. Elle a arrêté son traitement le mois dernier et consomme beaucoup d'alcool pour 'calmer ses angoisses'. Elle vit dans un appartement très encombré (Syndrome de Diogène suspecté) et ses voisins se plaignent d'odeurs fortes. Elle n'a plus de famille et refuse toute aide du service social, se montrant parfois très agressive verbalement quand on frappe à sa porte.
Ville extraite : La Garde
Médecin : identifie
Malveillance : aucune
Hospitalisation : aucun
État Logement : diogene
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
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "diogene",
  "evaluation.comid.justifications": [
    {
      "code": "psychiatrie",
      "justification": "bipolarité"
    },
    {
      "code": "addiction",
      "justification": "consomme beaucoup d'alcool pour 'calmer ses angoisses'"
    },
    {
      "code": "isolement_social",
      "justification": "n'a plus de famille et refuse toute aide du service social"
    },
    {
      "code": "logement_inadapte",
      "justification": "appartement très encombré (Syndrome de Diogène suspecté)"
    },
    {
      "code": "anxiete",
      "justification": "très angoissée"
    }
  ],
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

2. Calcul du score de complexité COMID...
Score Total : 6 (Situation à risque de complexité)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (La Garde)...

--- RESULTATS DE L'ORIENTATION ---

[ DAC - Dispositif d'Appui à la Coordination ] - Priorite : 105
Objectif : Motifs d'orientation combinés :
  • [Refus de soins ou d'aide (Priorité Absolue)] : Refus de soins ou opposition critique aux aides à domicile : Rupture critique de parcours nécessitant l'intervention immédiate du DAC pour débloquer la situation.
  • [Situation de complexité multidimensionnelle (Sanitaire, Social, Médico-social)] : Situation de forte complexité multidimensionnelle (sanitaire, social et médico-social) : Évaluation globale et coordination intensive par le DAC pour débloquer le parcours de vie à domicile.
  • [Suspicion de Diogène ou incurie] : Insalubrité ou négligence critique à domicile : Suspicion ou syndrome de Diogène/incurie avéré nécessitant une coordination multidimensionnelle renforcée par le DAC.
Contact : 04 94 35 32 01 | None

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mr Leroy (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Leroy (Moins de 60 ans) ---

1. Extraction IA pour : 'M. Leroy, 45 ans, habite à Toulon. Il est atteint ...'

--- DEBUG : ANALYSE EXPERTE ---
L'usager est un homme de 45 ans, atteint d'une Sclérose en Plaques (SEP) diagnostiquée il y a 2 ans. Il vit seul et se sent perdu dans son parcours de soins entre les différents spécialistes. Son moral est au plus bas et il exprime des idées noires.
Ville extraite : Toulon
Médecin : identifie
Malveillance : aucune
Hospitalisation : aucun
État Logement : propre
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
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.comid.justifications": [
    {
      "code": "precarite_financiere",
      "justification": "ses revenus ont chuté et il a du mal à payer son loyer"
    },
    {
      "code": "isolement_social",
      "justification": "il vit seul"
    },
    {
      "code": "depression",
      "justification": "il exprime des idées noires"
    }
  ],
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

2. Calcul du score de complexité COMID...
Score Total : 4 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION (Age: 45 ans) ---

[ DAC - Dispositif d'Appui à la Coordination ] - Priorite : 105
Objectif : Motifs d'orientation combinés :
  • [Refus de soins ou d'aide (Priorité Absolue)] : Refus de soins ou opposition critique aux aides à domicile : Rupture critique de parcours nécessitant l'intervention immédiate du DAC pour débloquer la situation.
  • [Situation de complexité multidimensionnelle (Sanitaire, Social, Médico-social)] : Situation de forte complexité multidimensionnelle (sanitaire, social et médico-social) : Évaluation globale et coordination intensive par le DAC pour débloquer le parcours de vie à domicile.
Contact : 04 94 35 32 01 | None

[ UTS / ASPI - Unité Territoriale Sociale (Action Sociale Prévention Insertion) ] - Priorite : 70
Objectif : PAS (Premier Accueil Social) : Évaluation, ouverture de droits, aides financières ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
Contact : 04 83 95 24 42 | 100, traverse des minimes 83000 Toulon

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mme Rossi (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Rossi (Violences Conjugales) ---

1. Extraction IA pour : 'Mme Rossi, 70 ans, habite à Toulon. Elle vient d'a...'

--- DEBUG : ANALYSE EXPERTE ---
La situation est critique car la personne a dû quitter son domicile en urgence en raison de violences physiques et verbales exercées par son mari. Elle a besoin d'une protection immédiate et d'un hébergement d'urgence.
Ville extraite : Toulon
Médecin : incertain
Malveillance : violences_physiques
Hospitalisation : aucun
État Logement : propre
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
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.comid.justifications": [
    {
      "code": "isolement_social",
      "justification": "elle est actuellement cachée chez une amie"
    },
    {
      "code": "logement_inadapte",
      "justification": "son mari est devenu très violent physiquement et verbalement"
    },
    {
      "code": "depression",
      "justification": "elle est actuellement cachée chez une amie (angoisse)"
    }
  ],
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

2. Calcul du score de complexité COMID...
Score Total : 4 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION (Protection / Violences) ---

[ Police / Gendarmerie (Urgence Vitale & Intervention) ] - Priorite : 110
Objectif : Intervention immédiate des forces de l'ordre en cas d'agression physique active et en cours ou danger vital imminent.
Contact : Non trouve dans le referentiel territorial

[ CCAS - Secours d'Urgence (Alimentaire & Factures) ] - Priorite : 85
Objectif : Secours financier ou alimentaire d'urgence de proximité : Attribution d'aides extra-légales par la mairie.
Contact : 04 94 24 65 00 | 100 rue des remparts - CS 20813 83051 Toulon Cedex

[ CLIC - Centre Local d'Information et de Coordination (Sénior) ] - Priorite : 80
Objectif : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : 04 94 24 65 25 | None

[ DAC - Situation de complexité multidimensionnelle (Sanitaire, Social, Médico-social) ] - Priorite : 72
Objectif : Situation de forte complexité multidimensionnelle (sanitaire, social et médico-social) : Évaluation globale et coordination intensive par le DAC pour débloquer le parcours de vie à domicile.
Contact : 04 94 35 32 01 | None

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mme Martin (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Martin (Détresse Aidant) ---

1. Extraction IA pour le récit de l'aidante...

--- DEBUG : ANALYSE EXPERTE ---
La fille de Mme M. (82 ans) est à bout, travaillant à temps plein et passant toutes ses soirées et week-ends chez sa mère. Cette dernière perd la tête, laisse le gaz allumé, se relève la nuit et a déjà tombée deux fois. La fille craque sous la pression et a peur de devenir méchante avec sa mère. Il est essentiel d'apporter une aide à domicile pour sécuriser Mme M. et permettre à sa fille de retrouver un peu de répit.
Ville extraite : Toulon
Médecin : identifie
Malveillance : aucune
Hospitalisation : aucun
État Logement : propre
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
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.comid.justifications": [
    {
      "code": "epuisement_aidant",
      "justification": "Je n'en peux plus, je craque."
    },
    {
      "code": "isolement_social",
      "justification": "Je travaille à temps plein et je passe toutes mes soirées et mes week-ends chez elle."
    },
    {
      "code": "logement_inadapte",
      "justification": "Ma mère laisse le gaz allumé, elle se relève la nuit..."
    },
    {
      "code": "anxiete",
      "justification": "Je pleure tout le temps au travail."
    }
  ],
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

2. Calcul du score de complexité COMID...
Score Total : 4 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- REPONSE D'ORIA POUR L'AIDANTE ---
ORIA : 'Je comprends votre épuisement. La situation de votre mère est Situation non complexe.'

VOTRE PRIORITÉ ABSOLUE : [ CLIC - Centre Local d'Information et de Coordination (Sénior) ]
MISSION : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
CONTACT : 04 94 24 65 25

CONSEIL POUR VOUS : 'Pensez également à contacter une plateforme de répit pour aidants. Ces structures proposent du soutien psychologique pour vous permettre de souffler.'

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mr Martin (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Martin ---

1. Extraction IA pour : 'M. Martin, 75 ans, habite à La Seyne-sur-Mer. Il a...'

--- DEBUG : ANALYSE EXPERTE ---
L'usager, âgé de 75 ans, est seul à domicile après l'hospitalisation de son épouse. Il a des problèmes de vue et ne peut plus préparer ses repas ni prendre ses médicaments.
Ville extraite : La Seyne-sur-Mer
Médecin : incertain
Malveillance : aucune
Hospitalisation : aucun
État Logement : propre
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
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.comid.justifications": [
    {
      "code": "multimorbidite",
      "justification": "de graves problèmes de vue et sa femme, qui s'occupait de tout, vient d'être hospitalisée"
    },
    {
      "code": "isolement_social",
      "justification": "Il se retrouve seul"
    },
    {
      "code": "logement_inadapte",
      "justification": "n'arrive plus à préparer ses repas ni à prendre ses médicaments"
    }
  ],
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

2. Calcul du score de complexité COMID...
Score Total : 3 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (La Seyne-sur-Mer)...

--- RESULTATS DE L'ORIENTATION ---

[ CLIC - Centre Local d'Information et de Coordination (Sénior) ] - Priorite : 80
Objectif : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : 04 94 06 97 04 | None

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mme Fontaine (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Fontaine (Alerte Kiné) ---

1. Extraction IA pour l'alerte du kiné...

--- DEBUG : ANALYSE EXPERTE ---
La patiente de 85 ans, résidente à Sanary, est en situation de détresse alimentaire et médicamenteuse. Son frigo est vide et elle oublie ses médicaments. Elle est également victime de spoliation financière par son fils qui vit avec elle et lui demande de l'argent de manière insistante. Il est important de prendre en compte ces éléments pour établir un plan de soins adapté à sa situation.
Ville extraite : Sanary
Médecin : identifie
Malveillance : spoliation_financiere
Hospitalisation : aucun
État Logement : propre
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
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "aide_alimentaire",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.comid.justifications": [
    {
      "code": "douleurs",
      "justification": "elle oublie ses médicaments contre la douleur"
    },
    {
      "code": "precarite_financiere",
      "justification": "son frigo est littéralement vide"
    },
    {
      "code": "isolement_social",
      "justification": "elle a l'air terrorisée"
    },
    {
      "code": "agressivite",
      "justification": "il lui crie dessus et j'ai remarqué qu'il lui demande de l'argent de façon très insistante à chaque fois que je suis là"
    }
  ],
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

2. Calcul du score de complexité COMID...
Score Total : 5 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Sanary-sur-Mer)...

--- REPONSE D'ORIA POUR LE KINE ---
ORIA : 'Situation identifiée comme Situation non complexe. Voici les actions prioritaires :'

ACTION : [ CEV - Cellule Écoute et Vigilance (Spoliation & Autres Dangers) ]
MOTIF : Mise en sécurité immédiate, protection juridique et physique des majeurs vulnérables en situation de danger social ou maltraitance financière.
CONTACT : 04 83 95 16 01

ACTION : [ CCAS - Secours d'Urgence (Alimentaire & Factures) ]
MOTIF : Secours financier ou alimentaire d'urgence de proximité : Attribution d'aides extra-légales par la mairie.
CONTACT : 04 94 88 50 70

ACTION : [ DAC - Situation de complexité multidimensionnelle (Sanitaire, Social, Médico-social) ]
MOTIF : Situation de forte complexité multidimensionnelle (sanitaire, social et médico-social) : Évaluation globale et coordination intensive par le DAC pour débloquer le parcours de vie à domicile.
CONTACT : 04 94 35 32 01

ACTION : [ UTS / ASPI - Unité Territoriale Sociale (Action Sociale Prévention Insertion) ]
MOTIF : PAS (Premier Accueil Social) : Évaluation, ouverture de droits, aides financières ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
CONTACT : 04 83 95 83 10

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mme Gautier (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Jeanne Gautier (Très Complexe) ---

1. Extraction IA pour le cas très complexe...

--- DEBUG : ANALYSE EXPERTE ---
La situation clinique est caractérisée par une grave dépression post-traumatique, des troubles cognitifs majeurs et une perte d'autonomie récente. La personne souffre de plusieurs pathologies chroniques et présente une polymédication importante. Elle vit seule dans un logement insalubre et inadapté, ce qui peut contribuer à son état de santé instable.
Ville extraite : Toulon
Médecin : identifie
Malveillance : aucune
Hospitalisation : aucun
État Logement : insalubre
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
  "evaluation.comid.justifications": [
    {
      "code": "multimorbidite",
      "justification": "diabète de type 2, insuffisance cardiaque et arthrose déformante"
    },
    {
      "code": "douleurs",
      "justification": "souffre d'un diabète de type 2, d'une insuffisance cardiaque et d'une arthrose déformante qui lui causent des douleurs chroniques permanentes et intolérables"
    },
    {
      "code": "polymedication",
      "justification": "ordonnance est extrêmement lourde avec une polymédication de plus de 9 médicaments par jour"
    },
    {
      "code": "troubles_cognitifs",
      "justification": "présente des troubles cognitifs majeurs avec une perte de mémoire et une désorientation temporelle"
    },
    {
      "code": "precarite_financiere",
      "justification": "sa retraite de 800 € ne lui permet plus de faire face à ses factures d'électricité, créant une grande précarité financière"
    },
    {
      "code": "isolement_social",
      "justification": "elle vit seule dans un logement insalubre et inadapté"
    },
    {
      "code": "logement_inadapte",
      "justification": "son logement est situé au 3ème étage sans ascenseur"
    },
    {
      "code": "depression",
      "justification": "elle traverse une période de transition majeure suite au décès récent de son époux, ce qui a déclenché une grave dépression clinique avec des idées noires"
    },
    {
      "code": "anxiete",
      "justification": "elle est très angoissée par sa santé"
    },
    {
      "code": "perte_autonomie_recente",
      "justification": "elle présente une perte d'autonomie récente pour toutes les activités de la vie quotidienne suite à sa chute récente avec fracture du poignet"
    }
  ],
  "evaluation.comid.multimorbidite": true,
  "evaluation.comid.douleurs": true,
  "evaluation.comid.allergies": false,
  "evaluation.comid.polymedication": true,
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

2. Calcul du score de complexité COMID...
Score Total : 11 (Situation complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION ---

[ DAC - Dispositif d'Appui à la Coordination ] - Priorite : 105
Objectif : Motifs d'orientation combinés :
  • [Refus de soins ou d'aide (Priorité Absolue)] : Refus de soins ou opposition critique aux aides à domicile : Rupture critique de parcours nécessitant l'intervention immédiate du DAC pour débloquer la situation.
  • [Situation de complexité multidimensionnelle (Sanitaire, Social, Médico-social)] : Situation de forte complexité multidimensionnelle (sanitaire, social et médico-social) : Évaluation globale et coordination intensive par le DAC pour débloquer le parcours de vie à domicile.
Contact : 04 94 35 32 01 | None

[ UTS / ASPI - Unité Territoriale Sociale (Action Sociale Prévention Insertion) ] - Priorite : 70
Objectif : PAS (Premier Accueil Social) : Évaluation, ouverture de droits, aides financières ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
Contact : 04 83 95 24 42 | 100, traverse des minimes 83000 Toulon

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mme Vial (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Vial (Recherche Médecin Traitant) ---

1. Extraction IA pour : 'Mme Vial, 82 ans, vient de s'installer à Toulon po...'

--- DEBUG : ANALYSE EXPERTE ---
Analyse manquante
Ville extraite : Toulon
Médecin : absent
Malveillance : aucune
Hospitalisation : aucun
État Logement : propre
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
  "usager.cadre_de_vie.aidant_regulier": "oui",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.comid.justifications": [
    {
      "code": "multimorbidite",
      "justification": "souffre de diabète de type 2 et d'hypertension"
    },
    {
      "code": "isolement_social",
      "justification": "elle vient de s'installer à Toulon pour se rapprocher de sa fille"
    },
    {
      "code": "lourdeur_reseau",
      "justification": "sa fille travaille beaucoup et s'inquiète de ne pas trouver de solution pour sa mère"
    },
    {
      "code": "anxiete",
      "justification": "elle est très angoissée par cette rupture de suivi médical"
    }
  ],
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
  "evaluation.comid.lourdeur_reseau": true,
  "vulnerabilites.social.isolement_relationnel": "critique"
}

2. Calcul du score de complexité COMID...
Score Total : 4 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux...
Ville extraite par l'IA : Toulon

--- RESULTATS DE L'ORIENTATION (Territoire: Toulon - Canton 1, 2 et 3) ---

[ DAC - Situation de complexité multidimensionnelle (Sanitaire, Social, Médico-social) ] - Priorite : 72
Objectif : Situation de forte complexité multidimensionnelle (sanitaire, social et médico-social) : Évaluation globale et coordination intensive par le DAC pour débloquer le parcours de vie à domicile.
Contact : 04 94 35 32 01 | None

[ CPTS - Communauté Professionnelle Territoriale de Santé ] - Priorite : 50
Objectif : Accès aux soins : Recherche de médecin traitant (justifiée par retraite/déménagement) et dispositif MISAS pour éviter le renoncement aux soins.
Contact : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mme Michu (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Michu ---

1. Extraction IA pour : 'Mme Michu, 82 ans, vit seule à Toulon dans son app...'

--- DEBUG : ANALYSE EXPERTE ---
Analyse manquante
Ville extraite : Toulon
Médecin : incertain
Malveillance : aucune
Hospitalisation : aucun
État Logement : propre
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
  "demande.motif_principal": "refus_aide_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "oui",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.comid.justifications": [
    {
      "code": "troubles_cognitifs",
      "justification": "elle commence à oublier de manger"
    },
    {
      "code": "perte_autonomie_recente",
      "justification": "elle a chuté la semaine dernière"
    },
    {
      "code": "isolement_social",
      "justification": "elle vit seule"
    }
  ],
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

2. Calcul du score de complexité COMID...
Score Total : 4 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION ---

[ DAC - Dispositif d'Appui à la Coordination ] - Priorite : 105
Objectif : Motifs d'orientation combinés :
  • [Refus de soins ou d'aide (Priorité Absolue)] : Refus de soins ou opposition critique aux aides à domicile : Rupture critique de parcours nécessitant l'intervention immédiate du DAC pour débloquer la situation.
  • [Situation de complexité multidimensionnelle (Sanitaire, Social, Médico-social)] : Situation de forte complexité multidimensionnelle (sanitaire, social et médico-social) : Évaluation globale et coordination intensive par le DAC pour débloquer le parcours de vie à domicile.
Contact : 04 94 35 32 01 | None

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mr Petit (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Petit (Aidant Conjoint Epuisé) ---

1. Extraction IA pour le récit du conjoint aidant...

--- DEBUG : ANALYSE EXPERTE ---
La situation est critique car la personne âgée de 83 ans souffre de la maladie de Parkinson et nécessite une aide plus forte pour gérer ses besoins quotidiens. Le fait qu'elle vive au 3ème étage sans ascenseur et que son époux est épuisé soulève des préoccupations quant à sa sécurité et à sa santé.
Ville extraite : Toulon
Médecin : identifie
Malveillance : aucune
Hospitalisation : aucun
État Logement : insalubre
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
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "insalubre",
  "evaluation.comid.justifications": [
    {
      "code": "multimorbidite",
      "justification": "la maladie de Parkinson depuis 5 ans"
    },
    {
      "code": "douleurs",
      "justification": "des malaises"
    },
    {
      "code": "epuisement_aidant",
      "justification": "je suis au bout du rouleau"
    },
    {
      "code": "logement_inadapte",
      "justification": "on habite à Toulon au 3ème étage sans ascenseur"
    },
    {
      "code": "isolement_social",
      "justification": "je ne dors plus car elle crie la nuit"
    },
    {
      "code": "anxiete",
      "justification": "j'ai peur pour mon propre cœur, je sens que je fatigue"
    }
  ],
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

2. Calcul du score de complexité COMID...
Score Total : 6 (Situation à risque de complexité)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- REPONSE D'ORIA POUR L'AIDANT ---
voici votre priorité :'

VOTRE PRIORITÉ ABSOLUE : [ PSCG SS APA - Pôle Social de Solidarité et de Gestion (APA) ]
MISSION : Contacter votre référent APA au Conseil Départemental (PSCG SS APA) pour toute modification de plan d'aide ou besoin d'accompagnement social supplémentaire.
CONTACT : 04 83 95 79 51

CONSEIL POUR VOUS : 'Prenez soin de vous également. En plus de votre référent APA, sachez que les plateformes de répit peuvent vous soutenir pendant votre hospitalisation.'

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mr Chen (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Chen (PCH / Handicap) ---

1. Extraction IA pour : 'M. Chen, 52 ans, habite à Toulon. Il est en situat...'

--- DEBUG : ANALYSE EXPERTE ---
L'usager, âgé de 52 ans, bénéficie de la PCH et cherche des informations sur les logements adaptés à son fauteuil roulant dans sa commune de résidence. Il n'a pas de médecin traitant identifié et ne subit pas de malveillance. Sa situation est considérée comme faible en termes d'urgence.
Ville extraite : Toulon
Médecin : incertain
Malveillance : aucune
Hospitalisation : aucun
État Logement : propre
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
  "evaluation.comid.justifications": [
    {
      "code": "logement_inadapte",
      "justification": "habite à Toulon et cherche des informations sur les logements adaptés à son fauteuil roulant dans la commune"
    },
    {
      "code": "isolement_social",
      "justification": "il est en situation de handicap moteur et bénéficie de la PCH, ce qui peut entraîner un isolement social"
    }
  ],
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

2. Calcul du score de complexité COMID...
Score Total : 2 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION (Cas Handicap / PCH) ---

[ CLIC - Centre Local d'Information et de Coordination ] - Priorite : 102
Objectif : Motifs d'orientation combinés :
  • [Centre Local d'Information et de Coordination (Sénior)] : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
  • [Centre Local d'Information et de Coordination (Exception PCH)] : Maintien à domicile : Accompagnement spécialisé PCH (Prestation de Compensation du Handicap) pour les moins de 60 ans.
Contact : 04 94 24 65 25 | None

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mme Morel (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Morel (Hôpital) ---

1. Extraction IA pour : 'Mme Morel, 80 ans, est actuellement hospitalisée à...'

--- DEBUG : ANALYSE EXPERTE ---
La patiente, âgée de 80 ans, est hospitalisée suite à une mauvaise chute et s'inquiète pour son retour à domicile car elle vit seule au 3ème étage. Elle a besoin d'aide pour organiser sa sortie et remplir ses dossiers administratifs car elle a perdu ses papiers lors de son admission en urgence.
Ville extraite : None
Médecin : incertain
Malveillance : aucune
Hospitalisation : en_cours
État Logement : propre
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
  "evaluation.comid.justifications": [
    {
      "code": "isolement_social",
      "justification": "elle vit seule au 3ème étage"
    },
    {
      "code": "logement_inadapte",
      "justification": "elle vit seule au 3ème étage"
    },
    {
      "code": "perte_autonomie_recente",
      "justification": "a fait une mauvaise chute"
    }
  ],
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

2. Calcul du score de complexité COMID...
Score Total : 3 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION (Hopital Sainte Musse) ---

[ Service Social de l'Hôpital (Hospitalisation en cours) ] - Priorite : 95
Objectif : Accompagnement social en milieu hospitalier : Organisation de la sortie et lien direct avec le service social de l'établissement.
Contact : Non trouve dans le referentiel territorial

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mr Pierre (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Antoinette (Nouveau Cas Complexe) ---

1. Extraction IA (Déterministe, Temp=0.0) pour : 'M. Pierre agée de 88 ans vis seul à domicile polypathologie avais oublié ma visi...'

--- DEBUG : ANALYSE EXPERTE ---
L'usager de 88 ans, vivant seul à domicile, a oublié sa visite médicale prévue. Il bénéficie d'un médecin traitant mais ne reçoit pas de visites à domicile. Il a besoin d'aide pour faire ses courses et son réfrigérateur est en panne. Il n'y a pas d'auxiliaire de vie ni d'enfants. Il est addict à l'alcool.
Ville extraite : Toulon
Médecin : identifie
Malveillance : aucune
Hospitalisation : aucun
État Logement : propre
--- FIN DEBUG ---

Données extraites (JSON) :
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
  "evaluation.comid.justifications": [
    {
      "code": "addiction",
      "justification": "addition à l'alcool"
    },
    {
      "code": "isolement_social",
      "justification": "vit seul à domicile"
    },
    {
      "code": "logement_inadapte",
      "justification": "refrigerateur ne fonctionne plus"
    },
    {
      "code": "perte_autonomie_recente",
      "justification": "difficulté à la marche"
    }
  ],
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

2. Calcul du score de complexité COMID...
Score Total : 5 (Situation non complexe)

3. Évaluation de l'orientation...

4. Recherche des contacts territoriaux (La Garde)...

--- RÉSULTATS DE L'ORIENTATION POUR MME ANTOINETTE ---

[ CLIC - Centre Local d'Information et de Coordination (Sénior) ] - Priorité : 80
Objectif : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : 04 22 44 84 73 | None

[ DAC - Situation de complexité multidimensionnelle (Sanitaire, Social, Médico-social) ] - Priorité : 72
Objectif : Situation de forte complexité multidimensionnelle (sanitaire, social et médico-social) : Évaluation globale et coordination intensive par le DAC pour débloquer le parcours de vie à domicile.
Contact : 04 94 35 32 01 | None

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mme Bernard (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Bernard (Suspicion de maltraitance) ---

1. Extraction IA pour : 'Mme Bernard, 88 ans, habite à La Seyne-sur-Mer. El...'

--- DEBUG : ANALYSE EXPERTE ---
La situation est préoccupante car Mme B. est très isolée et subit des violences physiques suspectes. Elle a également un compte vide et ne peut plus s'acheter à manger.
Ville extraite : La Seyne-sur-Mer
Médecin : incertain
Malveillance : violences_physiques
Hospitalisation : aucun
État Logement : non_renseigne
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
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "aide_alimentaire",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "non_renseigne",
  "evaluation.comid.justifications": [
    {
      "code": "isolement_social",
      "justification": "très isolée"
    },
    {
      "code": "precarite_financiere",
      "justification": "son compte est vide et elle n'a plus de quoi s'acheter à manger"
    },
    {
      "code": "isolement_social",
      "justification": "très isolée"
    },
    {
      "code": "agressivite",
      "justification": "le petit-fils de Mme B., qui vient la voir de temps en temps, semble lui voler de l'argent"
    }
  ],
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

2. Calcul du score de complexité COMID...
Score Total : 4 (Situation non complexe)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux...
Ville extraite par l'IA : La Seyne-sur-Mer

--- RESULTATS DE L'ORIENTATION (Territoire: La Seyne-sur-mer) ---

[ CEV - Cellule Écoute et Vigilance (Violences Physiques & Danger Immédiat) ] - Priorite : 107
Objectif : Mise en sécurité immédiate et protection d'urgence des majeurs vulnérables en situation de violence physique active ou menacée.
Contact : 04 83 95 16 01 | None

[ CCAS - Secours d'Urgence (Alimentaire & Factures) ] - Priorite : 85
Objectif : Secours financier ou alimentaire d'urgence de proximité : Attribution d'aides extra-légales par la mairie.
Contact : 04 94 06 97 18 | Espace Hermès 2 avenue Charles-Gide 83500 La Seyne-sur-Mer

[ DAC - Situation de complexité multidimensionnelle (Sanitaire, Social, Médico-social) ] - Priorite : 72
Objectif : Situation de forte complexité multidimensionnelle (sanitaire, social et médico-social) : Évaluation globale et coordination intensive par le DAC pour débloquer le parcours de vie à domicile.
Contact : 04 94 35 32 01 | None

[ UTS / ASPI - Unité Territoriale Sociale (Action Sociale Prévention Insertion) ] - Priorite : 70
Objectif : PAS (Premier Accueil Social) : Évaluation, ouverture de droits, aides financières ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
Contact : 04 83 95 48 30 ou 04 83 95 37 99 | rue Charles Gide 83500 La Seyne sur mer

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mr Dubois (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas M. Dubois ---

1. Extraction IA pour : 'M. Dubois, 74 ans, vit à Toulon. Il souffre de dia...'

--- DEBUG : ANALYSE EXPERTE ---
L'usager souffre de diabète, d'hypertension et d'une insuffisance rénale chronique. Il est anxieux pour sa santé et appelle le cabinet infirmier plusieurs fois par jour pour demander s'il a bien pris ses cachets.
Ville extraite : Toulon
Médecin : identifie
Malveillance : aucune
Hospitalisation : aucun
État Logement : propre
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
  "adresseur.degre_urgence_percu": "modere",
  "vulnerabilites.sante.hospitalisation.statut": "aucun",
  "demande.motif_principal": "maintien_a_domicile",
  "vulnerabilites.sante.professionnels_domicile": "oui",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "propre",
  "evaluation.comid.justifications": [
    {
      "code": "multimorbidite",
      "justification": "souffre de diabète, d'hypertension et d'une insuffisance rénale chronique"
    },
    {
      "code": "douleurs",
      "justification": "souffre en permanence dans les jambes"
    },
    {
      "code": "polymedication",
      "justification": "prend 8 médicaments par jour"
    },
    {
      "code": "precarite_financiere",
      "justification": "a du mal à payer son loyer et ses factures"
    },
    {
      "code": "logement_inadapte",
      "justification": "appartement au 4ème étage sans ascenseur"
    },
    {
      "code": "anxiete",
      "justification": "est très anxieux pour sa santé"
    }
  ],
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
Score Total : 6 (Situation à risque de complexité)

3. Evaluation de l'orientation...

4. Recherche des contacts territoriaux (Toulon)...

--- RESULTATS DE L'ORIENTATION ---

[ CLIC - Centre Local d'Information et de Coordination (Sénior) ] - Priorite : 80
Objectif : Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : 04 94 24 65 25 | None

[ DAC - Situation de complexité multidimensionnelle (Sanitaire, Social, Médico-social) ] - Priorite : 72
Objectif : Situation de forte complexité multidimensionnelle (sanitaire, social et médico-social) : Évaluation globale et coordination intensive par le DAC pour débloquer le parcours de vie à domicile.
Contact : 04 94 35 32 01 | None

[ UTS / ASPI - Unité Territoriale Sociale (Action Sociale Prévention Insertion) ] - Priorite : 70
Objectif : PAS (Premier Accueil Social) : Évaluation, ouverture de droits, aides financières ponctuelles. Accompagnement social (RSA, budget, logement, violences conjugales).
Contact : 04 83 95 24 42 | 100, traverse des minimes 83000 Toulon

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

<details>
<summary>🔍 Cas Mme Mouton (Détail des logs)</summary>

```text
--- Lancement du test ORIA : Cas Mme Georgette Mouton (Ollioules) ---

1. Extraction IA pour : 'Mme Georgette Mouton, 83 ans, vit seule à Ollioules dans un appartement devenu e...'

--- DEBUG : ANALYSE EXPERTE ---
La situation clinique est marquée par un grand isolement social, une résidence insalubre et encombrée, ainsi qu'un risque majeur de chute et d'oublis de médicaments. Il est essentiel de mettre en place des mesures pour améliorer la sécurité et la santé de l'usager.
Ville extraite : Ollioules
Médecin : absent
Malveillance : aucune
Hospitalisation : aucun
État Logement : diogene
--- FIN DEBUG ---

Données extraites (JSON) :
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
  "demande.motif_principal": "refus_de_soins",
  "vulnerabilites.sante.professionnels_domicile": "non",
  "usager.cadre_de_vie.aidant_regulier": "non",
  "usager.cadre_de_vie.etat_logement": "diogene",
  "evaluation.comid.justifications": [
    {
      "code": "isolement_social",
      "justification": "Mme G. M., 83 ans, vit seule à Ollioules dans un appartement devenu extrêmement insalubre et encombré de déchets et d'objets accumulés (syndrome de Diogène)."
    },
    {
      "code": "logement_inadapte",
      "justification": "appartement devenu extrêmement insalubre et encombré de déchets et d'objets accumulés"
    },
    {
      "code": "epuisement_aidant",
      "justification": "elle n'a aucun aidant à proximité"
    },
    {
      "code": "troubles_cognitifs",
      "justification": "oublis de médicaments (mise en danger)"
    }
  ],
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

2. Calcul du score de complexité COMID...
Score Total : 5 (Situation non complexe)

3. Évaluation de l'orientation...

4. Recherche des contacts territoriaux (Ollioules)...

--- RÉSULTATS DE L'ORIENTATION POUR MME GEORGETTE MOUTON ---

[ DAC - Dispositif d'Appui à la Coordination ] - Priorité : 105
Objectif : Motifs d'orientation combinés :
  • [Refus de soins ou d'aide (Priorité Absolue)] : Refus de soins ou opposition critique aux aides à domicile : Rupture critique de parcours nécessitant l'intervention immédiate du DAC pour débloquer la situation.
  • [Situation de complexité multidimensionnelle (Sanitaire, Social, Médico-social)] : Situation de forte complexité multidimensionnelle (sanitaire, social et médico-social) : Évaluation globale et coordination intensive par le DAC pour débloquer le parcours de vie à domicile.
  • [Suspicion de Diogène ou incurie] : Insalubrité ou négligence critique à domicile : Suspicion ou syndrome de Diogène/incurie avéré nécessitant une coordination multidimensionnelle renforcée par le DAC.
Contact : 04 94 35 32 01 | None

[ UTS Littoral Sud Sainte Baume - OLLIOULES (Relais CLIC) ] - Priorité : 80
Objectif : La commune ne dispose pas de CLIC, se rapprocher de l'UTS. Maintien à domicile : Information, évaluation, ouverture des droits (APA, CARSAT) et aide administrative (impôts, retraite). UNIQUEMENT si l'APA n'est pas déjà en place.
Contact : 04 83 95 58 50 | Espace Pierre Puget 2 Place Marius Trotobas 83190 Ollioules

[ CRT - Centre de Ressources Territorial (Accompagnement Renforcé) ] - Priorité : 78
Objectif : Maintien à domicile renforcé et intensif : Alternative à l'EHPAD pour les situations en perte d'autonomie importante ou complexité technique.
Contact : 06 84 99 32 49 | 104, chemin de Mar Vivo aux deux Chênes 83500 LA SEYNE SUR MER

[ CPTS - Communauté Professionnelle Territoriale de Santé ] - Priorité : 50
Objectif : Accès aux soins : Recherche de médecin traitant (justifiée par retraite/déménagement) et dispositif MISAS pour éviter le renoncement aux soins.
Contact : 06 81 10 57 70 | 198 rue de Lisbonne 83500 La Seyne-sur-Mer

BDD - Dossier sauvegardé avec succès en base de données de manière anonymisée.

```

</details>

