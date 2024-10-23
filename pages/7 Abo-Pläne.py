import streamlit as st

# Seite konfigurieren
st.set_page_config(page_title="Abonnementpläne", layout="wide")

# Seiten-Titel
st.title("Vergleich der Abonnementpläne")

# Verwende 3 Spalten für die Abonnementpläne
col1, col2, col3 = st.columns(3)

# Basic Plan
with col1:
    st.markdown("### Basic Plan")
    st.markdown("""
    - **Preis:** CHF 0
    - **Kapazität Rent-a-Virtual-Battery:** Keine
    - **Tracking & Empfehlungen:** Keine
    - **Stromsharen:** Nicht verfügbar
    - **Swisscoin:** Nicht verfügbar
    - **Stromkarte:** Nicht verfügbar
    - **Vergleich zu Gemeinde:** Verfügbar
    - **Loyalty / Referral:** Nicht verfügbar
    """, unsafe_allow_html=True)

# Medium Plan
with col2:
    st.markdown("### Medium Plan")
    st.markdown("""
    - **Preis:** CHF 14.90
    - **Kapazität Rent-a-Virtual-Battery:** 3000 kWh
    - **Tracking & Empfehlungen:** Volles Dashboard
    - **Stromsharen:** Verfügbar (Nur für Auto)
    - **Swisscoin:** 1 Swisscoin
    - **Stromkarte:** Verfügbar
    - **Vergleich zu Gemeinde:** Verfügbar
    - **Loyalty / Referral:** Nur für Auto
    """, unsafe_allow_html=True)

# Premium Plan
with col3:
    st.markdown("### Premium Plan")
    st.markdown("""
    - **Preis:** CHF 22
    - **Kapazität Rent-a-Virtual-Battery:** Unlimitiert
    - **Tracking & Empfehlungen:** Volles Dashboard
    - **Stromsharen:** Verfügbar (Ganzes Angebot)
    - **Swisscoin:** 2 Swisscoins
    - **Stromkarte:** Verfügbar
    - **Vergleich zu Gemeinde:** Verfügbar
    - **Loyalty / Referral:** Ganzes Angebot
    """, unsafe_allow_html=True)
