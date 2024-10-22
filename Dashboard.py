import streamlit as st
import plotly.graph_objects as go

# Seite konfigurieren (must be first command)
st.set_page_config(page_title="Virtual Battery", page_icon="⚡", layout="wide")

# Farben definieren
blue_color = "#044b5b"
yellow_color = "#facb04"

# Custom CSS for centering content
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
        .stRadio, .stNumberInput, .stSelectbox {
            display: block;
            margin-left: auto;
            margin-right: auto;
            text-align: center;
        }
        div[data-testid="stBlock"] > div {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
""", unsafe_allow_html=True)

# Initialisiere Session States
if "guthaben" not in st.session_state:
    st.session_state["guthaben"] = 1367
if "cash" not in st.session_state:
    st.session_state["cash"] = 967
if "kapazitaet" not in st.session_state:
    st.session_state["kapazitaet"] = 3000

# Werte laden
preis_kauf = 0.2714  # 26 Rp/kWh
preis_verkauf = 0.09  # 9 Rp/kWh (für Verkauf)
guthaben = st.session_state["guthaben"]
cash = st.session_state["cash"]
kapazitaet = st.session_state["kapazitaet"]

# Berechne den Geldwert des gespeicherten Stroms in CHF
stored_energy_value = guthaben * preis_verkauf

# Seite Titel
st.markdown("<h1 class='center-content'>Virtual Battery</h1>", unsafe_allow_html=True)

# Abschnitt: Kontoübersicht
st.markdown("<h2 class='center-content'>Kontoübersicht</h2>", unsafe_allow_html=True)
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"<div class='center-content'><h4>Aktuelles Stromguthaben: </h4><h2 style='color:{blue_color};'>{guthaben} kWh</h2></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='center-content'><h4>Kontoguthaben: </h4><h2 style='color:{blue_color};'>{cash:.2f} CHF</h2></div>", unsafe_allow_html=True)

# Abschnitt: Batterie-Status
st.markdown("---")
st.markdown("<h2 class='center-content'>Batterie-Status (kWh)</h2>", unsafe_allow_html=True)

# Batterie-Gauge-Diagramm
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=guthaben,
    gauge={
        'axis': {'range': [0, kapazitaet]},
        'bar': {'color': yellow_color}
    },
))
st.plotly_chart(fig, use_container_width=True)

# Batteriewert in CHF anzeigen
st.markdown(f"<div class='center-content'><p style='font-size:18px;'>Aktueller Wert des gespeicherten Stroms: <b>{stored_energy_value:.2f} CHF</b></p></div>", unsafe_allow_html=True)

# Abschnitt: Stromhandel
st.markdown("---")
st.markdown("<h2 class='center-content'>Stromhandel</h2>", unsafe_allow_html=True)

# Two columns for options and prices
col1, col2 = st.columns([1, 1])  # Adjust ratio if needed

# Left column: Trade options
with col1:
    st.markdown("<div class='center-content'>", unsafe_allow_html=True)
    trade_type = st.radio("Möchten Sie Strom kaufen, verkaufen oder verschenken?", ("Kaufen", "Verkaufen", "Verschenken"), index=0)
    st.markdown("</div>", unsafe_allow_html=True)

# Right column: Prices
with col2:
    st.markdown(f"<div class='center-content'><p><b>Kaufpreis:</b> {preis_kauf * 100:.2f} Rp/kWh</p></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='center-content'><p><b>Verkaufspreis:</b> {preis_verkauf * 100:.2f} Rp/kWh</p></div>", unsafe_allow_html=True)

# Centered trade amount and selection box
st.markdown("<div class='center-content'>", unsafe_allow_html=True)
trade_amount = st.number_input(f"Menge an Strom zum {trade_type.lower()} (kWh)", min_value=0)
st.markdown("</div>", unsafe_allow_html=True)

if trade_type == "Verschenken":
    recipient = st.selectbox("Wählen Sie den Empfänger", ("Grossmutter", "Ferienwohnung"))

# Confirm button
if st.button(f"{trade_type} bestätigen"):
    total_price = trade_amount * (preis_kauf if trade_type == "Kaufen" else preis_verkauf)

    if trade_type == "Kaufen":
        if total_price <= cash:
            guthaben += trade_amount
            cash -= total_price
            st.success(f"Sie haben erfolgreich {trade_amount} kWh gekauft.")
        else:
            st.error("Nicht genügend Guthaben!")
    elif trade_type == "Verkaufen":
        if trade_amount <= guthaben:
            guthaben -= trade_amount
            cash += total_price
            st.success(f"Sie haben erfolgreich {trade_amount} kWh verkauft.")
        else:
            st.error("Nicht genügend Strom zu verkaufen!")
    else:  # Verschenken
        if trade_amount <= guthaben:
            guthaben -= trade_amount
            st.success(f"Sie haben erfolgreich {trade_amount} kWh an {recipient} verschenkt.")
        else:
            st.error("Nicht genügend Strom zu verschenken!")

    # Update session state
    st.session_state["guthaben"] = guthaben
    st.session_state["cash"] = cash
