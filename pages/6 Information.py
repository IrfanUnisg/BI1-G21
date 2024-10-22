import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(layout="wide")

# Custom CSS for centering text and content
st.markdown("""
    <style>
        .center-content {
            text-align: center;
        }
        .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Page title
st.markdown("<h1 class='center-content'>Stromcoin</h1>", unsafe_allow_html=True)

# Introduction of Stromcoin
st.markdown("""
<p class='center-content'>
**Stromcoin** ist ein Krypto-Token, der als Belohnung für die Nutzung der Stromkonto-App vergeben wird. Das Besondere an Stromcoin ist, dass sein Wert nur steigen kann. Nutzer, die überschüssigen Strom über die App handeln oder ihre Energie effizient verwalten, profitieren durch die Teilnahme am Stromcoin-basierten Gewinnbeteiligungssystem.
</p>
""", unsafe_allow_html=True)

# Additional fictitious Stromcoin details
st.markdown("<h2 class='center-content'>Wichtige Informationen über Stromcoin:</h2>", unsafe_allow_html=True)
st.markdown("""
<p class='center-content'>
- **Ticker**: STRC<br>
- **Maximale Versorgung**: 2 Millionen STRC<br>
- **Verwendungszweck**: Gewinnbeteiligung durch die Nutzung der Stromkonto-App<br>
- **Preiswachstum**: Der Preis von Stromcoin kann nur steigen, was die langfristige Wertsteigerung für Nutzer garantiert.
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# Generate fictitious historical price data for Stromcoin (last year with only upward trend)
np.random.seed(0)
days = pd.date_range(end=pd.Timestamp.today(), periods=365)
prices = np.cumsum(np.random.uniform(0.01, 0.05, size=len(days))) / 100  # Prices only going up

# Create a DataFrame for the price data
price_df = pd.DataFrame({
    'Datum': days,
    'Preis (CHF)': prices
})

# Plot the price chart
st.markdown("<h2 class='center-content'>Stromcoin Preisentwicklung (letztes Jahr)</h2>", unsafe_allow_html=True)
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
st.markdown("<h2 class='center-content'>Vorteile der Nutzung von Stromcoin:</h2>", unsafe_allow_html=True)
st.markdown("""
<p class='center-content'>
- **Gewinnbeteiligung**: Durch den Stromcoin stellt Ihnen das Stromkonto einen Teil seines Gewinns zur Verfügung.<br>
- **Langfristige Wertsteigerung**: Der Wert von Stromcoin kann nur steigen, was bedeutet, dass je mehr Sie die App nutzen, desto mehr wertvolle Token verdienen Sie.<br>
- **Nachhaltigkeit fördern**: Durch die Teilnahme am Strommarkt und die Nutzung erneuerbarer Energien können Sie Ihre Stromkosten senken und gleichzeitig durch Stromcoin profitieren.<br>
- **Dezentralisierte Kontrolle**: Stromcoin basiert auf der Blockchain-Technologie, die ein sicheres und dezentrales System für den Energiehandel bietet.
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# Footer or additional fictitious content
st.markdown("""
<p class='center-content'>
Stromcoin ist nicht nur eine Belohnung für die Nutzung von Stromkonto, sondern auch ein Weg, langfristig an der Wertschöpfung im Strommarkt zu partizipieren. Seien Sie Teil der nachhaltigen Energiezukunft und profitieren Sie vom wachsenden Wert von Stromcoin!
</p>
""", unsafe_allow_html=True)
