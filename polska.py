import streamlit as st

st.set_page_config(page_title="Ostatnie mecze reprezentacji Polski", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    .wynik-row { display: flex; flex-direction: column; align-items: center; margin: 30px 0; border-bottom: 1px solid #222; padding-bottom: 20px; }
    .mecz-kontener { display: flex; justify-content: center; align-items: center; width: 100%; }
    .druzyna { font-size: 35px; font-weight: bold; color: white; width: 320px; text-align: center; }
    .wynik-liczba { font-size: 60px; font-weight: 900; min-width: 150px; text-align: center; }
    .flaga-img { width: 85px; height: auto; border-radius: 8px; box-shadow: 0 0 12px rgba(255,255,255,0.15); }
    .info-linia { font-size: 14px; color: #777777; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 1px; font-weight: bold; }
    .turniej-euro { color: #FFD700; font-weight: 900; } /* Złoty kolor dla Euro/MŚ */
    </style>
    """, unsafe_allow_html=True)

# s: W(wygrana), L(przegrana), D(remis) | miejsce: dom / wyjazd
# t: nazwa turnieju | wazne: True (dla złotej czcionki)
mecze = [
    {"o": "Szwecja", "f": "https://flagcdn.com/w160/se.png", "w": "3 : 2", "d": "31.03.2026", "s": "L", "miejsce": "wyjazd", "t": "Eliminacje MŚ - Baraż", "wazne": True},
    {"o": "Albania", "f": "https://flagcdn.com/w160/al.png", "w": "2 : 1", "d": "26.03.2026", "s": "W", "miejsce": "dom", "t": "Eliminacje MŚ - Baraż", "wazne": True},
    {"o": "Malta", "f": "https://flagcdn.com/w160/mt.png", "w": "2 : 3", "d": "17.11.2025", "s": "W", "miejsce": "wyjazd", "t": "Eliminacje MŚ", "wazne": False},
    {"o": "Holandia", "f": "https://flagcdn.com/w160/nl.png", "w": "1 : 1", "d": "14.11.2025", "s": "D", "miejsce": "dom", "t": "Eliminacje MŚ", "wazne": False},
    {"o": "Litwa", "f": "https://flagcdn.com/w160/lt.png", "w": "0 : 2", "d": "12.10.2025", "s": "W", "miejsce": "wyjazd", "t": "Eliminacje MŚ", "wazne": False},
    {"o": "Nowa Zelandia", "f": "https://flagcdn.com/w160/nz.png", "w": "1 : 0", "d": "09.10.2025", "s": "W", "miejsce": "dom", "t": "Mecz towarzyski", "wazne": False},
    {"o": "Finlandia", "f": "https://flagcdn.com/w160/fi.png", "w": "3 : 1", "d": "07.09.2025", "s": "W", "miejsce": "dom", "t": "Eliminacje MŚ", "wazne": False},
    {"o": "Holandia", "f": "https://flagcdn.com/w160/nl.png", "w": "1 : 1", "d": "04.09.2025", "s": "D", "miejsce": "wyjazd", "t": "Eliminacje MŚ", "wazne": False},
    {"o": "Finlandia", "f": "https://flagcdn.com/w160/fi.png", "w": "2 : 1", "d": "10.06.2025", "s": "L", "miejsce": "wyjazd", "t": "Eliminacje MŚ", "wazne": False},
    {"o": "Mołdawia", "f": "https://flagcdn.com/w160/md.png", "w": "2 : 0", "d": "06.06.2025", "s": "W", "miejsce": "dom", "t": "Mecz towarzyski", "wazne": False},
    {"o": "Malta", "f": "https://flagcdn.com/w160/mt.png", "w": "2 : 0", "d": "24.03.2025", "s": "W", "miejsce": "dom", "t": "Eliminacje MŚ", "wazne": False},
    {"o": "Litwa", "f": "https://flagcdn.com/w160/lt.png", "w": "1 : 0", "d": "21.03.2025", "s": "W", "miejsce": "dom", "t": "Eliminacje MŚ", "wazne": False},
    {"o": "Szkocja", "f": "https://flagcdn.com/w160/gb-sct.png", "w": "1 : 2", "d": "18.11.2024", "s": "L", "miejsce": "dom", "t": "Liga Narodów", "wazne": False},
    {"o": "Portugalia", "f": "https://flagcdn.com/w160/pt.png", "w": "5 : 1", "d": "15.11.2024", "s": "L", "miejsce": "wyjazd", "t": "Liga Narodów", "wazne": False},
    {"o": "Chorwacja", "f": "https://flagcdn.com/w160/hr.png", "w": "3 : 3", "d": "15.10.2024", "s": "D", "miejsce": "dom", "t": "Liga Narodów", "wazne": False}
]

st.markdown("<h1 style='text-align: center; font-size: 45px; margin-bottom: 40px;'>OSTATNIE MECZE REPREZENTACJI POLSKI</h1>", unsafe_allow_html=True)

flaga_pl = "https://flagcdn.com/w160/pl.png"

for m in mecze:
    # Ustalanie koloru wyniku
    kolor_wyniku = "#FFFFFF"
    if m['s'] == "W": kolor_wyniku = "#00FF00"
    elif m['s'] == "L": kolor_wyniku = "#FF0000"

    # Sprawdzanie czy turniej ma być złoty
    klasa_turnieju = 'class="turniej-euro"' if m['wazne'] else ""

    # Logika stron
    if m['miejsce'] == "dom":
        l_n, l_f = "POLSKA", flaga_pl
        p_n, p_f = m['o'].upper(), m['f']
        w_t = m['w']
    else:
        l_n, l_f = m['o'].upper(), m['f']
        p_n, p_f = "POLSKA", flaga_pl
        res = m['w'].split(" : ")
        w_t = f"{res[0]} : {res[1]}"

    st.markdown(f'''
        <div class="wynik-row">
            <div class="info-linia">
                {m['d']} | <span {klasa_turnieju}>{m['t']}</span> | {"DOM" if m['miejsce'] == 'dom' else 'WYJAZD'}
            </div>
            <div class="mecz-kontener">
                <img src="{l_f}" class="flaga-img">
                <span class="druzyna">{l_n}</span>
                <span class="wynik-liczba" style="color: {kolor_wyniku};">{w_t}</span>
                <span class="druzyna">{p_n}</span>
                <img src="{p_f}" class="flaga-img">
            </div>
        </div>
    ''', unsafe_allow_html=True)
