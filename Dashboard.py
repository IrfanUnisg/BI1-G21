import streamlit as st
import plotly.graph_objects as go

# Seite konfigurieren (must be first command)
st.set_page_config(page_title="Virtual Battery", page_icon="⚡", layout="wide")

# Inject custom CSS for styling
page_bg_css = """
<style>
    .stApp {
        background-color: #f0f4f4; /* Page background color */
    }
    .css-1d391kg { /* Navigation bar color */
        background-color: #ffffff;
    }
    .css-18ni7ap { /* Top bar color */
        background-color: #ffffff;
    }
    .plotly {
        background-color: #f0f4f4; /* Chart background color */
    }
</style>
"""

st.markdown(page_bg_css, unsafe_allow_html=True)

# Set the blue and yellow colors
blue_color = "#044b5b"
yellow_color = "#facb04"

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
    st.markdown(f"<h1 style='color:{blue_color};'>Virtual Battery</h1>", unsafe_allow_html=True)

# Kontoübersicht (Stromguthaben und Cash)
st.markdown(f"<h2 style='color:{blue_color};'>Stromkonto</h2>", unsafe_allow_html=True)
col3, col4 = st.columns(2)
with col3:
    st.markdown(f"<p style='color:{blue_color};'>Ihr aktuelles Stromguthaben: {guthaben} kWh</p>", unsafe_allow_html=True)
with col4:
    st.markdown(f"<p style='color:{blue_color};'>Ihr Kontoguthaben: {cash:.2f} CHF</p>", unsafe_allow_html=True)

# Anzeige des Batterie-Status als Gauge-Diagramm
st.markdown(f"<h2 style='color:{blue_color};'>Batterie-Status</h2>", unsafe_allow_html=True)
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=guthaben,
    gauge={'axis': {'range': [0, kapazitaet]},
           'bar': {'color': yellow_color}},  # Apply yellow color to the gauge bar
    title={'text': "Batterie-Status", 'font': {'color': blue_color}},  # Title color
))
st.plotly_chart(fig, use_container_width=True)

# Stromhandel
st.markdown(f"<h2 style='color:{blue_color};'>Stromhandel</h2>", unsafe_allow_html=True)
col5, col6 = st.columns(2)
with col5:
    trade_type = st.radio("Möchten Sie Strom kaufen oder verkaufen?", ("Kaufen", "Verkaufen"))
    trade_amount = st.number_input(f"Menge an Strom zum {trade_type.lower()} (kWh)", min_value=0)

with col6:
    st.markdown(f"<p style='color:{blue_color};'>Kaufpreis: {preis_kauf * 100:.2f} Rp/kWh</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:{blue_color};'>Verkaufspreis: {preis_verkauf * 100:.2f} Rp/kWh</p>", unsafe_allow_html=True)

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
