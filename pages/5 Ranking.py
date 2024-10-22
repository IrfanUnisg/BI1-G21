import streamlit as st
import pandas as pd

# Seite konfigurieren
st.set_page_config(page_title="Ranking", page_icon="⚡", layout="centered")

# Fiktive Daten für Rankings
data_schweiz = {
    "Name": ["Lukas Meier", "Sarah Müller", "Thomas Schmid", "Claudia Huber", "Michael Weber"],
    "Blitze": [120, 115, 110, 105, 100]
}

data_gemeinde = {
    "Name": ["Anna Steiner", "Jonas Keller", "Laura Frei", "Peter Graf", "Monika Berger"],
    "Blitze": [90, 85, 80, 75, 70]
}

data_freunde = {
    "Name": ["Paul Fischer", "Nina Maurer", "David Baumann", "Katja Beck", "Chris Vogel"],
    "Blitze": [65, 60, 55, 50, 45]
}

# DataFrames erstellen
df_schweiz = pd.DataFrame(data_schweiz)
df_gemeinde = pd.DataFrame(data_gemeinde)
df_freunde = pd.DataFrame(data_freunde)

# Seite Titel
st.markdown("<h1 style='text-align: center;'>⚡ Ranking ⚡</h1>", unsafe_allow_html=True)
st.markdown("---")

# Ranking Schweiz
st.markdown("<h2 style='text-align: center;'>Ranking: Schweiz</h2>", unsafe_allow_html=True)
st.table(df_schweiz)

st.markdown("---")

# Ranking Gemeinde
st.markdown("<h2 style='text-align: center;'>Ranking: Gemeinde</h2>", unsafe_allow_html=True)
st.table(df_gemeinde)

st.markdown("---")

# Ranking Freunde
st.markdown("<h2 style='text-align: center;'>Ranking: Freunde</h2>", unsafe_allow_html=True)
st.table(df_freunde)

# Abschluss
st.write("Diese Ranglisten basieren auf der Anzahl der Blitze, die durch Interaktionen mit der Stromkonto-App gesammelt wurden. Je mehr Blitze, desto höher das Ranking!")
