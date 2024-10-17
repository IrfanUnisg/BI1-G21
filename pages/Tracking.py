import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Seitentitel
st.title("Solaranlage Tracking Dashboard")

# Beispiel-Daten (können durch Echtzeitdaten ersetzt werden)
data = {
    'Monat': ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez'],
    'Erzeugte Energie (kWh)': [300, 320, 400, 450, 500, 550, 600, 620, 500, 450, 380, 350],
    'Kosten ohne Stromkonto (CHF)': [120, 128, 160, 180, 200, 220, 240, 248, 200, 180, 152, 140],
    'Kosten mit Stromkonto (CHF)': [100, 106, 130, 150, 165, 185, 200, 210, 170, 155, 130, 120],
    'Gesparte Kosten durch Solaranlage (CHF)': [45, 48, 60, 67, 75, 83, 90, 93, 75, 67, 57, 52],
    'Ersparnisse durch Stromkonto (CHF)': [20, 22, 30, 35, 35, 35, 40, 38, 30, 25, 22, 20]
}

# In einen DataFrame umwandeln
df = pd.DataFrame(data)

# Balkendiagramm für die Kosten mit und ohne Stromkonto
st.subheader("Stromkosten: Vergleich ohne Stromkonto und mit Stromkonto")
st.write("Dieses Diagramm zeigt die monatlichen Stromkosten ohne Stromkonto im Vergleich zu den Kosten mit einem Standard-Stromkonto-Abo.")

# Erstelle das Plotly Balkendiagramm
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
    title="Monatliche Stromkosten: Mit und ohne Stromkonto im Vergleich"
)

# Diagramm anzeigen
st.plotly_chart(fig)

# Weitere relevante Daten nebeneinander anzeigen
st.subheader("Weitere Energiedaten")
col1, col2 = st.columns(2)

# Berechnung der Gesamterzeugung und Gesamteinsparung
total_energy = df['Erzeugte Energie (kWh)'].sum()
total_solar_savings = df['Gesparte Kosten durch Solaranlage (CHF)'].sum()
total_account_savings = df['Ersparnisse durch Stromkonto (CHF)'].sum()

# Gesamte erzeugte Energie
col1.metric("Gesamte erzeugte Energie (kWh)", f"{total_energy} kWh")

# Gesamte Einsparungen durch die Solaranlage
col1.metric("Gesamt eingesparte Kosten durch Solaranlage (CHF)", f"{total_solar_savings:.2f} CHF")

# Gesamte Einsparungen durch Stromkonto
col2.metric("Gesamt eingesparte Kosten durch Stromkonto (CHF)", f"{total_account_savings:.2f} CHF")

# Aktuelle Leistung der Solaranlage (Beispieldaten)
st.subheader("Aktuelle Solardaten")
current_energy = 35  # Aktuelle Energieproduktion in kWh (Beispiel)
current_savings = 15  # Aktuelle Einsparungen in CHF (Beispiel)

st.metric("Aktuell erzeugte Energie (heute)", f"{current_energy} kWh")
st.metric("Aktuelle Einsparungen (heute)", f"{current_savings:.2f} CHF")

# Diagramm für die erzeugte Energie
st.subheader("Monatliche erzeugte Energie")
st.write("Dieses Diagramm zeigt die monatliche Energieproduktion Ihrer Solaranlage.")

st.line_chart(df.set_index('Monat')['Erzeugte Energie (kWh)'])
