import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Seitentitel
st.title("Solaranlage Tracking Dashboard")

# Beispiel-Daten (können durch Echtzeitdaten ersetzt werden)
data = {
    'Monat': ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt'],
    'Erzeugte Energie (kWh)': [300, 320, 400, 450, 500, 550, 600, 620, 500, 450],
    'Kosten ohne Stromkonto (CHF)': [120, 128, 160, 180, 200, 220, 240, 248, 200, 180],
    'Kosten mit Stromkonto (CHF)': [100, 106, 130, 150, 165, 185, 200, 210, 170, 155],
    'Gesparte Kosten durch Solaranlage (CHF)': [45, 48, 60, 67, 75, 83, 90, 93, 75, 67],
    'Ersparnisse durch Stromkonto (CHF)': [20, 22, 30, 35, 35, 35, 40, 38, 30, 25]
}

# In einen DataFrame umwandeln
df = pd.DataFrame(data)

# Stromkosten: Vergleich ohne und mit Stromkonto
st.subheader("Stromkosten: Vergleich ohne Stromkonto und mit Stromkonto")
st.write("Dieses Diagramm zeigt die monatlichen Stromkosten ohne Stromkonto im Vergleich zu den Kosten mit einem Standard-Stromkonto-Abo.")

# Plotly Balkendiagramm
fig = go.Figure()

# Kosten ohne Stromkonto
fig.add_trace(go.Bar(
    x=df['Monat'],
    y=df['Kosten ohne Stromkonto (CHF)'],
    name='Kosten ohne Stromkonto',
    marker_color='indianred'
))

# Kosten mit Stromkonto
fig.add_trace(go.Bar(
    x=df['Monat'],
    y=df['Kosten mit Stromkonto (CHF)'],
    name='Kosten mit Stromkonto',
    marker_color='lightsalmon'
))

# Layout anpassen
fig.update_layout(
    barmode='group',
    xaxis_title="Monat",
    yaxis_title="Kosten (CHF)",
    title="Monatliche Stromkosten: Mit und ohne Stromkonto im Vergleich",
    margin=dict(l=40, r=40, t=40, b=40),
    height=400,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

# Diagramm anzeigen
st.plotly_chart(fig, use_container_width=True)

# Weitere Energiedaten
st.subheader("Weitere Energiedaten")
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])

# Gesamte erzeugte Energie
col1.metric("Gesamte erzeugte Energie (kWh)", f"{df['Erzeugte Energie (kWh)'].sum()} kWh")

# Gesamte Einsparungen durch die Solaranlage
col2.metric("Gesamt eingesparte Kosten durch Solaranlage (CHF)", f"{df['Gesparte Kosten durch Solaranlage (CHF)'].sum():.2f} CHF")

# Gesamte Einsparungen durch das Stromkonto
col3.metric("Gesamt eingesparte Kosten durch Stromkonto (CHF)", f"{min(df['Ersparnisse durch Stromkonto (CHF)'].sum(), 100):.2f} CHF")

st.markdown("---")

# Aktuelle Leistung der Solaranlage
st.subheader("Aktuelle Solardaten")
col4, col5 = st.columns([1, 1])

# Aktuelle Daten
current_energy = 15.7  # kWh
current_savings = 9.2  # CHF

# Aktuelle Daten anzeigen
col4.metric("Aktuell erzeugte Energie (heute)", f"{current_energy} kWh")
col5.metric("Aktuelle Einsparungen (heute)", f"{current_savings:.2f} CHF")

# Diagramm für die erzeugte Energie
st.subheader("Monatliche erzeugte Energie")
st.write("Dieses Diagramm zeigt die monatliche Energieproduktion Ihrer Solaranlage.")

# Liniendiagramm für die Energieerzeugung
st.line_chart(df.set_index('Monat')['Erzeugte Energie (kWh)'])

# Strompreis-Verlauf hinzufügen
st.subheader("Strompreis-Verlauf (letzte 30 Tage, stündliche Messungen)")
np.random.seed(42)
strompreis = np.clip(0.07 + np.random.normal(0, 0.002, 24 * 30), 0.05, 0.1)

# Erstelle Zeitstempel für jede Stunde der letzten 30 Tage
time_index = pd.date_range(end=pd.Timestamp.today(), periods=24 * 30, freq='H').to_pydatetime().tolist()

# Plotly-Liniendiagramm für den Strompreis-Verlauf
fig_price = go.Figure()
fig_price.add_trace(go.Scatter(x=time_index, y=strompreis, mode='lines', name='Strompreis', line=dict(color='green')))

# Layout anpassen
fig_price.update_layout(
    xaxis_title="Zeit",
    yaxis_title="Strompreis (CHF)",
    title="Strompreis-Verlauf",
    margin=dict(l=40, r=40, t=40, b=40),
    height=400
)

# Diagramm anzeigen
st.plotly_chart(fig_price, use_container_width=True)
