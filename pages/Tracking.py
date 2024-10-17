import streamlit as st
import pandas as pd

# Seitentitel
st.title("Solaranlage Tracking Dashboard")

# Beispiel-Daten (können durch Echtzeitdaten ersetzt werden)
data = {
    'Monat': ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez'],
    'Erzeugte Energie (kWh)': [300, 320, 400, 450, 500, 550, 600, 620, 500, 450, 380, 350],
    'Gesparte Kosten (€)': [45, 48, 60, 67, 75, 83, 90, 93, 75, 67, 57, 52]
}

# In einen DataFrame umwandeln
df = pd.DataFrame(data)

# Säulendiagramm für die gesparten Kosten
st.subheader("Stromkosten Einsparungen durch Ihre Solaranlage")
st.write("Dieses Diagramm zeigt, wie viel Sie durch Ihre Solaranlage jeden Monat an Stromkosten gespart haben.")

# Verwende Streamlit's native plot Funktion
st.bar_chart(df.set_index('Monat')['Gesparte Kosten (€)'])

# Weitere relevante Daten
st.subheader("Weitere Solardaten")

# Berechnung der Gesamterzeugung und Gesamteinsparung
total_energy = df['Erzeugte Energie (kWh)'].sum()
total_savings = df['Gesparte Kosten (€)'].sum()

st.metric("Gesamte erzeugte Energie (kWh)", f"{total_energy} kWh")
st.metric("Gesamt eingesparte Kosten (€)", f"{total_savings} €")

# Aktuelle Leistung der Solaranlage (Beispieldaten)
current_energy = 35  # Aktuelle Energieproduktion in kWh (Beispiel)
current_savings = current_energy * 0.15  # 15 Cent pro kWh Einsparung (Beispiel)

st.metric("Aktuell erzeugte Energie (heute)", f"{current_energy} kWh")
st.metric("Aktuelle Einsparungen (heute)", f"{current_savings:.2f} €")

# Diagramm für die erzeugte Energie
st.subheader("Monatliche erzeugte Energie")
st.write("Dieses Diagramm zeigt die monatliche Energieproduktion Ihrer Solaranlage.")

st.line_chart(df.set_index('Monat')['Erzeugte Energie (kWh)'])
