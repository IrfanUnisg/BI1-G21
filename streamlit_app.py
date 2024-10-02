import streamlit as st

# Dummy-Datenbank für Benutzer
users_db = {
    "Jan": {"password": "stromkonto", "consumption": 500, "balance": 1000},  # Stromverbrauch in kWh, Guthaben in EUR
    "admin": {"password": "stromkonto", "consumption": 600, "balance": 1500},
}

# Session-State für die Anmeldung
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['username'] = ''

# Anmeldeseite
def login():
    st.title("Log-In")
    username = st.text_input("Benutzername")
    password = st.text_input("Passwort", type="password")
    
    if st.button("Anmelden"):
        if username in users_db and users_db[username]["password"] == password:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success(f"Erfolgreich angemeldet als {username}")
        else:
            st.error("Falscher Benutzername oder Passwort!")

# Hauptseite für Stromverbrauch, Kontoübersicht und Handel
def main_page():
    st.image("sk.png",width=50, height=50)
    st.title("Stromkonto")
    
    username = st.session_state['username']
    user_data = users_db[username]
    
    # Übersicht über den Stromverbrauch
    st.subheader("Stromverbrauch")
    st.write(f"Ihr aktueller Stromverbrauch: {user_data['consumption']} kWh")
    
    # Kontoübersicht (Stromguthaben)
    st.subheader("Stromkonto")
    st.write(f"Ihr aktuelles Stromguthaben: {user_data['balance']} EUR")
    
    # Strom kaufen/verkaufen
    st.subheader("Stromhandel")
    
    trade_type = st.radio("Möchten Sie Strom kaufen oder verkaufen?", ("Kaufen", "Verkaufen"))
    trade_amount = st.number_input(f"Wählen Sie die Menge an Strom zum {trade_type.lower()} (kWh)", min_value=0)
    trade_price = st.number_input("Geben Sie den Preis pro kWh ein (EUR)", min_value=0.0, format="%.2f")
    
    if st.button(f"{trade_type} bestätigen"):
        total_price = trade_amount * trade_price
        
        if trade_type == "Kaufen":
            if total_price <= user_data['balance']:
                user_data['consumption'] += trade_amount
                user_data['balance'] -= total_price
                st.success(f"Sie haben erfolgreich {trade_amount} kWh gekauft.")
            else:
                st.error("Nicht genügend Guthaben!")
        else:  # Verkaufen
            if trade_amount <= user_data['consumption']:
                user_data['consumption'] -= trade_amount
                user_data['balance'] += total_price
                st.success(f"Sie haben erfolgreich {trade_amount} kWh verkauft.")
            else:
                st.error("Nicht genügend Strom zu verkaufen!")

# Logout-Funktion
def logout():
    st.session_state['logged_in'] = False
    st.session_state['username'] = ''
    st.success("Sie haben sich erfolgreich abgemeldet.")

# App-Struktur
if st.session_state['logged_in']:
    main_page()
    if st.button("Abmelden"):
        logout()
else:
    login()
