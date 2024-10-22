import streamlit as st
import plotly.graph_objects as go

# Seite konfigurieren (must be first command)
st.set_page_config(page_title="Virtual Battery", page_icon="⚡", layout="centered")

# Farben definieren
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
preis_verkauf = 0.09  # 9 Rp/kWh (für Verkauf)
guthaben = st.session_state["guthaben"]
cash = st.session_state["cash"]
kapazitaet = st.session_state["kapazitaet"]

# Berechne den Geldwert des gespeicherten Stroms in CHF
stored_energy_value = guthaben * preis_verkauf

# Seite Titel
st.markdown("<h1 style='text-align: center;'>⚡ Virtual Battery ⚡</h1>", unsafe_allow_html=True)

# Abschnitt: Kontoübersicht
st.markdown("<h2 style='text-align: center;'>Kontoübersicht</h2>", unsafe_allow_html=True)
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"<h4>Aktuelles Stromguthaben: </h4><h2 style='color:{blue_color};'>{guthaben} kWh</h2>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<h4>Kontoguthaben: </h4><h2 style='color:{blue_color};'>{cash:.2f} CHF</h2>", unsafe_allow_html=True)

# Abschnitt: Batterie-Status
st.markdown("---")
st.markdown("<h2 style='text-align: center;'>Batterie-Status</h2>", unsafe_allow_html=True)

# Batterie-Gauge-Diagramm
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=guthaben,
    gauge={
        'axis': {'range': [0, kapazitaet]},
        'bar': {'color': yellow_color}
    },
    title={'text': "Batterie-Status (kWh)", 'font': {'color': blue_color}}
))
st.plotly_chart(fig, use_container_width=True)

# Batteriewert in CHF anzeigen
st.markdown(f"<p style='text-align: center; font-size:18px;'>Aktueller Batteriewert: <b>{stored_energy_value:.2f} CHF</b></p>", unsafe_allow_html=True)

# Abschnitt: Stromhandel
st.markdown("---")
st.markdown("<h2 style='text-align: center;'>Stromhandel</h2>", unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    trade_type = st.radio("Möchten Sie Strom kaufen oder verkaufen?", ("Kaufen", "Verkaufen"))
    trade_amount = st.number_input(f"Menge an Strom zum {trade_type.lower()} (kWh)", min_value=0)

with col4:
    st.markdown(f"<p><b>Kaufpreis:</b> {preis_kauf * 100:.2f} Rp/kWh</p>", unsafe_allow_html=True)
    st.markdown(f"<p><b>Verkaufspreis:</b> {preis_verkauf * 100:.2f} Rp/kWh</p>", unsafe_allow_html=True)

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

    # Update session state
    st.session_state["guthaben"] = guthaben
    st.session_state["cash"] = cash
