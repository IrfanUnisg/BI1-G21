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

# Style für die Tabelle: Verschiedene Farben pro Plan
def color_cells(val):
    if "Basic" in val:
        return 'background-color: #d3e4cd;'  # Light green for Basic
    elif "Medium" in val:
        return 'background-color: #ade8f4;'  # Light blue for Medium
    elif "Premium" in val:
        return 'background-color: #caf0f8;'  # Light teal for Premium
    return ''

# Wende den Style auf den DataFrame an
styled_df = df.style.applymap(color_cells, subset=["Basic Plan", "Medium Plan", "Premium Plan"])

# Zeige die Tabelle an
st.dataframe(styled_df, use_container_width=True)

# Zusätzlicher Hinweis oder Beschreibung, falls notwendig
st.write("""
Hier sehen Sie die verschiedenen Abonnementpläne im Vergleich. Die farblichen Hervorhebungen erleichtern es, die Unterschiede zwischen den Plänen zu erkennen.
""")
