import streamlit as st

# Hauptseite für Stromverbrauch, Kontoübersicht und Handel

col1, col2 = st.columns([1, 3])  # Der erste Parameter gibt das relative Verhältnis der Spalten an

with col1:
    st.image("sk.png", width=100)

with col2:
    st.title("Stromkonto")

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.subheader("Please enter the password.")
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if not check_password():
    st.stop()  # Do not continue if check_password is not True.


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
