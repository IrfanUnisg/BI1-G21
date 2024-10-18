import streamlit as st
import hmac
import plotly.graph_objects as go
import numpy as np

# Seite konfigurieren
st.set_page_config(page_title="Stromkonto", page_icon="⚡", layout="wide")

# Passwort-Überprüfung
def check_password():
    """Returns `True` if the user had the correct password."""
    def password_entered():
        """Checks whether a password entered von the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct", False):
        return True

    st.subheader("Bitte Passwort eingeben.")
    st.text_input("Passwort", type="password", on_change=password_entered, key="password")
    if "password_correct" in st.session_state:
        st.error("😕 Passwort inkorrekt")
    return False

if not check_password():
    st.stop()

# Initialisiere Session States
if "guthaben" not in st.session_state:
    st.session_state["guthaben"] = 600
if "cash" not in st.session_state:
    st.session_state["cash"] = 508
if "stromverbrauch" not in st.session_state:
    st.session_state["stromverbrauch"] = 500
if "kapazitaet" not in st.session_state:
    st.session_state["kapazitaet"] = 3000

# Werte laden
kaufpreis = 0.26  # 26 Rp/kWh
verkaufspreis = 0.09  # 9 Rp/kWh
stromverbrauch = st.session_state["stromverbrauch"]
guthaben = st.session_state["guthaben"]
cash = st.session_state["cash"]
kapazitaet = st.session_state["kapazitaet"]

# Hauptseite
st.title("Virtual Battery")

st.markdown("---")
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Stromverbrauch")
    st.write(f"Aktueller Verbrauch: {stromverbrauch} kWh")

    # Kontoübersicht (Stromguthaben und Cash)
    st.subheader("Stromkonto")
    st.write(f"Stromguthaben: {guthaben} kWh")
    st.write(f"Kontoguthaben: {cash:.2f} CHF")

with col2:
    # Anzeige des Batterie-Status als Gauge-Diagramm
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=guthaben,
        gauge={'axis': {'range': [0, kapazitaet]},
               'bar': {'color': "blue"}},
        title={'text': "Batterie-Status (kWh)"},
    ))
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
# Stromhandel
st.subheader("Stromhandel")

col3, col4 = st.columns(2)
with col3:
    st.write(f"Kaufpreis: {kaufpreis} CHF/kWh")
    st.write(f"Verkaufspreis: {verkaufspreis} CHF/kWh")

trade_type = st.radio("Möchten Sie Strom kaufen oder verkaufen?", ("Kaufen", "Verkaufen"))
trade_amount = st.number_input(f"Wählen Sie die Menge an Strom zum {trade_type.lower()} (kWh)", min_value=0)

if st.button(f"{trade_type} bestätigen"):
    if trade_type == "Kaufen":
        total_price = trade_amount * kaufpreis
        if total_price <= cash:
            st.session_state["guthaben"] += trade_amount
            st.session_state["cash"] -= total_price
            st.success(f"Sie haben {trade_amount} kWh für {total_price:.2f} CHF gekauft.")
        else:
            st.error("Nicht genügend Guthaben!")
    elif trade_type == "Verkaufen":
        total_price = trade_amount * verkaufspreis
        if trade_amount <= guthaben:
            st.session_state["guthaben"] -= trade_amount
            st.session_state["cash"] += total_price
            st.success(f"Sie haben {trade_amount} kWh für {total_price:.2f} CHF verkauft.")
        else:
            st.error("Nicht genügend Stromguthaben!")
