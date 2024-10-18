import streamlit as st
import plotly.graph_objects as go

# Seite konfigurieren (must be first command)
st.set_page_config(page_title="Virtual Battery", page_icon="⚡")

# Set the blue and yellow colors
blue_color = "#044b5b"
yellow_color = "#facb04"

# Initialisiere Session States
if "guthaben" not in st.session_state:
    st.session_state["guthaben"] = 1367
if "cash" not in st.session_state:
    st.session_state["cash"] = 967
if "kapazitaet" not in st.session_state:
    st.session_state["kapazitaet"] = 3000

# Werte laden
preis_kauf = 0.26  # 26 Rp/kWh
preis_verkauf = 0.09  # 9 Rp/kWh
guthaben = st.session_state["guthaben"]
cash = st.session_state["cash"]
kapazitaet = st.session_state["kapazitaet"]

# Titel
st.markdown("<h1>Virtual Battery</h1>", unsafe_allow_html=True)

# Kontoübersicht (Stromguthaben und Cash)
st.markdown("<h2>Stromkonto</h2>", unsafe_allow_html=True)
col3, col4 = st.columns(2)
with col3:
    st.markdown(f"<p>Ihr aktuelles Stromguthaben: {guthaben} kWh</p>", unsafe_allow_html=True)
with col4:
    st.markdown(f"<p>Ihr Kontoguthaben: {cash:.2f} CHF</p>", unsafe_allow_html=True)

# Anzeige des Batterie-Status als Gauge-Diagramm
st.markdown("<h2>Batterie-Status</h2>", unsafe_allow_html=True)
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=guthaben,
    gauge={'axis': {'range': [0, kapazitaet]},
           'bar': {'color': yellow_color}},  # Apply yellow color to the gauge bar
    title={'text': "Batterie-Status", 'font': {'color': blue_color}},  # Title color
))
st.plotly_chart(fig, use_container_width=True)

# Stromhandel
st.markdown("<h2>Stromhandel</h2>", unsafe_allow_html=True)
col5, col6 = st.columns(2)
with col5:
    trade_type = st.radio("Möchten Sie Strom kaufen oder verkaufen?", ("Kaufen", "Verkaufen"))
    trade_amount = st.number_input(f"Menge an Strom zum {trade_type.lower()} (kWh)", min_value=0)

with col6:
    st.markdown(f"<p>Kaufpreis: {preis_kauf * 100:.2f} Rp/kWh</p>", unsafe_allow_html=True)
    st.markdown(f"<p>Verkaufspreis: {preis_verkauf * 100:.2f} Rp/kWh</p>", unsafe_allow_html=True)

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
