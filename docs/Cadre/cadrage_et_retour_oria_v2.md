# Cadrage et Retour sur le Projet ORIA - Prototype (V1.1)

*Document mis à jour suite à nos derniers échanges.*

## 1. Cadrage du Projet ORIA (V1)

**Objectif Principal** : Développer un prototype fonctionnel d'une application permettant aux professionnels sanitaires, sociaux et médico-sociaux du DAC Var Ouest d'orienter efficacement des patients, prioritairement les personnes âgées nécessitant un maintien à domicile, vers les structures les plus adaptées.

### Parcours Utilisateur
1. **Saisie** : Le professionnel, en situation (domicile/cabinet), enregistre une note vocale (ou texte) décrivant la situation clinique, sociale et administrative du patient.
2. **Extraction** : Une Intelligence Artificielle (LLM + Speech-to-Text) transcrit l'audio et structure les informations selon un schéma de données prédéfini (`schema_pivot.json`).
3. **Analyse & Score** : L'IA évalue la complexité/fragilité à l'aide de grilles intégrées (COMID).
4. **Orientation** : Un moteur de règles métier (`orientation_rules.json`) identifie **les** structures les plus pertinentes par domaine d'intervention.
5. **Restitution** : L'application propose les orientations possibles, génère un indice de fragilité et pré-remplit la fiche d'orientation.

### Périmètre de la V1 (Prototype)
- **Cible** : Parcours Personnes Âgées (PA) & Maintien à domicile.
- **Fonctionnalités exclues** : Prédiction des ruptures de parcours (prévu pour plus tard).
- **Structures cibles priorisées** : CRT, CLIC, CCAS, UTS, DAC, CEV, CPTS.

---

## 2. Retour sur l'existant

Vos schémas de données (`schema_pivot.json`, `schema_definition.json`) sont extrêmement complets et la structuration logique (all_of, any_of) des `orientation_rules.json` est parfaite pour un moteur d'inférence.

---

## 3. Évolution des Règles d'Orientation (Suite à vos commentaires)

Vous avez soulevé un point crucial : **les structures ne sont pas appelées pour les mêmes choses**, un simple score de priorité absolu n'est donc pas pertinent car il risquerait d'exclure une structure médicale au profit d'une structure sociale, alors que le patient a besoin des deux.

> [!TIP]
> **Nouvelle approche : Orientation Multi-Domaines**
> Au lieu de donner un score global, le moteur de règles va proposer des orientations catégorisées par "besoin". Par exemple :
> - *Pour la coordination globale* : **DAC** ou **CRT**
> - *Pour l'accompagnement social* : **UTS** ou **CCAS**
> - *Pour le médical* : **CPTS**

### Le cas spécifique UTS vs CCAS (Ordre social)
La règle a été clarifiée selon votre retour : 
- Pour un besoin d'ordre social, **l'UTS est la structure de référence par défaut**.
- **Exception** : Si le CCAS de la commune concernée dispose d'une assistante sociale, alors ce **CCAS prime sur l'UTS**.
- *Cette logique implique l'utilisation d'une base de données territoriale (le référentiel dont vous disposez).*

### Le Référentiel Territorial
L'intégration de votre **référentiel territorial** (que vous possédez déjà) sera la prochaine étape technique essentielle. Il permettra au moteur de savoir :
- Quel est le CLIC compétent sur le code postal du patient.
- Si le CCAS de ce code postal dispose d'une assistante sociale (pour surcharger l'UTS).

---

## 4. Prochaines Étapes Techniques pour la V1

Voici l'ordre recommandé pour la suite du développement :

1. **Intégration du Référentiel Territorial**
   - Importer votre fichier de référentiel (Excel/CSV) et le transformer en base de données ou fichier de configuration pour le lier aux codes postaux.
2. **Le Moteur d'Extraction LLM**
   - Rédiger le prompt système pour un modèle LLM (ex: GPT-4 ou Gemini) qui lui donne comme instruction : *"Voici une note vocale transcrite, remplis le JSON suivant exactement selon ce `schema_definition.json`."*
3. **Le Moteur de Règles (Backend)**
   - Développer le script qui prend le `schema_pivot.json`, lit le `referentiel_territorial`, et évalue les `orientation_rules.json` pour sortir **une liste de structures recommandées par domaine** (et non plus un score unique).
4. **La Génération du Document**
   - Créer un modèle (template) pour la "fiche d'orientation" et injecter les données.
5. **L'Interface Utilisateur (Frontend)**
   - Une interface simple avec un bouton d'enregistrement vocal, affichant le résultat de l'IA et les orientations proposées.
