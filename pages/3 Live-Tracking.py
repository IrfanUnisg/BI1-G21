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
    st.metric("Warmwasser Temperatur", "55 °C")

# Example of power consumption and solar power generation over time (simulating the data from the image)
time = pd.date_range(start="2023-10-19 00:00", end="2023-10-19 23:59", freq="5min")
consumption = np.random.uniform(0.5, 1.5, len(time))  # Simulate power consumption
solar = np.random.uniform(0.1, 1.2, len(time))  # Simulate solar power generation

# Create a DataFrame
data = pd.DataFrame({"Time": time, "Consumption (kW)": consumption, "Solar Power (kW)": solar})

# Filter data between 7:00 AM and 6:00 PM
data = data[(data['Time'].dt.time >= pd.to_datetime('07:00').time()) & 
            (data['Time'].dt.time <= pd.to_datetime('18:00').time())]

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
    title="Energieverbrauch und Solarproduktion (7:00 - 18:00 Uhr)",
    xaxis_title="Zeit",
    yaxis_title="Leistung (kW)",
    height=500,
    xaxis_rangeslider_visible=True
)

# Layout to display chart next to summary
col_chart, col_summary = st.columns([2, 1])

# Display the plot in the first column
with col_chart:
    st.plotly_chart(fig, use_container_width=True)

# Summary of energy usage in the second column
with col_summary:
    st.markdown("---")
    st.subheader("Zusammenfassung (Tag)")

    # Static summary values with correct column setup
    col5, col6, col7, col8 = st.columns(4)  # Create 4 columns

    with col5:
        st.metric("Verbrauch", "15.2 kWh")
    with col6:
        st.metric("Solarenegie", "7.3 kWh")
    with col7:
        st.metric("Eigenverbrauch", "4.2 kWh")
    with col8:
        st.metric("Bezug", "27.7 kWh")
