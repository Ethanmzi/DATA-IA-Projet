import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Prédiction Affluence RATP", layout="wide")

st.title("📊 Prédiction de l'affluence dans les transports")

# Chargement des données et entraînement rapide du modèle
@st.cache_data
def load_and_train():
    # On utilise le dataset temporel qui contient les colonnes 'affluence', 'heure', etc.
    df = pd.read_csv('dataset_pret_pour_ml.csv')
    
    le = LabelEncoder()
    # On s'assure que la colonne station est bien traitée
    df['station_id'] = le.fit_transform(df['station'])
    
    # Définition des caractéristiques pour l'IA
    features = ['station_id', 'heure', 'jour_semaine', 'est_weekend', 'meteo']
    
    # Entraînement du modèle
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(df[features], df['affluence'])
    
    return df, model, le

# Initialisation du dataframe, du modèle et de l'encodeur
df, model, le = load_and_train()

# Barre latérale pour les filtres
st.sidebar.header("Paramètres de simulation")
station_sel = st.sidebar.selectbox("Choisir une station", df['station'].unique())
jour_sel = st.sidebar.slider("Jour de la semaine (0=Lundi, 6=Dimanche)", 0, 6, 0)
meteo_sel = st.sidebar.radio("Météo", ["Beau temps", "Pluie / Froid"])
meteo_val = 1 if meteo_sel == "Pluie / Froid" else 0

# Calcul des prédictions pour toute la journée (24h)
heures = np.arange(0, 24)
station_id = le.transform([station_sel])[0]
est_weekend = 1 if jour_sel >= 5 else 0

# Création du tableau de données pour la prédiction
inputs = pd.DataFrame({
    'station_id': [station_id]*24,
    'heure': heures,
    'jour_semaine': [jour_sel]*24,
    'est_weekend': [est_weekend]*24,
    'meteo': [meteo_val]*24
})

predictions = model.predict(inputs)

# Affichage des résultats sur deux colonnes
col1, col2 = st.columns([1, 2])

with col1:
    st.metric("Affluence Totale Journalière", f"{int(sum(predictions))} voyageurs")
    st.write(f"Scénario pour la station : **{station_sel}**")
    st.write(f"Jour sélectionné : **{jour_sel}** (0=Lun, 6=Dim)")
    st.info("Ce dashboard utilise un modèle de Forêt Aléatoire pour prédire les pics de fréquentation.")

with col2:
    # Préparation des données pour le graphique
    chart_data = pd.DataFrame({'Heure': heures, 'Affluence prédite': predictions})
    st.subheader("Courbe d'affluence prévisionnelle")
    st.line_chart(chart_data.set_index('Heure'))