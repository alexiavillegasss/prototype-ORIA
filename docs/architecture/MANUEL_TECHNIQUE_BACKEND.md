# 📘 MANUEL TECHNIQUE COMPLET - PROTOTYPE ORIA

## 1. ARCHITECTURE GLOBALE ET FONCTIONNEMENT

# Architecture Technique du Prototype ORIA

Ce document détaille le fonctionnement interne du moteur d'orientation ORIA. Le système repose sur une architecture **hybride**, combinant la puissance de compréhension des **LLM (Large Language Models)** et la rigueur des **systèmes experts (moteurs de règles, "arbres décisionnels")**.

---

## Le Pipeline ORIA en 4 Étapes

### 1. L'Extraction Intelligente (LLM Text to Schéma Pivot)
*   **Composant** : `SignalExtractor` (situé dans `backend/src/ai/extraction/extractor.py`)
*   **Technologie** : LLM (Llama 3) + Schéma Pivot JSON.
*   **Rôle** : C'est la phase de compréhension. Le système reçoit un récit libre (écrit pour le moment). L'IA analyse le texte pour identifier les signaux faibles parmi 30 critères cliniques et sociaux (Base COMID).
*   **Exemple** : "Il ne mange plus et son fils lui prend son argent" → *L'IA extrait : `Dénutrition: OUI`, `Spoliation: OUI`, `Vulnérabilité sociale: CRITIQUE`.*

### 2. Le Scoring de Complexité (Algorithme Déterministe)
*   **Composant** : `ScoringEngine` (situé dans `backend/src/application/scoring_engine.py`)
*   **Technologie** : Python (Logique mathématique).
*   **Rôle** : Pour garantir la fiabilité, le calcul du score n'est pas laissé à l'IA. Un algorithme précis additionne les poids de chaque signal extrait, en se basant sur le fonctionnement de la grille COMID.
*   **Classification** :
    *   **0 - 8** : Situation non complexe (Orientation préventive).
    *   **9 - 15** : Situation à risque de complexité (Coordination nécessaire).
    *   **16+** : Situation très complexe (Urgence médico-sociale).

### 3. Le Moteur d'Orientation (Règles Métier)
*   **Composant** : `OrientationEngine` (situé dans `backend/src/application/orientation_engine.py`)
*   **Technologie** : Moteur de règles JSON (`orientation_rules.json`).
*   **Rôle** : C'est ici que l'expertise humaine intervient. Le système confronte les données extraites à des règles métier strictes discutées lors du GT ORIA avec les coordos de l'antenne de Toulon (âge, APA en place, danger imminent...).
*   **Décision** : Le moteur trie les structures par priorité. Par exemple, si une maltraitance est détectée, la structure de protection (CEV) remonte automatiquement en priorité n°1, écrasant les autres.

### 4. Le Maillage Territorial (Base de Données)
*   **Composant** : `TerritoryManager` (situé dans `backend/src/application/territory_manager.py`)
*   **Technologie** : Référentiel Territorial JSON (Extensible vers SQL si plus de données).
*   **Rôle** : ORIA transforme une décision théorique en une action réelle. Il va chercher dans la base les contacts exacts (nom, téléphone, adresse) de la structure choisie, en fonction de la commune de l'usager.

---

## Pourquoi cette architecture "Hybride" ?

