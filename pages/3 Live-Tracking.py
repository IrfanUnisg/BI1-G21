import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
st.set_page_config(layout="wide")
# Custom CSS for centering and stacking metric titles and values
st.markdown("""
    <style>
        .stMetric label {
            display: block;
            font-size: 14px;
            margin-bottom: 5px;
            text-align: center;
        }
        .stMetric div {
            text-align: center;
        }
        h1, h2, h3 {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Page title
st.markdown("<h1 style='text-align: center;'>Live-Tracking Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")
# Live consumption data
st.markdown("<h2 style='text-align: center;'>Live Daten</h2>", unsafe_allow_html=True)

# Centered columns for live data metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Aktueller Verbrauch", value="1'096 W")
with col2:
    st.metric(label="Aktueller Bezug", value="895 W")
with col3:
    st.metric(label="Aktuelle Solarleistung", value="201 W")
with col4:
    st.metric(label="Warmwasser Temperatur", value="55 °C")

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

# Plot consumption with dark blue color
fig.add_trace(go.Scatter(
    x=data['Time'], y=data['Consumption (kW)'], mode='lines', name='Verbrauch',
    line=dict(color='#044b5b', width=3)  # Dark blue
))

# Plot solar power generation with yellow color
fig.add_trace(go.Scatter(
    x=data['Time'], y=data['Solar Power (kW)'], mode='lines', name='Solarleistung',
    line=dict(color='#facb04', width=3)  # Yellow as specified
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
    # Set both the plot background and the paper (figure) background to #f0f4f4
    plot_bgcolor='#f0f4f4',  # Background color of the plot area
    paper_bgcolor='#f0f4f4',  # Background color of the entire figure
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
st.markdown("---")
# Display the plot
st.plotly_chart(fig, use_container_width=True)

# Add a horizontal line
st.markdown("---")

# Summary of energy usage below the chart
st.markdown("<h2 style='text-align: center;'>Zusammenfassung (Tag)</h2>", unsafe_allow_html=True)

# Static summary values displayed in 4 columns with values stacked under the labels
col5, col6, col7, col8 = st.columns(4)

with col5:
    st.metric(label="Verbrauch", value="15.7 kWh")
with col6:
    st.metric(label="Solarenegie", value="7.3 kWh")
with col7:
    st.metric(label="Eigenverbrauch", value="4.6 kWh")
with col8:
    st.metric(label="Bezug", value="11.1 kWh")
