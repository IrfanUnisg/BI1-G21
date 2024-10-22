import streamlit as st

# Seite konfigurieren
st.set_page_config(page_title="Ranking", page_icon="⚡", layout="centered")

# Fiktive Daten für Rankings
ranking_schweiz = [
    {"Rang": 1, "Name": "Lukas Meier", "Blitze": 120},
    {"Rang": 2, "Name": "Sarah Müller", "Blitze": 115},
    {"Rang": 3, "Name": "Thomas Schmid", "Blitze": 110},
    {"Rang": 4, "Name": "Claudia Huber", "Blitze": 105},
    {"Rang": 5, "Name": "Michael Weber", "Blitze": 100},
]

ranking_gemeinde = [
    {"Rang": 1, "Name": "Anna Steiner", "Blitze": 90},
    {"Rang": 2, "Name": "Jonas Keller", "Blitze": 85},
    {"Rang": 3, "Name": "Laura Frei", "Blitze": 80},
    {"Rang": 4, "Name": "Peter Graf", "Blitze": 75},
    {"Rang": 5, "Name": "Monika Berger", "Blitze": 70},
]

ranking_freunde = [
    {"Rang": 1, "Name": "Luc Fischer", "Blitze": 65},
    {"Rang": 2, "Name": "Irfan Kujovic", "Blitze": 60},
    {"Rang": 3, "Name": "Celia Bührer", "Blitze": 55},
    {"Rang": 4, "Name": "Marco Köhler", "Blitze": 50},
    {"Rang": 5, "Name": "Flurin Oehler", "Blitze": 45},
]

# Hilfsfunktion, um eine HTML-Tabelle zu generieren
def generate_table(data):
    html = "<table style='width:100%; border-collapse: collapse; border: 1px solid black;'>"
    html += "<thead><tr style='background-color: #f2f2f2;'>"
    html += "<th style='border: 1px solid black; padding: 8px;'>Rang</th>"
    html += "<th style='border: 1px solid black; padding: 8px;'>Name</th>"
    html += "<th style='border: 1px solid black; padding: 8px;'>Blitze</th>"
    html += "</tr></thead><tbody>"
    
    for entry in data:
        html += f"<tr><td style='border: 1px solid black; padding: 8px;'>{entry['Rang']}</td>"
        html += f"<td style='border: 1px solid black; padding: 8px;'>{entry['Name']}</td>"
        html += f"<td style='border: 1px solid black; padding: 8px;'>{entry['Blitze']}</td></tr>"
    
    html += "</tbody></table>"
    return html

# Seite Titel
st.markdown("<h1 style='text-align: center;'>⚡ Ranking ⚡</h1>", unsafe_allow_html=True)
st.markdown("---")

# Ranking Schweiz
st.markdown("<h2 style='text-align: center;'>Schweiz</h2>", unsafe_allow_html=True)
st.markdown(generate_table(ranking_schweiz), unsafe_allow_html=True)

st.markdown("---")

# Ranking Gemeinde
st.markdown("<h2 style='text-align: center;'>Gemeinde Uzwil</h2>", unsafe_allow_html=True)
st.markdown(generate_table(ranking_gemeinde), unsafe_allow_html=True)

st.markdown("---")

# Ranking Freunde
st.markdown("<h2 style='text-align: center;'>Freunde</h2>", unsafe_allow_html=True)
st.markdown(generate_table(ranking_freunde), unsafe_allow_html=True)

# Abschluss
st.write("Diese Ranglisten basieren auf der Anzahl der Blitze, die durch Generieren von Strom gesammelt wurden. Je mehr Blitze, desto höher das Ranking!")
