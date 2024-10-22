import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go


# Page title
st.title("Stromcoin")

# Introduction of Stromcoin
st.write("""
**Stromcoin** ist ein Krypto-Token, der als Belohnung für die Nutzung der Stromkonto-App vergeben wird. Das Besondere an Stromcoin ist, dass sein Wert nur steigen kann. Nutzer, die überschüssigen Strom über die App handeln oder ihre Energie effizient verwalten, profitieren durch die Teilnahme am Stromcoin-basierten Umsatzbeteiligungssystem.
""")

# Additional fictitious Stromcoin details
st.subheader("Wichtige Informationen über Stromcoin:")
st.write("""
- **Ticker**: STRC
- **Maximale Versorgung**: 50 Millionen STRC
- **Verwendungszweck**: Einnahmenbeteiligung durch die Nutzung der Stromkonto-App
- **Preiswachstum**: Der Preis von Stromcoin kann nur steigen, was die langfristige Wertsteigerung für Nutzer garantiert.
""")

st.markdown("---")

# Generate fictitious historical price data for Stromcoin (last 30 days with only upward trend)
np.random.seed(0)
days = pd.date_range(end=pd.Timestamp.today(), periods=30)
prices = np.cumsum(np.random.uniform(0.01, 0.05, size=len(days)))/10  # Prices only going up

# Create a DataFrame for the price data
price_df = pd.DataFrame({
    'Datum': days,
    'Preis (CHF)': prices
})

# Plot the price chart
st.subheader("Stromcoin Preisentwicklung (letzte 30 Tage)")
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
    xaxis_tickformat='%d %b',  # Format the date axis
    showlegend=False
)

# Display the price chart
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Additional fictitious features or benefits of Stromcoin
st.subheader("Vorteile der Nutzung von Stromcoin:")
st.write("""
- **Umsatzbeteiligung**: Stromcoin ermöglicht Ihnen, Einnahmen aus der Stromkonto-App zu teilen und davon zu profitieren.
- **Langfristige Wertsteigerung**: Der Wert von Stromcoin kann nur steigen, was bedeutet, dass je mehr Sie die App nutzen, desto mehr wertvolle Token Sie verdienen.
- **Nachhaltigkeit fördern**: Durch die Teilnahme am Strommarkt und die Nutzung erneuerbarer Energien können Sie Ihre Stromkosten senken und gleichzeitig durch Stromcoin profitieren.
- **Dezentralisierte Kontrolle**: Stromcoin basiert auf der Blockchain-Technologie, die ein sicheres und dezentrales System für den Energiehandel bietet.
""")

st.markdown("---")

# Footer or additional fictitious content
st.write("""
Stromcoin ist nicht nur eine Belohnung für die Nutzung von Stromkonto, sondern auch ein Weg, langfristig an der Wertschöpfung im Strommarkt zu partizipieren. Seien Sie Teil der nachhaltigen Energiezukunft und profitieren Sie vom wachsenden Wert von Stromcoin!
""")