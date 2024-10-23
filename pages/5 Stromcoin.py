import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Seite konfigurieren (must be first command)
st.set_page_config(page_title="Stromcoin", page_icon="⚡", layout="wide")

# Farben definieren
blue_color = "#044b5b"
yellow_color = "#facb04"

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
    st.session_state["stromcoins"] = 57  # Beispielwert
if "stromcoins_value" not in st.session_state:
    st.session_state["stromcoins_value"] = 6.17  # Beispielwert in CHF

# Werte laden
stromcoins_in_possession = st.session_state["stromcoins"]
stromcoins_value_in_chf = st.session_state["stromcoins_value"]

# Generate fictitious historical price data for Stromcoin (last year with only upward trend)
np.random.seed(0)
days = pd.date_range(end=pd.Timestamp.today(), periods=365)
prices = np.cumsum(np.random.uniform(0.01, 0.05, size=len(days))) / 100  # Prices only going up

# Create a DataFrame for the price data
price_df = pd.DataFrame({
    'Datum': days,
    'Preis (CHF)': prices
})

# Current price of Stromcoin (latest price from the generated data)
current_price = price_df['Preis (CHF)'].iloc[-1]

# Display Stromcoin ownership and value in CHF
stromcoins_in_possession = 57
stromcoins_value = stromcoins_in_possession * current_price

# Seite Titel
st.markdown("<h1 class='center-content'>Stromcoin</h1>", unsafe_allow_html=True)

# Introduction of Stromcoin
st.write("""
**Stromcoin** ist ein Krypto-Token, der als Belohnung für die Nutzung der Stromkonto-App vergeben wird. Das Besondere an Stromcoin ist, dass sein Wert nur steigen kann. Nutzer, die überschüssigen Strom über die App handeln oder ihre Energie effizient verwalten, profitieren durch die Teilnahme am Stromcoin-basierten Gewinnbeteiligungssystem.
""")
st.markdown("---")

# Titel für 'Ihre Stromcoins'
st.markdown("<h2 class='center-content'>Ihre Stromcoins</h2>", unsafe_allow_html=True)

# Zwei Spalten für Stromcoins im Besitz und deren Wert in CHF
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"<div class='value-under-title'><h4>Anzahl der Stromcoins im Besitz:</h4><h2 style='color:{blue_color};'>{stromcoins_in_possession} STRC</h2></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='value-under-title'><h4>Aktueller Wert in CHF:</h4><h2 style='color:{blue_color};'>{stromcoins_value:.2f} CHF</h2></div>", unsafe_allow_html=True)

st.markdown("---")

# Plot the price chart
st.subheader("Stromcoin Preisentwicklung (letztes Jahr)")
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=price_df['Datum'],
    y=price_df['Preis (CHF)'],
    mode='lines+markers',
    name='Preis (CHF)',
    line=dict(color='#044b5b')
))

fig.update_layout(
    title="Stromcoin Preisentwicklung",
    xaxis_title="Datum",
    yaxis_title="Preis (CHF)",
    height=400,
    margin=dict(l=40, r=40, t=40, b=40),
    xaxis_tickformat='%b %Y',  # Format the date axis for monthly display
    showlegend=False
)

# Display the price chart
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Additional fictitious features or benefits of Stromcoin
st.subheader("Vorteile der Nutzung von Stromcoin:")
st.write("""
- **Gewinnbeteiligung**: Durch den Stromcoin stellt Ihnen das Stromkonto einen Teil seines Gewinns zur Verfügung.
- **Langfristige Wertsteigerung**: Der Wert von Stromcoin kann nur steigen, was bedeutet, dass je mehr Sie die App nutzen, desto mehr wertvolle Token verdienen Sie.
- **Nachhaltigkeit fördern**: Durch die Teilnahme am Strommarkt und die Nutzung erneuerbarer Energien können Sie Ihre Stromkosten senken und gleichzeitig durch Stromcoin profitieren.
- **Dezentralisierte Kontrolle**: Stromcoin basiert auf der Blockchain-Technologie, die ein sicheres und dezentrales System für den Energiehandel bietet.
""")

st.markdown("---")

# Footer or additional fictitious content
st.write("""
Stromcoin ist nicht nur eine Belohnung für die Nutzung von Stromkonto, sondern auch ein Weg, langfristig an der Wertschöpfung im Strommarkt zu partizipieren. Seien Sie Teil der nachhaltigen Energiezukunft und profitieren Sie vom wachsenden Wert von Stromcoin!
""")