|       Caractéristique        |         IA Pure (Chatbot)         |                    Architecture ORIA                      |
| :--------------------------- | :-------------------------------: | :--------------------------------------------------------:|
| **Fiabilité**                |       Risque d'hallucinations     |           **100% Fiable** (Calculs mathématiques)         |
| **Explicabilité**            |          "Boîte noire"            |      **Transparente** (On voit chaque règle activée)      |
| **Mise à jour**              |       ré-entraînement long        |   **Immédiate** (On modifie juste le fichier de règles)   |
| **Sécurité**                 |     Peut inventer des contacts    |    **Vérifiée** (S'appuie sur un référentiel officiel)    |

---

## Stack Technique
*   **Langage** : Python 3.12
*   **IA (Extraction)** : **Llama 3** (via **Ollama**) - *Choix privilégié pour la confidentialité des données (traitement local).*
*   **IA (Optionnelle)** : Compatible OpenAI API (GPT-4) pour les synthèses complexes, juste à modifier dans llm_client.py pour changer le modèle.
*   **Données** : JSON (pour la flexibilité du prototype)
*   **Validation** : Suite de 20 tests unitaires de simulation humaine.


## 2. ARBORESCENCE ET RÔLES DES FICHIERS

📂 BACKEND (Le moteur)
- `backend/src/main.py` : Point d'entrée principal de l'API. Orchestre la réception des récits et l'envoi des résultats.
- `backend/src/ai/extraction/extractor.py` : Le "cerveau" de l'extraction. Transforme le texte libre en données structurées.
- `backend/src/infrastructure/llm_client.py` : Gère la communication technique avec le modèle Llama 3 (via Ollama).

📂 APPLICATION (La logique métier)
- `backend/src/application/scoring_engine.py` : Le moteur de calcul officiel du score COMID.
- `backend/src/application/orientation_engine.py` : Le cerveau qui choisit la structure adaptée (CRT, DAC, etc.).
- `backend/src/application/territory_manager.py` : L'annuaire intelligent qui trouve le bon numéro de téléphone selon la ville.

📂 CONFIGURATION (L'intelligence métier)
- `config/schemas/schema_definition.json` : Définition précise de tous les champs du dossier patient (Schéma Pivot).
- `config/rules/COMID.json` : Le barème officiel basé sur la grille COMID pour calculer le score de fragilité (sociale et clinique).
- `config/rules/orientation_rules.json` : Les règles métier qui décident quelle structure est la plus adaptée.
- `config/referentials/referentiel_territoire.json` : Annuaire local permettant de trouver le bon contact selon la zone géographique.
- `config/app_config.yaml` : Configuration technique du projet (modèles utilisés, paramètres système).

📂 DÉPENDANCES ET ENVIRONNEMENT (Le dossier `venv/lib/site-packages`)
- Ce dossier contient toutes les bibliothèques externes installées (FastAPI, Pydantic, PyYAML, etc.). 
- Ce sont les "outils" du projet. On ne modifie jamais ces fichiers ; on les utilise simplement via des `import` dans le code.


## 3. GESTION DE LA BASE DE DONNÉES (SQLITE)

# Documentation de la Base de Données ORIA

Ce document explique le fonctionnement, la structure et le rôle de la base de données intégrée au prototype ORIA.

---

### Pourquoi SQLite ?
Pour ce prototype, nous avons choisi **SQLite**. Contrairement aux bases de données lourdes (comme MySQL ou PostgreSQL) qui nécessitent l'installation de gros serveurs, SQLite est **intégré nativement dans Python**. 
* **Avantage :** Toute la base de données est contenue dans un seul et unique fichier local.
* **Lieu de stockage :** Le fichier s'appelle `oria_database.db` et se trouve à la racine du projet.

### Le module Python (`DatabaseManager`)
Le fichier qui fait le pont entre le moteur ORIA et la base de données se trouve ici :
`backend/src/infrastructure/database.py`

Il a deux rôles principaux :
1. **Créer la table** si elle n'existe pas au démarrage.
2. **Sauvegarder les données** (fonction `save_dossier()`) après chaque analyse de l'IA. Pour que les dictionnaires Python puissent être stockés, ce fichier les transforme automatiquement en texte (format JSON).

### Structure de la Table principale : `dossiers_patients`
C'est ici que l'historique complet de chaque patient est enregistré. Les colonnes (champs) qui composent cette table sont:

|       Nom de la colonne      | Type de donnée |                                            Description                                           |
| :----------------------------| :------------- | :----------------------------------------------------------------------------------------------  |
| **`id`**                     |      INT       |           L'identifiant unique du dossier (Numéro de patient). Il s'incrémente tout seul.        |
| **`date_creation`**          |      TEXT      |                     La date et l'heure exactes où l'analyse a été effectuée.                     |
| **`texte_original`**         |      TEXT      |            Le récit brut du patient ou du professionnel (ce qui a été envoyé à l'IA).            |
| **`donnees_extraites`**      |   TEXT (JSON)  |            Le "Schéma Pivot" rempli par Llama 3 (variables cliniques, sociales, etc.)            |
| **`score_comid`**            |      INT       |                    Le score de complexité mathématique (ex: 13).                                 |
| **`niveau_comid`**           |      TEXT      |             Le label textuel de la complexité (ex: "Situation complexe").                        |
| **`structures_orientations`**|   TEXT (JSON)  |        La recommandation finale du moteur, incluant la priorité, le contact et l'objectif.       |

### C'est quoi la table `sqlite_sequence` ?
Quand on ouvre la base de données, on voit une deuxième table appelée `sqlite_sequence`. 
C'est une table système générée automatiquement par SQLite. 
* **Son rôle :** Elle mémorise le dernier `id` utilisé. Si on supprime le dossier numéro 10, cette table permet à SQLite de se souvenir qu'il ne faut pas réutiliser le 10, et que le prochain dossier devra obligatoirement être le numéro 11. C'est la garantie que chaque patient a un identifiant unique à vie.

### Comment visualiser la base de données ?
Puisque le fichier `oria_database.db` est un fichier binaire, on peut le visualiser grâce à l'extension **"SQLite Viewer"**. 


## 4. HISTORIQUE D'OPTIMISATION DE L'IA

# Journal d'Optimisation de l'IA ORIA

Ce fichier consigne uniquement les améliorations apportées au **moteur d'extraction IA** et aux **règles de scoring** pour affiner la précision clinique.

## Améliorations du Moteur d'Extraction

### 1. Stratégie de Précision : Dictionnaire de Synonymes vs RAG
Pour maximiser la précision de détection sans alourdir le système, nous avons choisi une approche par **"Dictionnaire Dynamique"** injecté dans le prompt :
- **Le Choix** : Chaque critère dans `COMID.json` possède une liste d'exemples/synonymes (ex: Alzheimer pour troubles cognitifs).
- **Pourquoi pas le RAG (Retrieval Augmented Generation) ?** : Le RAG est indispensable pour des milliers de documents. Pour nos 30 critères cliniques, le RAG ajouterait une complexité technique (base de données vectorielle, modèles d'embeddings) disproportionnée. 
- **L'Avantage** : Cette méthode est "Data-Driven". On peut affiner l'intelligence de l'IA simplement en ajoutant des mots-clés dans le fichier JSON, sans toucher à une seule ligne de code Python. C'est le meilleur équilibre entre puissance et simplicité de maintenance pour ce prototype.

### 2. Précision de l'Extraction (Prompt Engineering)
- **Problème** : L'IA "oubliait" d'extraire des données pivots (âge, ville) car elle était submergée par les 30 critères COMID à évaluer simultanément.
- **Solution** : 
    - Restructuration du prompt dans `extractor.py` avec une hiérarchie stricte.
    - Ajout d'une section **"INSTRUCTIONS CRITIQUES"** imposant l'extraction prioritaire de l'âge, de la ville et du statut APA.
- **Résultat** : Récupération systématique des données administratives de base, même sur des récits longs.

### 3. Raisonnement Avancé (Chain of Thought)
- **Problème** : L'IA était trop timide et manquait des critères complexes en appliquant une logique purement littérale (si le mot exact n'y est pas, elle ne trouve rien).
- **Solution** : Modification de `extractor.py` pour implémenter la technique du **Chain of Thought** (Chaîne de pensée). On oblige l'IA à écrire une **justification (preuve) étape par étape** avant de prendre sa décision pour chaque item COMID.
- **Résultat** : Amélioration de la détection des signaux faibles et augmentation de la pertinence du score de complexité global.

**Comment la "Chain of Thought" permet-elle à l'IA de déduire des informations non-écrites ?**
Pour comprendre la magie de la déduction de l'IA (comme déduire le critère "Danger" à partir de la phrase "Madame Durand sort dans la rue en chemise de nuit"), il faut combiner deux principes de son fonctionnement :
1. **Sa "culture générale" (Le pré-entraînement)** : Le modèle (Llama 3) a "lu" une grande partie d'internet avant d'arriver sur notre machine. Dans son réseau de neurones, les concepts de `nuit` + `extérieur` + `chemise de nuit` sont mathématiquement très liés aux concepts de `froid`, d'`accident` ou d'`hypothermie`.
2. **La prédiction du mot suivant** : Un modèle génère du texte mot par mot en devinant la suite logique. Si on lui demande brutalement "Y a-t-il un danger ?", il peut répondre "Non" trop vite car le mot "danger" est absent. Mais avec la *Chain of Thought*, on le force à justifier. L'IA va d'abord écrire son observation : *"Fait observé : errance nocturne"*. En écrivant cela, son réseau de neurones s'active sur les concepts liés, ce qui l'amène à déduire et à écrire la conséquence : *"Conséquence : risque d'hypothermie"*. Une fois le mot "hypothermie" écrit, la conclusion mathématiquement inévitable pour la suite de la phrase devient : *"Déduction : Danger = OUI"*. 
L'acte de forcer l'IA à "réfléchir à voix haute" permet ainsi de débloquer et d'utiliser ses connaissances latentes ! La ligne de code qui permet cela est dans le fichier 'extractor.py', ligne 60.

### 4. Simplification du Référentiel (Codes courts)
- **Problème** : Les codes d'items trop longs (ex: `lourdeur_emotionnelle_ou_physique_...`) étaient mal gérés par l'IA, causant des oublis.
- **Solution** : 
    - Simplification drastique de `COMID.json` avec des codes courts (ex: `lourdeur_reseau`).
    - Mise à jour du prompt pour utiliser ces nouveaux codes comme "ancres" logiques.
- **Résultat** : Meilleure fiabilité de l'extraction et scoring plus cohérent.


## 5. INTERACTIONS ET FONCTIONS DES FICHIERS (Le Workflow ORIA)

Cette section explique comment les fichiers "se parlent" entre eux lorsqu'un nouveau patient est analysé. Pour bien comprendre, le parallèle est fait avec une véritable équipe médicale.
### Étape 1 : La réception (`main.py` - Le Chef d'Orchestre)
*   **Fonction appelée** : `analyze(request: AnalyzeRequest)`
*   **Le Concept** : C'est la porte d'entrée. Le chef d'orchestre reçoit l'histoire brute du patient. Il ne sait rien faire lui-même, mais il connaît le numéro de téléphone de tous les experts (les autres fichiers) et va les appeler un par un dans le bon ordre.

### Étape 2 : La compréhension (`extractor.py` - Le Traducteur)
*   **Fonction appelée par le chef** : `extractor.extract(request.text)`
*   **Le Concept** : Le chef d'orchestre donne le texte à l'extracteur. L'extracteur lit le formulaire vierge (`schema_definition.json`) et demande à l'IA Llama 3 (`llm_client.py`) de lire le texte et de cocher les bonnes cases. 
*   **Résultat transmis à l'étape suivante** : Un formulaire rempli proprement (âge, ville, apa, pch, medecin traitant, hospitalisation,urgence, malveillance, motif principal, isolement, et tous les critères comid en true ou false)--> LE TRAVAIL DE L'IA EST TERMINÉ, ON PASSE AU CALCUL PUR ET DUR GRACE AUX MOTEURS.

### Étape 3 : L'évaluation clinique (`scoring_engine.py` - Le Docteur Mathématicien)
*   **Fonction appelée par le chef** : `scoring_engine.calculate_comid_score(extracted_data)`
*   **Le Concept** : Le chef donne le formulaire rempli au "Docteur". Ce docteur prend le barème officiel COMID (`COMID.json`), et additionne les points de manière 100% mathématique et transparente.
*   **Résultat transmis à l'étape suivante** : Le score total (ex: 13/30) et la classification ("Situation complexe").

### Étape 4 : Le choix de la structure (`orientation_engine.py` - Le Juge)
*   **Fonction appelée par le chef** : `orientation_engine.evaluate_orientation(...)`
*   **Le Concept** : C'est le cerveau métier. Le chef donne le dossier (formulaire + score COMID) au Juge. Le Juge ouvre son livre des lois (`orientation_rules.json`) et vérifie si le patient passe les 3 portes d'éligibilité (`all_of`, `any_of`, `none_of`) pour chaque structure (DAC, CRT, CEV...). 
*   **Résultat transmis à l'étape suivante** : Une liste triée des gagnants (ex: Le CRT est la priorité n°1 car urgence détectée).

### Étape 5 : La recherche du contact (`territory_manager.py` - L'Opérateur Téléphonique)
*   **Fonction appelée par le chef** : `territory_manager.get_contacts_for_structures(...)`
*   **Le Concept** : Le chef sait qu'il faut envoyer le patient au "CRT", mais où ? Il demande à l'Opérateur de chercher dans son annuaire (`referentiel_territoire.json`). L'Opérateur regarde la ville du patient (ex: Toulon) et trouve le vrai numéro de téléphone de la structure locale.
*   **Résultat transmis à l'étape suivante** : La fiche contact complète et prête à l'emploi.

### Étape 6 : La mémoire (`database.py` - L'Archiviste)
*   **Fonction appelée par le chef** : `db_manager.save_dossier(...)`
*   **Le Concept** : Avant de rendre sa conclusion, le chef d'orchestre demande à l'Archiviste de prendre tout le dossier, le score, l'orientation et le numéro de téléphone, et de les graver de façon permanente dans le coffre-fort (`oria_database.db`). 

*(Fin du workflow : Le Chef d'Orchestre `main.py` reprend tous ces documents validés, et les affiche à l'écran !)*


## 6. LA MAGIE DE L'OBJET (L'Injection de Dépendances)

Une grande force de cette architecture (basée sur la Programmation Orientée Objet) est que nos fichiers Python (comme `orientation_engine.py`) sont complètement **aveugles**.
Ils ne contiennent aucun chemin écrit "en dur" (pas de `C:/Users/...`).

**Exemple : Le moteur d'orientation ne sait pas où sont rangées ses propres règles.**
Quand on ouvre le fichier, il dit simplement : *"Donnez-moi un chemin d'accès (`rules_path`), et je l'ouvrirai."*

**Où ça se décide alors ?**
C'est le chef d'orchestre (`main.py`) qui fait ce lien ! C'est lui qui sait où se trouve le fichier JSON et qui le donne au moteur au moment du démarrage :
```python
# main.py définit le chemin de votre choix :
CHEMIN_REGLES = "config/rules/orientation_rules.json"

# Et il "branche" ce fichier dans le moteur :
moteur = OrientationEngine(rules_path=CHEMIN_REGLES)
```

**Pourquoi c'est surpuissant ?**
Parce que demain, si l'on souhaite créer des règles spécifiques pour les enfants, nous n'aurons **pas besoin de réécrire le moteur Python**. Il suffira de créer un nouveau petit fichier JSON, et de dire au chef d'orchestre d'allumer un deuxième moteur en parallèle :
```python
moteur_adultes = OrientationEngine(rules_path="regles_adultes.json")
moteur_enfants = OrientationEngine(rules_path="regles_enfants.json")
```
Un seul fichier de code Python permet ainsi de faire tourner une infinité de cerveaux différents !


## 7. LA STRUCTURE LOGIQUE DES RÈGLES (Comment fonctionne le ET / OU)

Dans le fichier `orientation_rules.json`, chaque bloc de règle d'une structure (comme le DAC ou le CRT) est évalué selon une structure de filtres stricte :
* **`all_of`** : *Toutes* les conditions listées ici doivent être validées en même temps (**Logique ET**).
* **`any_of`** : *Au moins une* des conditions listées ici doit être validée (**Logique OU**).
* **`none_of`** : *Aucune* des conditions listées ici ne doit être validée (**Logique NON**).

### Pourquoi découper une structure en plusieurs règles (Exemple du DAC) ?
Le moteur de règles d'ORIA est conçu de façon simple et robuste. Il n'autorise pas d'écritures complexes ou imbriquées du type : `Déclencher si (A OU B) OU (C ET D)` au sein d'un unique bloc.

Si l'on essayait de tout fusionner dans le bloc principal du DAC :
* Mettre `GIR [1,2,3]` et `aidant_regulier == non` dans `any_of` déclencherait le DAC par erreur pour une personne autonome (GIR 6) uniquement parce qu'elle vit seule.
* Pour le DAC, on veut détecter la **combinaison simultanée** : un patient lourdement dépendant **ET** sans aidant de proximité.

**La solution élégante d'ORIA :**
Puisque le moteur accepte d'avoir plusieurs blocs de règles ciblant le même type de structure (`structure_type: "DAC"`), nous découpons simplement la logique en plusieurs sous-règles autonomes :
* **Règle 1 (`eligibility_dac_01`)** : Les déclencheurs généraux classiques du DAC (ex: refus de soins, rupture de parcours, suspicion de maltraitance...).
* **Règle 2 (`eligibility_dac_02`)** : Déclencheur spécifique dépendance + solitude (GIR 1-3 **ET** pas d'aidant).
* **Règle 3 (`eligibility_dac_03`)** : Déclencheur spécifique réseau saturé (Professionnels déjà présents **ET** complexité du dossier avérée).

Le moteur d'orientation évalue chaque règle de façon séquentielle. Si la Règle 1 **OU** la Règle 2 **OU** la Règle 3 est validée, le patient sera éligible au DAC avec la justification précise associée au déclencheur qui a gagné !


## 8. LE DÉTERMINISME ABSOLU DE L'IA (Température = 0.0)

Dans l'aide à la décision médico-sociale, **l'imprévisibilité et la non-reproductibilité ne sont pas acceptables**. Pour garantir qu'un même patient reçoive rigoureusement les mêmes orientations, ORIA neutralise le hasard inhérent aux modèles de langage génératifs.

* **Le défi (Température par défaut ~ 0.8)** : Les LLM génèrent du texte de manière probabiliste. Une température élevée induit de la créativité et de la variabilité dans la détection des signaux cliniques (COMID). Un même dossier peut donc obtenir des scores fluctuants (ex: 10, puis 19) d'une seconde à l'autre.
* **La solution d'ORIA (Température = 0.0)** : Le client LLM (`llm_client.py`) configure explicitement le paramètre `"temperature": 0.0` dans l'API d'Ollama :
  ```json
  "options": {
      "temperature": 0.0
  }
  ```
* **Le bénéfice** : L'IA sélectionne systématiquement le chemin logique ayant la plus haute certitude mathématique. L'extraction devient 100% stable, factuelle, et scientifiquement reproductible (le même texte produira toujours le même score et les mêmes fiches contacts).

> [!TIP]
> **Complémentarité CoT & Température 0.0** : La température à `0.0` n'entrave pas la *Chain of Thought*. Au contraire, elles se renforcent mutuellement : la CoT force l'IA à décomposer son raisonnement clinique pas à pas, tandis que la température à `0.0` garantit que chaque étape de ce raisonnement soit guidée par la logique la plus rigoureuse et 100% reproductible (sans dérive ni bruit aléatoire).

---

###############################################################################
# ANNEXE : LOGIQUE DÉCISIONNELLE DE L'ORIENTATION (V1.1)
###############################################################################

Le moteur d'orientation ORIA utilise un système de filtres éliminatoires (All Of), de signaux positifs (Any Of) et de priorités numériques (0-100).

### Comment les priorités sont-elles choisies (Le rôle d'arbitre) ?
Lorsqu'un patient complexe coche beaucoup de cases, il peut être théoriquement éligible à plusieurs structures en même temps (ex: sans médecin -> CPTS, âgé avec besoin d'aide -> CLIC, situation complexe -> DAC). Le score de priorité (de 100 à 60) permet de résoudre ces "collisions" en classant les résultats. La structure avec le plus gros score arrive toujours en haut de la liste.

Cette échelle n'est pas calculée par l'IA, elle est définie à l'avance par des experts métier. Elle a été pensée comme un **entonnoir des urgences et des obligations légales** :

* **Priorité Absolue (100 - 95) : Obligations et urgences vitales**
  (Ex: PSCG pour l'APA, ou CEV pour la maltraitance). Le besoin de protéger (danger) ou de respecter le circuit légal départemental écrase toutes les autres demandes.
* **Haute Complexité (90 - 85) : L'intervention lourde et la coordination**
  (Ex: DAC ou CRT). Si le patient relève d'une coordination complexe, la structure spécialisée prend le pas sur les guichets de base. Le DAC ne fait pas forcément "à la place des autres", mais il devient le coordinateur : face à une situation bloquée, des aides inefficaces ou un patient perdu, c'est le DAC qui va solliciter et coordonner les autres structures (ex: contacter la CPTS pour le médecin traitant) pour remettre le parcours en marche.
* **Première Ligne / Administratif (80 - 60) : Le guichet standard**
  (Ex: CLIC, ASPI, CCAS). Ce sont les solutions "par défaut". Si aucune grande urgence (95) ou extrême complexité (85) n'est détectée, ce sont ces guichets qui remportent "le match" de l'orientation.


1. **PSCG SS APA (Priorité 100)**
   - Condition : APA déjà en place (OUI).
   - Rôle : Redirection vers le référent départemental unique.

2. **CEV - Cellule Écoute et Vigilance (Priorité 95)**
   - Signaux : Maltraitances (tous types), danger habitat, urgence critique.
   - Note : Peut générer un signalement au Procureur.

3. **Service Social de l'Hôpital (Priorité 95)**
   - Signaux : Patient actuellement hospitalisé ou sortie récente (< 10 jours).
   - Rôle : Organisation de la sortie et lien ville-hôpital.

4. **CRT - Centre de Ressources Territorial (Priorité 90)**
   - Condition : Âge >= 60 ans.
   - Signaux : GIR 1-4, refus d'aide, besoin de maintien à domicile intensif.

5. **DAC - Dispositif d'Appui à la Coordination (Priorité 85)**
   - Condition : Complexité élevée (Score COMID >= 10).
   - Signaux : Rupture de parcours, conflit professionnel, épuisement aidant.
   - Rôle : Coordination de dernier recours pour situations bloquées.

6. **CLIC - Centre Local d'Information (Priorité 80)**
   - Condition : APA = NON + Demande de maintien à domicile.
   - Signaux : Âge >= 60 ans ou PCH, besoin d'organisation d'aides.

7. **UTS / ASPI - Service Social Départemental (Priorité 70)**
   - Condition : APA = NON.
   - Signaux : Précarité, RSA, violences conjugales, gestion budget, logement.

8. **CPTS - Accès aux Soins (Priorité 65)**
   - Signaux : Absence de médecin traitant (justifiée), dispositif MISAS (60+).

9. **CCAS - Premier Accueil (Priorité 60)**
   - Condition : APA = NON.
   - Signaux : Demandes d'informations générales, aides facultatives communales.
