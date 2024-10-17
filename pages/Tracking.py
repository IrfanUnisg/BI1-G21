import streamlit as st
import pandas as pd

# Seitentitel
st.title("Solaranlage Tracking Dashboard")

# Beispiel-Daten (können durch Echtzeitdaten ersetzt werden)
data = {
    'Monat': ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez'],
    'Erzeugte Energie (kWh)': [300, 320, 400, 450, 500, 550, 600, 620, 500, 450, 380, 350],
    'Kosten mit Solaranlage (CHF)': [45, 48, 60, 67, 75, 83, 90, 93, 75, 67, 57, 52],
    'Kosten mit Stromkonto (CHF)': [100, 106, 130, 150, 165, 185, 200, 210, 170, 155, 130, 120]
}

# In einen DataFrame umwandeln
df = pd.DataFrame(data)

# Säulendiagramm mit zwei Säulen pro Monat
st.subheader("Kosten mit Solaranlage vs. Kosten mit Stromkonto")
st.write("Dieses Diagramm zeigt die monatlichen Stromkosten, wenn Sie eine Solaranlage nutzen, im Vergleich zu den Kosten mit einem Standard-Stromkonto-Abo.")

# Daten in das richtige Format für ein gestapeltes Diagramm umwandeln
bar_data = pd.DataFrame({
    'Kosten mit Solaranlage (CHF)': df['Kosten mit Solaranlage (CHF)'],
    'Kosten mit Stromkonto (CHF)': df['Kosten mit Stromkonto (CHF)']
}, index=df['Monat'])

# Bar chart anzeigen
st.bar_chart(bar_data)

# Weitere relevante Daten nebeneinander anzeigen
st.subheader("Weitere Energiedaten")
col1, col2 = st.columns(2)

# Berechnung der Gesamterzeugung und Gesamteinsparung
total_energy = df['Erzeugte Energie (kWh)'].sum()
total_savings = df['Kosten mit Stromkonto (CHF)'].sum() - df['Kosten mit Solaranlage (CHF)'].sum()

# Gesamte erzeugte Energie
col1.metric("Gesamte erzeugte Energie (kWh)", f"{total_energy} kWh")

# Gesamte Einsparungen durch die Solaranlage
col2.metric("Gesamt eingesparte Kosten (CHF)", f"{total_savings:.2f} CHF")

# Aktuelle Leistung der Solaranlage (Beispieldaten)
st.subheader("Aktuelle Solardaten")
current_energy = 35  # Aktuelle Energieproduktion in kWh (Beispiel)
current_savings = 15  # Aktuelle Einsparungen in CHF (Beispiel)

st.metric("Aktuell erzeugte Energie (heute)", f"{current_energy} kWh")
st.metric("Aktuelle Einsparungen (heute)", f"{current_savings:.2f} CHF")
