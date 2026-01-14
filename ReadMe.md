# 🚉 Prédiction de l'Affluence dans les Transports Publics (IA)

Ce projet complet de Data Science vise à modéliser, analyser et prédire l'affluence horaire dans les stations du réseau ferré (Métro et RER) en utilisant des données réelles et du Machine Learning.

## 🎯 Objectifs du Projet
1. **Nettoyage de Données** : Ordonner et structurer les données Open Data RATP 2021.
2. **Analyse de Données (EDA)** : Identifier les pôles majeurs par ville et arrondissement.
3. **Simulation Temporelle** : Créer un dataset dynamique (pics horaires, météo, weekends).
4. **Machine Learning** : Prédire l'affluence via un modèle Random Forest.
5. **Déploiement** : Interface utilisateur interactive avec Streamlit.

## 🛠️ Stack Technique
* **Langage** : Python 3.9 (Distribution Anaconda)
* **Traitement de données** : Pandas, Numpy
* **Visualisation** : Matplotlib, Seaborn
* **Intelligence Artificielle** : Scikit-Learn (Random Forest Regressor)
* **Dashboard** : Streamlit

## 📁 Structure du Projet
* `trafic_2021_ordonne.csv` : Base de données nettoyée et classée par rang de fréquentation.
* `generate_data.py` : Script générant le trafic horaire simulé sur 30 jours.
* `dataset_pret_pour_ml.csv` : Dataset final utilisé pour l'entraînement de l'IA.
* `app.py` : Application Streamlit (le Dashboard interactif).



## 📊 Analyse des Données
Grâce au prétraitement, le projet permet de consulter les données par catégories directement dans Jupyter :
- **Top Villes** : Visualisation des pôles de banlieue (ex: Puteaux, Saint-Denis).
- **Top Arrondissements** : Identification des zones névralgiques parisiennes (10ème, 8ème, 1er).
- **Profils Horaires** : Distinction claire entre les pics "travail" (semaine) et les pics "loisirs" (weekend).



## 🚀 Installation et Utilisation

1. **Initialiser l'environnement** :
   ```bash
   conda activate projet_transport

2. **Générer les données et entraîner le modèle** : Exécuter les cellules du notebook ou le script de simulation pour créer `dataset_pret_pour_ml.csv` .

3. **Lancer le Dashboard** :

    ```Bash

    streamlit run app.py


## 📈 Résultats du Modèle

Le modèle Random Forest atteint une précision (R²) supérieure à 0.95, permettant d'anticiper avec précision les besoins en transport selon :

L'heure de la journée (gestion des heures de pointe).

Le jour de la semaine (semaine vs weekend).

Les conditions météo (impact de la pluie sur le trafic).

Projet réalisé par Ethan et Mayles - Apprenant en Data & IA