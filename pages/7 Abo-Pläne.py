import streamlit as st

# Seite konfigurieren
st.set_page_config(page_title="Abonnementpläne", layout="wide")

# Seiten-Titel
st.title("Vergleich der Abonnementpläne")

# HTML für die farbige Tabelle
st.markdown("""
    <style>
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
                <td class="medium">CHF 14.90</td>
                <td class="premium">CHF 22</td>
            </tr>
            <tr>
                <td>Kapazität Rent-a-Virtual-Battery</td>
                <td class="basic">Keine</td>
                <td class="medium">3000 kWh</td>
                <td class="premium">Unlimitiert</td>
            </tr>
            <tr>
                <td>Tracking & Empfehlungen</td>
                <td class="basic">Keine</td>
                <td class="medium">Volles Dashboard</td>
                <td class="premium">Volles Dashboard</td>
            </tr>
            <tr>
                <td>Stromsharing</td>
                <td class="basic">Nicht verfügbar</td>
                <td class="medium">Verfügbar (Nur für Auto)</td>
                <td class="premium">Verfügbar (Ganzes Angebot)</td>
            </tr>
            <tr>
                <td>Swisscoin</td>
                <td class="basic">Nicht verfügbar</td>
                <td class="medium">1 Swisscoin</td>
                <td class="premium">2 Swisscoins</td>
            </tr>
            <tr>
                <td>Stromkarte</td>
                <td class="basic">Nicht verfügbar</td>
                <td class="medium">Verfügbar</td>
                <td class="premium">Verfügbar</td>
            </tr>
            <tr>
                <td>Vergleich zu Gemeinde</td>
                <td class="basic">Verfügbar</td>
                <td class="medium">Verfügbar</td>
                <td class="premium">Verfügbar</td>
            </tr>
            <tr>
                <td>Loyalty / Referral</td>
                <td class="basic">Nicht verfügbar</td>
                <td class="medium">Nur für Auto</td>
                <td class="premium">Ganzes Angebot</td>
            </tr>
        </tbody>
    </table>
""", unsafe_allow_html=True)
