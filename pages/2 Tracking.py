import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

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
    </style>
""", unsafe_allow_html=True)

# Page title
st.markdown("<h1 style='text-align: center;'>Solar Tracking Dashboard</h1>", unsafe_allow_html=True)

# Sample data (can be replaced with real-time data)
data = {
    'Monat': ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt'],
    'Erzeugte Energie (kWh)': [300, 320, 400, 450, 500, 550, 600, 620, 500, 400],
    'Kosten ohne Stromkonto (CHF)': [240, 220, 180, 160, 150, 180, 200, 220, 230, 245],
    'Kosten mit Stromkonto (CHF)': [200, 175, 150, 145, 140, 150, 180, 195, 200, 205],
    'Gesparte Kosten durch Solaranlage (CHF)': [45.1, 48, 60, 67, 75, 83, 90, 93, 75, 67],
    'Ersparnisse durch Stromkonto (CHF)': [6, 5.6, 8, 7, 6, 7, 7, 6, 8, 7],
    'Stromverbrauch (kWh)': [450, 400, 350, 300, 250, 240, 260, 320, 370, 410]  # Sample consumption
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Electricity costs: Comparison without and with electricity account
st.markdown("<h2 style='text-align: center;'>Stromkosten: Vergleich ohne/mit Stromkonto</h2>", unsafe_allow_html=True)

# Plotly bar chart
fig = go.Figure()

# Costs without electricity account
fig.add_trace(go.Bar(
    x=df['Monat'],
    y=df['Kosten ohne Stromkonto (CHF)'],
    name='Kosten ohne Stromkonto',
    marker_color='#044b5b'
))

# Costs with electricity account (changed to yellow)
fig.add_trace(go.Bar(
    x=df['Monat'],
    y=df['Kosten mit Stromkonto (CHF)'],
    name='Kosten mit Stromkonto',
    marker_color='#facb04'
))

# Adjust layout
fig.update_layout(
    barmode='group',
    xaxis_title="Monat",
    yaxis_title="Kosten (CHF)",
    margin=dict(l=40, r=40, t=40, b=40),
    height=400,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

# Display chart
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Section: Additional energy data
st.markdown("<h2 style='text-align: center;'>Weitere Energiedaten</h2>", unsafe_allow_html=True)

# Centered columns for metrics under "Weitere Energiedaten"
col1, col2, col3 = st.columns(3)

# Total generated energy
col1.metric(label="Gesamte erzeugte Energie (kWh)", value=f"{df['Erzeugte Energie (kWh)'].sum()} kWh")

# Total savings from solar system
col2.metric(label="Gesamt eingesparte Kosten durch Solaranlage (CHF)", value=f"{df['Gesparte Kosten durch Solaranlage (CHF)'].sum():.2f} CHF")

# Total savings from the electricity account
col3.metric(label="Gesamt eingesparte Kosten durch Stromkonto (CHF)", value=f"{df['Ersparnisse durch Stromkonto (CHF)'].sum():.2f} CHF")

st.markdown("---")

# Section: Current solar system performance
st.markdown("<h2 style='text-align: center;'>Aktuelle Solardaten</h2>", unsafe_allow_html=True)

# Centered columns for metrics under "Aktuelle Solardaten"
col4, col5, col6 = st.columns(3)

# Example for current values
current_energy = 15.7  # kWh
current_savings = 2.5  # CHF
current_solar = 0.24

# Current data
col4.metric(label="Heute erzeugte Energie (kWh)", value=f"{current_energy} kWh")
col5.metric(label="Heute eingesparte Kosten durch Solaranlage (CHF)", value=f"{current_savings:.2f} CHF")
col6.metric(label="Heute eingesparte Kosten durch Stromkonto (CHF)", value=f"{current_solar:.2f} CHF")

st.markdown("---")

# Chart for generated energy
st.markdown("<h2 style='text-align: center;'>Monatliche erzeugte Energie</h2>", unsafe_allow_html=True)


# Line chart for energy generation and consumption
fig_energy = go.Figure()
fig_energy.add_trace(go.Scatter(x=df['Monat'], y=df['Erzeugte Energie (kWh)'], mode='lines+markers', name='Erzeugte Energie', line=dict(color='#044b5b')))
fig_energy.add_trace(go.Scatter(x=df['Monat'], y=df['Stromverbrauch (kWh)'], mode='lines+markers', name='Stromverbrauch', line=dict(color='#facb04')))

# Adjust layout
fig_energy.update_layout(
    title="Monatliche Energieproduktion und Stromverbrauch",
    xaxis_title="Monat",
    yaxis_title="Energie (kWh)",
    height=400,
)

st.plotly_chart(fig_energy, use_container_width=True)

# Generate hourly prices for October (31 days)
np.random.seed(0)  # For reproducibility
days = 31  # Number of days in October
hours = np.arange(1, 25)  # Hourly data from 1 to 24
min_price = 5  # Minimum price in Rp
max_price = 10  # Maximum price in Rp

# Initialize the list of hourly prices
hourly_prices = []

# Start with a random price within the specified range
previous_price = np.random.uniform(min_price, max_price)

# Generate hourly prices for each day
for day in range(days):
    for hour in range(24):
        # Incrementally adjust the price within a smaller range, e.g., ±0.5 Rp
        price_change = np.random.uniform(-0.5, 0.5)  # Reduce the fluctuation
        current_price = previous_price + price_change
        # Ensure the price stays within the defined bounds
        current_price = max(min(current_price, max_price), min_price)  
        hourly_prices.append(current_price)
        previous_price = current_price  # Update previous price for the next hour

# Create DataFrame for hourly prices
price_df = pd.DataFrame({
    'Stunde': np.tile(hours, days),
    'Tag': np.repeat(np.arange(1, days + 1), 24),
    'Preis (Rp)': hourly_prices
})

st.markdown("---")

# Plot hourly prices for the last week
st.markdown("<h2 style='text-align: center;'>Spotmarkt Strompreisentwicklung (letzte Woche)</h2>", unsafe_allow_html=True)

# Filter for the last week of October (assuming the month has 31 days)
last_week_price_df = price_df[price_df['Tag'] > 24]  # Filter for days greater than 24 (25th to 31st)

fig_prices = go.Figure()

fig_prices.add_trace(go.Scatter(
    x=last_week_price_df['Tag'].astype(str) + ' ' + last_week_price_df['Stunde'].astype(str) + ':00',  # Combine day and hour for x-axis labels
    y=last_week_price_df['Preis (Rp)'],
    mode='lines+markers',
    name='Strompreise (Rp)',
    line=dict(color='#044b5b')
))

# Adjust layout for price chart
fig_prices.update_layout(
    xaxis_title="Zeit",
    yaxis_title="Preis (Rp)",
    height=400,
    margin=dict(l=40, r=40, t=40, b=40),
    xaxis_tickangle=-45,  # Rotate x-axis labels for better visibility
)

# Display the price chart
st.plotly_chart(fig_prices, use_container_width=True)
