# 🚉 Prédiction de l'Affluence dans les Transports Publics (IA & Data)

Ce projet vise à modéliser et prédire l'affluence horaire dans les stations de transport (Métro/RER) en fonction de paramètres temporels et contextuels. 

## 🎯 Objectifs du Projet
1. **Analyse de données** : Traitement des données réelles de trafic (Open Data RATP 2021).
2. **Data Augmentation** : Simulation d'un dataset temporel dynamique (cycles horaires, jours de la semaine).
3. **Machine Learning** : Entraînement d'un modèle capable de prédire l'affluence future.
4. **Visualisation** : Création d'un dashboard interactif pour l'aide à la décision.

## 🛠️ Stack Technique
* **Langage** : Python 3.9 (Environnement Anaconda)
* **Data Science** : Pandas, Numpy
* **Machine Learning** : Scikit-Learn (Random Forest Regressor)
* **Visualisation** : Matplotlib, Seaborn
* **Interface / Dashboard** : Streamlit

## 📊 Fonctionnement du Modèle
Le modèle prend en entrée 5 variables clés :
- **L'ID de la station** (encodé via LabelEncoder)
- **L'heure de la journée** (0-23h)
- **Le jour de la semaine** (0=Lundi, 6=Dimanche)
- **Le type de jour** (Ouvré ou Week-end)
- **La météo** (0=Beau temps, 1=Intempéries)

Le modèle utilise une **Forêt Aléatoire (Random Forest)** pour capturer les relations non-linéaires, notamment les pics d'affluence du matin et du soir.

## 🚀 Installation et Lancement

1. **Cloner le projet** :
   ```bash
   git clone <ton-lien-github-ici>
   cd projet-ia-transports


2. **Installer les dépendances** :

    ```Bash

    pip install pandas scikit-learn streamlit matplotlib seaborn


3. **Lancer le Dashboard** :

    ```Bash

    streamlit run app.py


## 📈 Résultats

**Précision du modèle (R²)**: ~0.98 (sur données simulées).

**Interface** : Dashboard dynamique permettant de tester des scénarios "What-if" (ex: influence de la pluie un dimanche après-midi).

Projet réalisé dans le cadre d'une étude sur l'Intelligence Artificielle appliquée à la Smart City.