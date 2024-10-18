import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Seitentitel
st.title("Solaranlage Tracking Dashboard")

# Beispiel-Daten (können durch Echtzeitdaten ersetzt werden)
data = {
    'Monat': ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt'],
    'Erzeugte Energie (kWh)': [300, 320, 400, 450, 500, 550, 600, 620, 500, 450],
    'Stromverbrauch (kWh)': [250, 270, 380, 430, 480, 510, 580, 610, 480, 420],
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

st.plotly_chart(fig, use_container_width=True)

# Weitere Energiedaten
st.subheader("Weitere Energiedaten")
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])

# Gesamte erzeugte Energie
col1.metric("Gesamte erzeugte Energie (kWh)", f"{df['Erzeugte Energie (kWh)'].sum()} kWh")

# Gesamte Einsparungen durch die Solaranlage
col2.metric("Gesamt eingesparte Kosten durch Solaranlage (CHF)", f"{df['Gesparte Kosten durch Solaranlage (CHF)'].sum():.2f} CHF")

# Gesamte Einsparungen durch das Stromkonto (leicht unter 100 CHF)
col3.metric("Gesamt eingesparte Kosten durch Stromkonto (CHF)", f"{df['Ersparnisse durch Stromkonto (CHF)'].sum():.2f} CHF")

st.markdown("---")

# Aktuelle Leistung der Solaranlage
st.subheader("Aktuelle Solardaten")
col4, col5 = st.columns([1, 1])

# Beispiel für aktuelle Werte
current_energy = 15  # kWh
current_savings = 15  # CHF

# Aktuelle Daten
col4.metric("Aktuell erzeugte Energie (heute)", f"{current_energy} kWh")
col5.metric("Aktuelle Einsparungen (heute)", f"{current_savings:.2f} CHF")

# Diagramm für die erzeugte Energie und Stromverbrauch
st.subheader("Monatliche erzeugte Energie und Stromverbrauch")
st.write("Dieses Diagramm zeigt die monatliche Energieproduktion und den Stromverbrauch Ihrer Solaranlage.")

# Liniendiagramm für die Energieerzeugung und Stromverbrauch
fig_energy = go.Figure()

fig_energy.add_trace(go.Scatter(x=df['Monat'], y=df['Erzeugte Energie (kWh)'], mode='lines+markers', name='Erzeugte Energie'))
fig_energy.add_trace(go.Scatter(x=df['Monat'], y=df['Stromverbrauch (kWh)'], mode='lines+markers', name='Stromverbrauch', line=dict(dash='dash')))

# Layout anpassen
fig_energy.update_layout(
    title="Monatliche erzeugte Energie und Stromverbrauch (kWh)",
    xaxis_title="Monat",
    yaxis_title
