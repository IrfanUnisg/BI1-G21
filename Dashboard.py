import streamlit as st
import hmac
import plotly.graph_objects as go
import numpy as np

# Seite konfigurieren
st.set_page_config(page_title="Virtual Battery", page_icon="⚡", layout="wide")

# Passwort-Überprüfung
def check_password():
    def password_entered():
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
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
if "kapazitaet" not in st.session_state:
    st.session_state["kapazitaet"] = 3000

# Werte laden
preis_kauf = 0.26  # 26 Rp/kWh
preis_verkauf = 0.09  # 9 Rp/kWh
guthaben = st.session_state["guthaben"]
cash = st.session_state["cash"]
kapazitaet = st.session_state["kapazitaet"]

# Layout mit einer besseren Struktur und Styling
col1, col2 = st.columns([1, 4])
with col1:
    st.image("sk.png", width=100)

with col2:
    st.title("Virtual Battery")

# Kontoübersicht (Stromguthaben und Cash)
st.subheader("Stromkonto")
col3, col4 = st.columns(2)
with col3:
    st.write(f"Ihr aktuelles Stromguthaben: {guthaben} kWh")
with col4:
    st.write(f"Ihr Kontoguthaben: {cash:.2f} CHF")

# Anzeige des Batterie-Status als Gauge-Diagramm
st.subheader("Batterie-Status")
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=guthaben,
    gauge={'axis': {'range': [0, kapazitaet]},
           'bar': {'color': "blue"}},
    title={'text': "Batterie-Status"},
))
st.plotly_chart(fig, use_container_width=True)

# Stromhandel
st.subheader("Stromhandel")
col5, col6 = st.columns(2)
with col5:
    trade_type = st.radio("Möchten Sie Strom kaufen oder verkaufen?", ("Kaufen", "Verkaufen"))
    trade_amount = st.number_input(f"Menge an Strom zum {trade_type.lower()} (kWh)", min_value=0)

with col6:
    st.write(f"Kaufpreis: {preis_kauf * 100:.2f} Rp/kWh")
    st.write(f"Verkaufspreis: {preis_verkauf * 100:.2f} Rp/kWh")

if st.button(f"{trade_type} bestätigen"):
    total_price = trade_amount * (preis_kauf if trade_type == "Kaufen" else preis_verkauf)

    if trade_type == "Kaufen":
        if total_price <= cash:
            guthaben += trade_amount
            cash -= total_price
            st.success(f"Sie haben erfolgreich {trade_amount} kWh gekauft.")
        else:
            st.error("Nicht genügend Guthaben!")
    else:  # Verkaufen
        if trade_amount <= guthaben:
            guthaben -= trade_amount
            cash += total_price
            st.success(f"Sie haben erfolgreich {trade_amount} kWh verkauft.")
        else:
            st.error("Nicht genügend Strom zu verkaufen!")

    st.session_state["guthaben"] = guthaben
    st.session_state["cash"] = cash
