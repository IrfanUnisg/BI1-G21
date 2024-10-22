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
consumption = np.random.uniform(0.5, 1.5, len(time))  # Simulate power consumption

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
solar[start_idx:peak_idx] = np.linspace(0, 1.2, peak_idx - start_idx) + np.random.uniform(-0.1, 0.1, peak_idx - start_idx)
solar[peak_idx:end_idx] = np.linspace(1.2, 0, end_idx - peak_idx) + np.random.uniform(-0.1, 0.1, end_idx - peak_idx)

# Make sure no negative values
solar[solar < 0] = 0

# 
