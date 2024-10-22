import streamlit as st

# Seite konfigurieren
st.set_page_config(page_title="Ranking", page_icon="⚡", layout="wide")

# Eigene Blitze
own_blitze = 112

# Fiktive Daten für Rankings
ranking_schweiz = [
    {"Rang": 1, "Name": "Lukas Meier", "Blitze": 563},
    {"Rang": 2, "Name": "Sarah Müller", "Blitze": 554},
    {"Rang": 3, "Name": "Thomas Schmid", "Blitze": 549},
    {"Rang": 4, "Name": "Claudia Huber", "Blitze": 497},
    {"Rang": 5, "Name": "Michael Weber", "Blitze": 486},
]

ranking_gemeinde = [
    {"Rang": 1, "Name": "Anna Steiner", "Blitze": 256},
    {"Rang": 2, "Name": "Jonas Keller", "Blitze": 178},
    {"Rang": 3, "Name": "Laura Frei", "Blitze": 167},
    {"Rang": 4, "Name": "Peter Graf", "Blitze": 145},
    {"Rang": 5, "Name": "Monika Berger", "Blitze": 130},
]

ranking_freunde = [
    {"Rang": 1, "Name": "Luc Fischer", "Blitze": 124},
    {"Rang": 2, "Name": "Irfan Kujovic", "Blitze": 112},
    {"Rang": 3, "Name": "Celia Bührer", "Blitze": 109},
    {"Rang": 4, "Name": "Marco Köhler", "Blitze": 106},
    {"Rang": 5, "Name": "Flurin Oehler", "Blitze": 99},
]

# Hilfsfunktion, um eine HTML-Tabelle zu generieren
def generate_table(data, highlight_value=None):
    html = "<table style='width:100%; border-collapse: collapse; border: 1px solid black;'>"
    html += "<thead><tr style='background-color: #f2f2f2;'>"
    html += "<th style='border: 1px solid black; padding: 8px;'>Rang</th>"
    html += "<th style='border: 1px solid black; padding: 8px;'>Name</th>"
    html += "<th style='border: 1px solid black; padding: 8px;'>Blitze</th>"
    html += "</tr></thead><tbody>"
    
    for entry in data:
        # Highlight row if 'Blitze' matches the highlight_value
        if entry['Blitze'] == highlight_value:
            html += f"<tr style='background-color: #ADD8E6;'><td style='border: 1px solid black; padding: 8px;'>{entry['Rang']}</td>"
            html += f"<td style='border: 1px solid black; padding: 8px;'>{entry['Name']}</td>"
            html += f"<td style='border: 1px solid black; padding: 8px;'>{entry['Blitze']}</td></tr>"
        else:
            html += f"<tr><td style='border: 1px solid black; padding: 8px;'>{entry['Rang']}</td>"
            html += f"<td style='border: 1px solid black; padding: 8px;'>{entry['Name']}</td>"
            html += f"<td style='border: 1px solid black; padding: 8px;'>{entry['Blitze']}</td></tr>"
    
    html += "</tbody></table>"
    return html

# Seite Titel
st.markdown("<h1 style='text-align: center;'>⚡ Ranking ⚡</h1>", unsafe_allow_html=True)
st.markdown("---")

# Anzeige für eigene Blitze (keine Farbänderung mehr)
st.markdown(f"<h2 style='text-align: center;'>Du hast {own_blitze} Blitze gesammelt!</h2>", unsafe_allow_html=True)
st.markdown("---")

# Ranking Schweiz
st.markdown("<h2 style='text-align: center;'>Schweiz</h2>", unsafe_allow_html=True)
st.markdown(generate_table(ranking_schweiz), unsafe_allow_html=True)

st.markdown("---")

# Ranking Gemeinde
st.markdown("<h2 style='text-align: center;'>Gemeinde St.Gallen</h2>", unsafe_allow_html=True)
st.markdown(generate_table(ranking_gemeinde), unsafe_allow_html=True)

st.markdown("---")

# Ranking Freunde, highlighting the row with 112 Blitze
st.markdown("<h2 style='text-align: center;'>Freunde</h2>", unsafe_allow_html=True)
st.markdown(generate_table(ranking_freunde, highlight_value=112), unsafe_allow_html=True)
st.markdown("---")
# Abschluss
st.write("Diese Ranglisten basieren auf der Anzahl der Blitze, die durch Generieren von Strom gesammelt wurden. Je mehr Blitze, desto höher das Ranking!")
