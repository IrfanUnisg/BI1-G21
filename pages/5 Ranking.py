import streamlit as st
import pandas as pd

# Seite konfigurieren
st.set_page_config(page_title="Ranking", page_icon="⚡", layout="centered")

# Fiktive Daten für Rankings
data_schweiz = {
    "Rang": [1, 2, 3, 4, 5],
    "Name": ["Lukas Meier", "Sarah Müller", "Thomas Schmid", "Claudia Huber", "Michael Weber"],
    "Blitze": [120, 115, 110, 105, 100]
}

data_gemeinde = {
    "Rang": [1, 2, 3, 4, 5],
    "Name": ["Anna Steiner", "Jonas Keller", "Laura Frei", "Peter Graf", "Monika Berger"],
    "Blitze": [90, 85, 80, 75, 70]
}

data_freunde = {
    "Rang": [1, 2, 3, 4, 5],
    "Name": ["Luc Fischer", "Irfan Kujovic", "Celia Bührer", "Marco Köhler", "Flurin Oehler"],
    "Blitze": [65, 60, 55, 50, 45]
}

# DataFrames erstellen und Index vollständig entfernen
df_schweiz = pd.DataFrame(data_schweiz).reset_index(drop=True)
df_gemeinde = pd.DataFrame(data_gemeinde).reset_index(drop=True)
df_freunde = pd.DataFrame(data_freunde).reset_index(drop=True)

# Seite Titel
st.markdown("<h1 style='text-align: center;'>⚡ Ranking </h1>", unsafe_allow_html=True)
st.markdown("---")

# Ranking Schweiz
st.markdown("<h2 style='text-align: center;'>Schweiz</h2>", unsafe_allow_html=True)
st.table(df_schweiz)  # Index ist jetzt entfernt

st.markdown("---")

# Ranking Gemeinde
st.markdown("<h2 style='text-align: center;'>Gemeinde Uzwil</h2>", unsafe_allow_html=True)
st.table(df_gemeinde)  # Index ist jetzt entfernt

st.markdown("---")

# Ranking Freunde
st.markdown("<h2 style='text-align: center;'>Freunde</h2>", unsafe_allow_html=True)
st.table(df_freunde)  # Index ist jetzt entfernt

# Abschluss
st.write("Diese Ranglisten basieren auf der Anzahl der Blitze, die durch Interaktionen mit der Stromkonto-App gesammelt wurden. Je mehr Blitze, desto höher das Ranking!")
