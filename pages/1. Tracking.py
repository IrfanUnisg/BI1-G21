import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Page title
st.title("Solar Tracking Dashboard")

# Sample data (can be replaced with real-time data)
data = {
    'Monat': ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt'],
    'Erzeugte Energie (kWh)': [300, 320, 400, 450, 500, 550, 600, 620, 500, 450],
    'Kosten ohne Stromkonto (CHF)': [120, 128, 160, 180, 200, 220, 240, 248, 200, 180],
    'Kosten mit Stromkonto (CHF)': [100, 106, 130, 150, 165, 185, 200, 210, 170, 155],
    'Gesparte Kosten durch Solaranlage (CHF)': [45.1, 48, 60, 67, 75, 83, 90, 93, 75, 67],
    'Ersparnisse durch Stromkonto (CHF)': [6, 5.6, 8, 7, 6, 7, 7, 6, 8, 7],
    'Stromverbrauch (kWh)': [250, 260, 300, 320, 350, 380, 400, 420, 380, 350]  # Sample consumption
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Electricity costs: Comparison without and with electricity account
st.subheader("Stromkosten: Vergleich ohne/mit Stromkonto")

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
# Additional energy data
st.subheader("Weitere Energiedaten")

col1, col2, col3 = st.columns([1, 1, 1])

# Total generated energy
col1.metric("Gesamte erzeugte Energie (kWh)", f"{df['Erzeugte Energie (kWh)'].sum()} kWh")

# Total savings from solar system
col2.metric("Gesamt eingesparte Kosten durch Solaranlage (CHF)", f"{df['Gesparte Kosten durch Solaranlage (CHF)'].sum():.2f} CHF")

# Total savings from the electricity account
col3.metric("Gesamt eingesparte Kosten durch Stromkonto (CHF)", f"{df['Ersparnisse durch Stromkonto (CHF)'].sum():.2f} CHF")

st.markdown("---")

# Current solar system performance
st.subheader("Aktuelle Solardaten")
col4, col5 = st.columns([1, 1])

# Example for current values
current_energy = 15.7  # kWh
current_savings = 9.2  # CHF

# Current data
col4.metric("Aktuell erzeugte Energie (heute)", f"{current_energy} kWh")
col5.metric("Aktuelle Einsparungen (heute)", f"{current_savings:.2f} CHF")
st.markdown("---")
# Chart for generated energy
st.subheader("Monatliche erzeugte Energie")
st.write("Dieses Diagramm zeigt die monatliche Energieproduktion Ihrer Solaranlage, einschließlich des Stromverbrauchs.")

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
st.subheader("Spotmarkt Strompreisentwicklung (letzte Woche)")
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
