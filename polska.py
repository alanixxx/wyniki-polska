import streamlit as st

st.set_page_config(page_title="Wyniki Polska", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    .wynik-row { display: flex; justify-content: center; align-items: center; margin: 20px 0; flex-direction: column; }
    .mecz-kontener { display: flex; justify-content: center; align-items: center; }
    .druzyna { font-size: 45px; font-weight: bold; padding: 0 30px; color: white; min-width: 300px; text-align: center; }
    .wynik-liczba { font-size: 70px; font-weight: 900; min-width: 180px; text-align: center; }
    .flaga-img { width: 90px; height: auto; border-radius: 8px; }
    .data-spotkania { font-size: 18px; color: #aaaaaa; margin-bottom: -10px; }
    </style>
    """, unsafe_allow_html=True)

# Dane meczów: o-przeciwnik, f-flaga, w-wynik, d-data, s-status (W-wygrana, L-przegrana, D-remis)
mecze = [
    {"o": "Szwecja", "f": "https://flagcdn.com/w160/se.png", "w": "2 : 3", "d": "31.03.2026", "s": "L"},
    {"o": "Albania", "f": "https://flagcdn.com/w160/al.png", "w": "2 : 1", "d": "26.03.2026", "s": "W"},
    {"o": "Malta", "f": "https://flagcdn.com/w160/mt.png", "w": "3 : 2", "d": "17.11.2025", "s": "W"},
    {"o": "Holandia", "f": "https://flagcdn.com/w160/nl.png", "w": "1 : 1", "d": "14.11.2025", "s": "D"},
    {"o": "Litwa", "f": "https://flagcdn.com/w160/lt.png", "w": "2 : 0", "d": "12.10.2025", "s": "W"}
]

st.markdown("<h1 style='text-align: center; font-size: 60px;'>POLSKA - OSTATNIE MECZE</h1>", unsafe_allow_html=True)

for m in mecze:
    # Logika kolorów: Wygrana = Zielony, Przegrana = Czerwony, Remis = Biały
    kolor = "#FFFFFF" # domyślny biały
    if m['s'] == "W": kolor = "#00FF00" # zielony
    elif m['s'] == "L": kolor = "#FF0000" # czerwony

    st.markdown(f'''
        <div class="wynik-row">
            <div class="data-spotkania">{m['d']}</div>
            <div class="mecz-kontener">
                <img src="https://flagcdn.com/w160/pl.png" class="flaga-img">
                <span class="druzyna">POLSKA</span>
                <span class="wynik-liczba" style="color: {kolor};">{m['w']}</span>
                <span class="druzyna">{m['o'].upper()}</span>
                <img src="{m['f']}" class="flaga-img">
            </div>
        </div>
    ''', unsafe_allow_html=True)
