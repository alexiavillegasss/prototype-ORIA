# Cadrage et Retour sur le Projet ORIA - Prototype (V1)

## 1. Cadrage du Projet ORIA (V1)

**Objectif Principal** : Développer un prototype fonctionnel d'une application permettant aux professionnels sanitaires, sociaux et médico-sociaux du DAC Var Ouest d'orienter efficacement des patients, prioritairement les personnes âgées nécessitant un maintien à domicile, vers les structures les plus adaptées.

### Parcours Utilisateur
1. **Saisie** : Le professionnel, en situation (domicile/cabinet), enregistre une note vocale (ou texte) décrivant la situation clinique, sociale et administrative du patient.
2. **Extraction** : Une Intelligence Artificielle (LLM + Speech-to-Text) transcrit l'audio et structure les informations selon un schéma de données prédéfini (`schema_pivot.json`).
3. **Analyse & Score** : L'IA évalue la complexité/fragilité à l'aide de grilles intégrées (COMID).
4. **Orientation** : Un moteur de règles métier (`orientation_rules.json`) identifie la ou les structures les plus pertinentes.
5. **Restitution** : L'application propose l'orientation, génère un indice de fragilité et pré-remplit la fiche d'orientation.

### Périmètre de la V1 (Prototype)
- **Cible** : Parcours Personnes Âgées (PA) & Maintien à domicile.
- **Fonctionnalités exclues** : Prédiction des ruptures de parcours (prévu pour plus tard).
- **Structures cibles priorisées** : CRT, CLIC, CCAS, UTS, DAC.

---

## 2. Retour sur l'existant

J'ai analysé les documents que vous avez fournis : `schema_pivot.json`, `schema_definition.json` et `orientation_rules.json`.

> [!TIP]
> **Félicitations pour la qualité du travail déjà accompli !** Vos schémas de données sont extrêmement complets. L'utilisation d'indices de confiance (`niveau_confiance_global`, `signaux_detectes`) et la structuration des vulnérabilités (autonomie, santé, social, administratif, habitat) montrent une excellente compréhension des enjeux métier.

### Points forts :
- **Architecture de la donnée** : Le `schema_definition.json` est clair, granulaire et couvre parfaitement le spectre médico-social.
- **Règles d'orientation** : La structure logique (all_of, any_of, none_of) est parfaite pour un moteur d'inférence.

### Modifications mineures apportées (Typos) :
J'ai remarqué et corrigé quelques fautes de frappe dans `schema_definition.json` pour éviter des bugs lors du développement :
- `decription` corrigé en `description`
- `suspiion_malveillance` corrigé en `suspicion_malveillance`
- `téléphonne` corrigé en `téléphone`
- `abscent` corrigé en `absent` dans `orientation_rules.json`

---

## 3. Ajout des Priorités dans `orientation_rules.json`

Afin de respecter la logique de priorité que vous avez définie, j'ai mis à jour le champ `base_priority_score` de chaque structure pour que le moteur de règles puisse les départager. 

> [!IMPORTANT]
> **Rappel de vos règles métier :**
> - *Maintien à domicile renforcé* -> **CRT**
> - *Maintien à domicile classique* -> **CLIC** (ou UTS si pas de CLIC)
> - *Si CCAS avec assistante sociale* -> **CCAS** priorisé sur UTS
> - *Besoin de coordination / Refus de soins / Problématiques multiples* -> **DAC**

### Scores de priorité mis en place :
1. **DAC (Score : 100)** : Priorité maximale. J'ai ajouté les conditions "refus_de_soins", "coordination" et "complexite_medico_sociale" dans les critères de déclenchement.
2. **CEV (Score : 95)** : Cellule d'écoute et vigilance, urgence et danger (conservé très haut car relatif au danger).
3. **CRT (Score : 90)** : Déclenchée pour le maintien à domicile *renforcé*.
4. **CLIC (Score : 80)** : Déclenchée pour le maintien à domicile *classique*.
5. **CCAS (Score : 75)** : Priorisé par rapport à l'UTS en cas de besoin d'assistante sociale.
6. **CPTS (Score : 65)** : Recherche de médecin traitant.
7. **UTS (Score : 60)** : Structure de recours (fallback) si pas de CLIC ou CCAS compétent sur le territoire.

*J'ai exécuté un script qui a automatiquement mis à jour le fichier `orientation_rules.json` sur votre machine avec ces nouveaux scores et critères.*

---

## 4. Prochaines Étapes : Par où commencer pour la V1 ?

Pour développer le prototype, voici l'ordre recommandé :

1. **Le Moteur d'Extraction LLM**
   - Rédiger le prompt système pour un modèle LLM (ex: GPT-4 ou Gemini) qui lui donne comme instruction : *"Voici une note vocale transcrite, remplis le JSON suivant exactement selon ce `schema_definition.json`."*
2. **Le Moteur de Règles (Backend)**
   - Développer un script (en Python ou JavaScript) qui prend le `schema_pivot.json` généré par le LLM, et le compare aux `orientation_rules.json`.
   - Il doit renvoyer la structure avec le **plus haut score** (`base_priority_score`) parmi celles qui sont "éligibles" (où les conditions `all_of`, `any_of` sont respectées).
3. **La Génération du Document**
   - Créer un modèle (template) pour la "fiche d'orientation".
   - Utiliser un script pour remplacer les variables du template avec les données du `schema_pivot.json`.
4. **L'Interface Utilisateur (Frontend)**
   - Une interface simple (web ou mobile) avec un gros bouton "Enregistrer une note vocale", qui envoie l'audio au backend, et affiche le résultat (Orientation proposée + Bouton "Télécharger la fiche").

**Questions pour vous :**
- Comment souhaitez-vous gérer la notion de "territoire" ? Actuellement le fichier ne précise pas géographiquement comment savoir s'il y a un CLIC ou non. Souhaitez-vous qu'on utilise un référentiel (codes postaux) dans une prochaine étape ?
- Voulez-vous qu'on commence tout de suite par écrire le script du moteur de règles ou le prompt de l'IA pour l'extraction ?
