import streamlit as st
import hmac
import plotly.graph_objects as go

st.set_page_config(page_title="Stromkonto", page_icon="sk.png")

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
col1, col2 = st.columns([1, 4])
with col1:
    st.image("sk.png", width=100)

with col2:
    st.title("Stromkonto")

preis = 0.1
stromverbrauch = 500
guthaben = st.session_state.get("guthaben", 600)
kapazitaet = 1000
cash = st.session_state.get("cash", 508)

# Kontoübersicht (Stromguthaben)
st.subheader("Stromkonto")
st.write(f"Ihr aktuelles Stromguthaben: {guthaben} kWh")
st.write(f"Ihr Kontoguthaben: {cash} CHF")

# Create the gauge chart once and store it in session state
if "gauge_chart" not in st.session_state:
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=guthaben,
        gauge={'axis': {'range': [0, kapazitaet]},
               'bar': {'color': "blue"}},
        title={'text': "Battery State"},
    ))
    st.session_state["gauge_chart"] = fig

# Display the gauge chart (use Plotly's figure object from session state)
chart_plot = st.plotly_chart(st.session_state["gauge_chart"], use_container_width=True)

# Strom kaufen/verkaufen
st.subheader("Stromhandel")

trade_type = st.radio("Möchten Sie Strom kaufen oder verkaufen?", ("Kaufen", "Verkaufen"))
trade_amount = st.number_input(f"Wählen Sie die Menge an Strom zum {trade_type.lower()} (kWh)", min_value=0)

if st.button(f"{trade_type} bestätigen"):
    total_price = trade_amount * preis

    if trade_type == "Kaufen":
        if total_price <= cash:
            guthaben += trade_amount
            cash -= total_price
            st.success(f"Sie haben erfolgreich {trade_amount} kWh gekauft.")
        else:
            st.error("Nicht genügend Guthaben!")
    else:  # Verkaufen
        if trade_amount <= guthaben:
            guthaben -= trade_amount
            cash += total_price
            st.success(f"Sie haben erfolgreich {trade_amount} kWh verkauft.")
        else:
            st.error("Nicht genügend Strom zu verkaufen!")

    # Update the session state with the new values
    st.session_state["guthaben"] = guthaben
    st.session_state["cash"] = cash

    # Update the existing gauge chart with new values
    st.session_state["gauge_chart"].data[0].value = guthaben

    # Rerender the updated chart in the same place
    chart_plot.plotly_chart(st.session_state["gauge_chart"], use_container_width=True)
