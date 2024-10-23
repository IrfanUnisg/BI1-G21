import streamlit as st
import pandas as pd

# Seite konfigurieren
st.set_page_config(page_title="Abonnementpläne", layout="wide")

# Seiten-Titel
st.title("Vergleich der Abonnementpläne")

# Daten für die Abonnementpläne
data = {
    "Merkmal": [
        "Preis", 
        "Kapazität Rent-a-Virtual-Battery", 
        "Tracking & Empfehlungen", 
        "Stromsharing", 
        "Swisscoin", 
        "Stromkarte", 
        "Vergleich zu Gemeinde", 
        "Loyalty / Referral"
    ],
    "Basic Plan": [
        "CHF 0", 
        "Keine", 
        "Keine", 
        "Nicht verfügbar", 
        "Nicht verfügbar", 
        "Nicht verfügbar", 
        "Verfügbar", 
        "Nicht verfügbar"
    ],
    "Medium Plan": [
        "CHF 14.90", 
        "3000 kWh", 
        "Volles Dashboard", 
        "Verfügbar (Nur für Auto)", 
        "1 Swisscoin", 
        "Verfügbar", 
        "Verfügbar", 
        "Nur für Auto"
    ],
    "Premium Plan": [
        "CHF 22", 
        "Unlimitiert", 
        "Volles Dashboard", 
        "Verfügbar (Ganzes Angebot)", 
        "2 Swisscoins", 
        "Verfügbar", 
        "Verfügbar", 
        "Ganzes Angebot"
    ]
}

# Erstelle einen DataFrame aus den Abodaten
df = pd.DataFrame(data)

# Setze die "Merkmal"-Spalte als Index, um sie als erste Spalte anzuzeigen und die Indizes zu vermeiden
df.set_index("Merkmal", inplace=True)

# Zeige die Tabelle an
st.table(df)

# Zusätzlicher Hinweis oder Beschreibung
st.write("""
Hier sehen Sie die verschiedenen Abonnementpläne im Vergleich. Diese Tabelle erleichtert es, die Unterschiede zwischen den Plänen zu erkennen.
""")
