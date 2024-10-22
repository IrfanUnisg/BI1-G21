import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Page title
st.title("Live-Tracking Dashboard")

# Live consumption data
st.subheader("Live Daten")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Aktueller Verbrauch", "1'096 W")
with col2:
    st.metric("Aktueller Bezug", "895 W")
with col3:
    st.metric("Aktuelle Solarleistung", "201 W")
with col4:
    st.metric("Warmwasser Temperatur", "46 °C")

# Example of power consumption and solar power generation over time (simulating the data from the image)
time = pd.date_range(start="2023-10-19 00:00", end="2023-10-19 23:59", freq="5min")
consumption = np.random.uniform(0.5, 1.5, len(time))  # Simulate power consumption
solar = np.random.uniform(0.1, 1.2, len(time))  # Simulate solar power generation

# Create a DataFrame
data = pd.DataFrame({"Time": time, "Consumption (kW)": consumption, "Solar Power (kW)": solar})

# Plot energy usage over time
fig = go.Figure()

# Plot consumption
fig.add_trace(go.Scatter(
    x=data['Time'], y=data['Consumption (kW)'], mode='lines', name='Verbrauch',
    line=dict(color='blue', width=2)
))

# Plot solar power generation
fig.add_trace(go.Scatter(
    x=data['Time'], y=data['Solar Power (kW)'], mode='lines', name='Solarleistung',
    line=dict(color='yellow', width=2)
))

# Update layout
fig.update_layout(
    title="Energieverbrauch und Solarproduktion",
    xaxis_title="Zeit",
    yaxis_title="Leistung (kW)",
    height=500,
    xaxis_rangeslider_visible=True
)

# Display the plot
st.plotly_chart(fig, use_container_width=True)

# Summary of energy usage
st.markdown("---")
st.subheader("Zusammenfassung")

# Static summary values (using values from the image)
col5, col6, col7, col8 = st.columns(4)
with col5:
    st.metric("Verbrauch", "31.9 kWh")
with col6:
    st.metric("Solarenegie", "4.3 kWh")
with col7:
    st.metric("Eigenverbrauch", "4.2 kWh")
with col8:
    st.metric("Bezug", "27.7 kWh")
