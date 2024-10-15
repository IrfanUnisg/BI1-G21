import streamlit as st
stromverbrauch = st.session_state.get("stromverbrauch", "Nicht verfügbar")
st.subheader("Stromverbrauch")
st.write(f"Ihr aktueller Stromverbrauch: {stromverbrauch} kWh")
