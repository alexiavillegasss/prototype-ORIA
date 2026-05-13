# 🧠 Journal d'Optimisation de l'IA ORIA

Ce fichier consigne uniquement les améliorations apportées au **moteur d'extraction IA** et aux **règles de scoring** pour affiner la précision clinique.

## 🛠️ Améliorations du Moteur d'Extraction

### 1. Précision de l'Extraction (Prompt Engineering)
- **Problème** : L'IA "oubliait" d'extraire des données pivots (âge, ville) car elle était submergée par les 30 critères COMID à évaluer simultanément.
- **Solution** : 
    - Restructuration du prompt dans `extractor.py` avec une hiérarchie stricte.
    - Ajout d'une section **"INSTRUCTIONS CRITIQUES"** imposant l'extraction prioritaire de l'âge, de la ville et du statut APA.
- **Résultat** : Récupération systématique des données administratives de base, même sur des récits longs.

### 2. Détection des Signaux Faibles (Scoring COMID)
- **Observation** : L'IA est actuellement trop "littérale" (timide). Elle ne coche un critère que si le mot exact est présent.
- **Exemple** : Sur le cas Mme Durand, elle manque la "dégradation rapide" malgré la mention de déambulations nocturnes dangereuses.
- **Action à venir** : Implémenter une étape de **Chaîne de Pensée (Chain of Thought)** pour forcer l'IA à déduire les critères cliniques à partir des faits observés.

### 3. Raisonnement Avancé (Chain of Thought)
- **Problème** : L'IA était trop timide et manquait des critères complexes en appliquant une logique purement littérale.
- **Solution** : 
    - Modification de `extractor.py` pour exiger une **justification (preuve)** pour chaque item COMID.
    - Ajout d'exemples de déductions (ex: Déambulation = Instabilité).
- **Résultat** : Amélioration de la détection des signaux faibles et augmentation de la pertinence du score de complexité global.

---
*Dernière mise à jour : 13/05/2026*
