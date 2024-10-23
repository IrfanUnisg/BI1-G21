import streamlit as st

# Seite konfigurieren
st.set_page_config(page_title="Abonnementpläne", layout="wide")

# CSS für zentrierten Titel
st.markdown("""
    <style>
    .center-title {
        text-align: center;
    }
    .table {
        width: 100%;
        margin-bottom: 1rem;
        background-color: transparent;
        border-collapse: collapse;
        text-align: center;
    }
    .table th, .table td {
        padding: 0.75rem;
        vertical-align: top;
        border: 1px solid #dee2e6;
    }
    .table thead th {
        vertical-align: bottom;
        border-bottom: 2px solid #dee2e6;
    }
    .table tbody + tbody {
        border-top: 2px solid #dee2e6;
    }
    .basic {
        background-color: #d3e4cd;  /* Light green for Basic */
    }
    .medium {
        background-color: #ade8f4;  /* Light blue for Medium */
    }
    .premium {
        background-color: #caf0f8;  /* Light teal for Premium */
    }
    </style>
""", unsafe_allow_html=True)

# Seiten-Titel zentriert
st.markdown("<h1 class='center-title'>Vergleich der Abonnementpläne</h1>", unsafe_allow_html=True)

# HTML für die farbige Tabelle
st.markdown("""
    <table class="table">
        <thead>
            <tr>
                <th>Merkmal</th>
                <th class="basic">Basic Plan</th>
                <th class="medium">Medium Plan</th>
                <th class="premium">Premium Plan</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Preis</td>
                <td class="basic">CHF 0</td>
                <td class="medium">CHF 12.90</td>
                <td class="premium">CHF 18.90</td>
            </tr>
            <tr>
                <td>Kapazität Rent-a-Virtual-Battery</td>
                <td class="basic">Keine</td>
                <td class="medium">3000 kWh</td>
                <td class="premium">Unlimitiert</td>
            </tr>
            <tr>
                <td>Tracking & Empfehlungen</td>
                <td class="basic">Basic Dashboard</td>
                <td class="medium">Volles Dashboard</td>
                <td class="premium">Volles Dashboard</td>
            </tr>
            <tr>
                <td>Strom-Sharing</td>
                <td class="basic">Nicht verfügbar</td>
                <td class="medium">3 weitere Haushalte</td>
                <td class="premium">5 weitere Haushalte</td>
            </tr>
            <tr>
                <td>Strom-Coin</td>
                <td class="basic">Nicht verfügbar</td>
                <td class="medium">Nicht verfügbar</td>
                <td class="premium">Jährliche Ausschüttung</td>
            </tr>
            <tr>
                <td>Strom-Debitkarte</td>
                <td class="basic">Nicht verfügbar</td>
                <td class="medium">Nicht verfügbar</td>
                <td class="premium">Verfügbar</td>
            </tr>
            <tr>
                <td>Ranking</td>
                <td class="basic">Verfügbar</td>
                <td class="medium">Verfügbar</td>
                <td class="premium">Verfügbar</td>
            </tr>
            <tr>
                <td>Loyalty / Referral</td>
                <td class="basic">Nicht verfügbar</td>
                <td class="medium">Limitiert verfügbar</td>
                <td class="premium">Ganzes Angebot</td>
            </tr>
        </tbody>
    </table>
""", unsafe_allow_html=True)
