import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Seite konfigurieren (must be first command)
st.set_page_config(page_title="Stromcoin", page_icon="⚡", layout="wide")

# Farben definieren
blue_color = "#044b5b"

# Custom CSS for centering content and ensuring values are below titles
st.markdown("""
    <style>
        .center-content {
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        .stButton button {
            display: block;
            margin: 0 auto;
        }
        .value-under-title h4 {
            margin-bottom: 5px;
            text-align: center;
        }
        .value-under-title h2 {
            margin-top: 0;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Initialisiere Session States
if "stromcoins" not in st.session_state:
    st.session_state["stromcoins"] = 57
if "stromcoins_value" not in st.session_state:
    st.session_state["stromcoins_value"] = 6.17  # Fiktiver Wert in CHF

# Werte laden
stromcoins_in_possession = st.session_state["stromcoins"]
stromcoins_value_in_chf = st.session_state["stromcoins_value"]

# Seite Titel
st.markdown("<h1 class='center-content'>Ihre Stromcoins</h1>", unsafe_allow_html=True)

st.markdown("---")
# Erstelle zwei Spalten für Stromcoins und Wert in CHF
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"<div class='value-under-title'><h4>Anzahl der Stromcoins im Besitz:</h4><h2 style='color:{blue_color};'>{stromcoins_in_possession} STRC</h2></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='value-under-title'><h4>Aktueller Wert in CHF:</h4><h2 style='color:{blue_color};'>{stromcoins_value_in_chf:.2f} CHF</h2></div>", unsafe_allow_html=True)

st.markdown("---")

# Zusätzliche Informationen oder Diagramme können hier folgen...
