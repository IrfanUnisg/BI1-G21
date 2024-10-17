import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

stromverbrauch = st.session_state.get("stromverbrauch", "Nicht verfügbar")
st.subheader("Stromverbrauch")
st.write(f"Ihr aktueller Stromverbrauch: {stromverbrauch} kWh")

# Seitentitel
st.title("Solar-Tracking ")

# Einführung
st.write("""
Willkommen im Dashboard zur Überwachung Ihrer Solaranlage. Hier sehen Sie Ihre aktuelle Energieproduktion, Einsparungen und weitere nützliche Daten.
""")

# Beispiel-Daten (können durch Echtzeitdaten ersetzt werden)
# Erzeugte Energie in kWh pro Monat
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
fig, ax = plt.subplots()
ax.bar(df['Monat'], df['Gesparte Kosten (€)'], color='skyblue')
ax.set_xlabel('Monat')
ax.set_ylabel('Gesparte Kosten (€)')
ax.set_title('Einsparungen im Stromkonto (in €)')
st.pyplot(fig)

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

fig2, ax2 = plt.subplots()
ax2.plot(df['Monat'], df['Erzeugte Energie (kWh)'], marker='o', color='orange')
ax2.set_xlabel('Monat')
ax2.set_ylabel('Erzeugte Energie (kWh)')
ax2.set_title('Erzeugte Energie pro Monat (in kWh)')
st.pyplot(fig2)

# Hinweis auf die laufende Leistung der Solaranlage
st.subheader("Status Ihrer Solaranlage")
st.write("Ihre Solaranlage produziert derzeit zuverlässig Energie und hilft Ihnen, die Stromkosten zu senken.")
