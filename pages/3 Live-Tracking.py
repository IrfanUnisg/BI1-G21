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

# Example of power consumption and solar power generation over time (simulating the data for the full day)
time = pd.date_range(start="2023-10-20 00:00", end="2023-10-20 23:59", freq="5min")
# Reduce the range of random consumption to simulate less fluctuation
consumption = np.random.uniform(0.9, 1.2, len(time))  # Simulate power consumption with reduced variation

# Initialize solar power array
solar = np.zeros(len(time))

# Solar power is active between 08:30 and 18:30 with a peak at 13:30
start_time = pd.Timestamp("2023-10-20 08:30")
end_time = pd.Timestamp("2023-10-20 18:30")
peak_time = pd.Timestamp("2023-10-20 13:30")

# Indices corresponding to the start, peak, and end of solar production
start_idx = np.where(time == start_time)[0][0]
peak_idx = np.where(time == peak_time)[0][0]
end_idx = np.where(time == end_time)[0][0]

# Solar power ramps up and down with some random variability
solar[start_idx:peak_idx] = np.linspace(0, 1.2, peak_idx - start_idx) + np.random.uniform(-0.05, 0.05, peak_idx - start_idx)
solar[peak_idx:end_idx] = np.linspace(1.2, 0, end_idx - peak_idx) + np.random.uniform(-0.05, 0.05, end_idx - peak_idx)

# Make sure no negative values
solar[solar < 0] = 0

# Create a DataFrame
data = pd.DataFrame({"Time": time, "Consumption (kW)": consumption, "Solar Power (kW)": solar})

# Plot energy usage over time
fig = go.Figure()

# Plot consumption
fig.add_trace(go.Scatter(
    x=data['Time'], y=data['Consumption (kW)'], mode='lines', name='Verbrauch',
    line=dict(color='deepskyblue', width=3)
))

# Plot solar power generation
fig.add_trace(go.Scatter(
    x=data['Time'], y=data['Solar Power (kW)'], mode='lines', name='Solarleistung',
    line=dict(color='yellow', width=3)
))

# Update layout for style and appearance
fig.update_layout(
    title="Energieverbrauch und Solarproduktion am 20. Oktober",
    xaxis_title="Zeit",
    yaxis_title="Leistung (kW)",
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickformat="%H:%M",  # Format for time as hour:minute
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=True,
        zeroline=False,
        showline=True,
        showticklabels=True,
    ),
    plot_bgcolor='white',
    showlegend=True,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    height=500,
)

# Display the plot
st.plotly_chart(fig, use_container_width=True)

# Add a horizontal line
st.markdown("---")

# Summary of energy usage below the chart
st.subheader("Zusammenfassung (Tag)")

# Static summary values displayed in 4 columns
col5, col6, col7, col8 = st.columns(4)

with col5:
    st.metric("Verbrauch", "15.7 kWh")
with col6:
    st.metric("Solarenegie", "7.3 kWh")
with col7:
    st.metric("Eigenverbrauch", "4.2 kWh")
with col8:
    st.metric("Bezug", "11.1 kWh")
