import streamlit as st
import hmac
import plotly.graph_objects as go
st.set_page_config(page_title="Stromkonto",page_icon="sk.png")
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
    st.subheader("Please enter the password.")
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False
if not check_password():
    st.stop()  # Do not continue if check_password is not True.


# Hauptseite für Stromverbrauch, Kontoübersicht und Handel
col1, col2= st.columns([1,4])
with col1:
    st.image("sk.png", width=100)

with col2:
    st.title("Stromkonto")


preis=0.1
stromverbrauch=500
guthaben=600
kapazitaet=1000
# Übersicht über den Stromverbrauch
st.subheader("Stromverbrauch")
st.write(f"Ihr aktueller Stromverbrauch: {stromverbrauch} kWh")

# Kontoübersicht (Stromguthaben)
st.subheader("Stromkonto")
st.write(f"Ihr aktuelles Stromguthaben: {guthaben} kWh")

# Create a gauge chart
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=guthaben,
    gauge={'axis': {'range': [0, kapazitaet]},
           'bar': {'color': "blue"}},
    title={'text': "Battery State"},
))
# Display the gauge chart
st.plotly_chart(fig)

# Strom kaufen/verkaufen
st.subheader("Stromhandel")

trade_type = st.radio("Möchten Sie Strom kaufen oder verkaufen?", ("Kaufen", "Verkaufen"))
trade_amount = st.number_input(f"Wählen Sie die Menge an Strom zum {trade_type.lower()} (kWh)", min_value=0)

if st.button(f"{trade_type} bestätigen"):
    total_price = trade_amount * preis
    
    if trade_type == "Kaufen":
        if total_price <= guthaben:
            stromverbrauch += trade_amount
            guthaben -= total_price
            st.success(f"Sie haben erfolgreich {trade_amount} kWh gekauft.")
        else:
            st.error("Nicht genügend Guthaben!")
    else:  # Verkaufen
        if trade_amount <= stromverbrauch:
            stromverbrauch -= trade_amount
            guthaben += total_price
            st.success(f"Sie haben erfolgreich {trade_amount} kWh verkauft.")
        else:
            st.error("Nicht genügend Strom zu verkaufen!")
