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
    df = pd.read_csv('dataset_pret_pour_ml.csv')
    le = LabelEncoder()
    df['station_id'] = le.fit_transform(df['station'])
    
    features = ['station_id', 'heure', 'jour_semaine', 'est_weekend', 'meteo']
    model = RandomForestRegressor(n_estimators=50)
    model.fit(df[features], df['affluence'])
    return df, model, le

df, model, le = load_and_train()

# Barre latérale pour les filtres
st.sidebar.header("Paramètres de simulation")
station_sel = st.sidebar.selectbox("Choisir une station", df['station'].unique())
jour_sel = st.sidebar.slider("Jour de la semaine (0=Lundi, 6=Dimanche)", 0, 6, 0)
meteo_sel = st.sidebar.radio("Météo", ["Beau temps", "Pluie / Froid"])
meteo_val = 1 if meteo_sel == "Pluie / Froid" else 0

# Calcul des prédictions pour toute la journée
heures = np.arange(0, 24)
station_id = le.transform([station_sel])[0]
est_weekend = 1 if jour_sel >= 5 else 0

inputs = pd.DataFrame({
    'station_id': [station_id]*24,
    'heure': heures,
    'jour_semaine': [jour_sel]*24,
    'est_weekend': [est_weekend]*24,
    'meteo': [meteo_val]*24
})

predictions = model.predict(inputs)

# Affichage des résultats
col1, col2 = st.columns([1, 2])

with col1:
    st.metric("Affluence Totale Estimée", f"{int(sum(predictions))} pers.")
    st.write(f"Scénario pour : **{station_sel}**")
    st.info("Ce dashboard utilise le modèle Random Forest entraîné précédemment.")

with col2:
    chart_data = pd.DataFrame({'Heure': heures, 'Affluence': predictions})
    st.line_chart(chart_data.set_index('Heure'))