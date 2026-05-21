# 🧠 ORIA - Assistant Intelligent d'Orientation Médico-Sociale (Var, 83)

ORIA est un prototype innovant d'aide à la décision territoriale et clinique. Il combine l'intelligence artificielle générative locale (**Llama 3 via Ollama**) et un moteur de règles métier **100% déterministe** pour analyser les récits de vie des personnes âgées vulnérables et les orienter instantanément vers les bonnes structures d'aide (DAC, CRT, CLIC, UTS, CCAS, CEV...).

---

## 🛠️ Architecture du Pipeline ORIA

Le traitement d'une situation patient suit une chaîne de responsabilité stricte et optimisée :

1. **SignalExtractor (IA local, Temp=0.0)** : Analyse le texte libre décrivant la situation, détecte les 30 indicateurs de vulnérabilité clinique/sociale (COMID) et extrait les données administratives clés (GIR, APA, Commune).
2. **ScoringEngine (Déterministe)** : Calcule le score de complexité COMID global et catégorise le niveau de complexité (Simple, À risque, Complexe).
3. **OrientationEngine (Moteur de Règles)** : Filtre et priorise les structures éligibles. Les doublons de structures sont fusionnés de manière ergonomique avec regroupement des justifications cliniques en liste à puces.
4. **TerritoryManager (Localisation)** : Recherche les coordonnées physiques (téléphone, adresse) des structures élues dans le référentiel territorial varois (Toulon, La Garde, La Valette, Ollioules, etc.).
5. **DatabaseManager (SQLite)** : Archive l'intégralité du dossier (récit, extraction IA, score, orientations et contacts) dans la base `oria_database.db`.

---

## 🚀 Démarrage Rapide

### 1. Prérequis & IA Locale
Assurez-vous qu'Ollama est démarré sur votre machine et que le modèle Llama 3 est chargé :
```bash
ollama run llama3
```

### 2. Lancer les simulations de tests
Les tests de simulation permettent de valider toute la chaîne décisionnelle.
```bash
# Tester le cas de M. Gilbert (Toulon - Dépendance & saturation)
python tests_simulation/test_mr_gilbert.py

# Tester le cas de Mme Antoinette (La Garde - Épuisement aidant & refus de SAAD)
python tests_simulation/test_mme_antoinette.py

# Tester le cas de Mme Huguette (La Valette - Spoliation financière & protection d'urgence)
python tests_simulation/test_mme_huguette.py
```

### 3. Démarrer le serveur API (FastAPI)
Pour lancer le serveur de production locale en arrière-plan :
```bash
cd backend/src
uvicorn main:app --reload
```
L'API sera accessible sur `http://localhost:8000`. L'endpoint `/analyze` permet de soumettre des textes libres pour obtenir l'orientation complète en JSON.

---

## 📂 Organisation de la Documentation

Toute l'intelligence conceptuelle et métier du projet est documentée dans le dossier `docs/` :
* **[`docs/architecture/MANUEL_TECHNIQUE_BACKEND.md`](file:///c:/Users/alexi/Desktop/prototype-ORIA/docs/architecture/MANUEL_TECHNIQUE_BACKEND.md)** : Fonctionnement interne de l'injection de dépendance, du moteur de règles (ET/OU), et explication du déterminisme absolu de l'IA (Température = 0.0).
* **[`docs/metier/RECAP_SIMULATIONS_CAS_PATIENTS.md`](file:///c:/Users/alexi/Desktop/prototype-ORIA/docs/metier/RECAP_SIMULATIONS_CAS_PATIENTS.md)** : Journal de bord contenant l'intégralité des **23 cas patients réels** testés et validés par le moteur décisionnel d'ORIA.
* **[`docs/Cadre/cadrage_et_retour_oria_v2.md`](file:///c:/Users/alexi/Desktop/prototype-ORIA/docs/Cadre/cadrage_et_retour_oria_v2.md)** : Cadrage métier historique et retours d'expérience du projet.
