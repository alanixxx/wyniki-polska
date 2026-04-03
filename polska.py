import streamlit as st

st.set_page_config(page_title="Wyniki Polska - Pełny Harmonogram", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    .wynik-row { display: flex; flex-direction: column; align-items: center; margin: 30px 0; border-bottom: 1px solid #222; padding-bottom: 20px; }
    .mecz-kontener { display: flex; justify-content: center; align-items: center; width: 100%; }
    .druzyna { font-size: 35px; font-weight: bold; color: white; width: 320px; text-align: center; }
    .wynik-liczba { font-size: 60px; font-weight: 900; min-width: 150px; text-align: center; }
    .flaga-img { width: 85px; height: auto; border-radius: 8px; box-shadow: 0 0 12px rgba(255,255,255,0.15); }
    .data-spotkania { font-size: 14px; color: #777777; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 1px; }
    </style>
    """, unsafe_allow_html=True)

# s: W(wygrana), L(przegrana), D(remis) | miejsce: dom / wyjazd
# Lista na podstawie Twojego screena (od najnowszych)
mecze = [
    {"o": "Szwecja", "f": "https://flagcdn.com/w160/se.png", "w": "3 : 2", "d": "31.03.2026", "s": "L", "miejsce": "wyjazd"},
    {"o": "Albania", "f": "https://flagcdn.com/w160/al.png", "w": "2 : 1", "d": "26.03.2026", "s": "W", "miejsce": "dom"},
    {"o": "Malta", "f": "https://flagcdn.com/w160/mt.png", "w": "2 : 3", "d": "17.11.2025", "s": "W", "miejsce": "wyjazd"},
    {"o": "Holandia", "f": "https://flagcdn.com/w160/nl.png", "w": "1 : 1", "d": "14.11.2025", "s": "D", "miejsce": "dom"},
    {"o": "Litwa", "f": "https://flagcdn.com/w160/lt.png", "w": "0 : 2", "d": "12.10.2025", "s": "W", "miejsce": "wyjazd"},
    {"o": "Nowa Zelandia", "f": "https://flagcdn.com/w160/nz.png", "w": "1 : 0", "d": "09.10.2025", "s": "W", "miejsce": "dom"},
    {"o": "Finlandia", "f": "https://flagcdn.com/w160/fi.png", "w": "3 : 1", "d": "07.09.2025", "s": "W", "miejsce": "dom"},
    {"o": "Holandia", "f": "https://flagcdn.com/w160/nl.png", "w": "1 : 1", "d": "04.09.2025", "s": "D", "miejsce": "wyjazd"},
    {"o": "Finlandia", "f": "https://flagcdn.com/w160/fi.png", "w": "2 : 1", "d": "10.06.2025", "s": "L", "miejsce": "wyjazd"},
    {"o": "Mołdawia", "f": "https://flagcdn.com/w160/md.png", "w": "2 : 0", "d": "06.06.2025", "s": "W", "miejsce": "dom"},
    {"o": "Malta", "f": "https://flagcdn.com/w160/mt.png", "w": "2 : 0", "d": "24.03.2025", "s": "W", "miejsce": "dom"},
    {"o": "Litwa", "f": "https://flagcdn.com/w160/lt.png", "w": "1 : 0", "d": "21.03.2025", "s": "W", "miejsce": "dom"},
    {"o": "Szkocja", "f": "https://flagcdn.com/w160/gb-sct.png", "w": "1 : 2", "d": "18.11.2024", "s": "L", "miejsce": "dom"},
    {"o": "Portugalia", "f": "https://flagcdn.com/w160/pt.png", "w": "5 : 1", "d": "15.11.2024", "s": "L", "miejsce": "wyjazd"},
    {"o": "Chorwacja", "f": "https://flagcdn.com/w160/hr.png", "w": "3 : 3", "d": "15.10.2024", "s": "D", "miejsce": "dom"}
]

st.markdown("<h1 style='text-align: center; font-size: 50px; margin-bottom: 40px;'>HARMONOGRAM MECZÓW REPREZENTACJI</h1>", unsafe_allow_html=True)

flaga_pl = "https://flagcdn.com/w160/pl.png"

for m in mecze:
    kolor = "#FFFFFF"
    if m['s'] == "W": kolor = "#00FF00"
    elif m['s'] == "L": kolor = "#FF0000"

    if m['miejsce'] == "dom":
        l_nazwa, l_flaga = "POLSKA", flaga_pl
        p_nazwa, p_flaga = m['o'].upper(), m['f']
        wynik_tekst = m['w']
    else:
        l_nazwa, l_flaga = m['o'].upper(), m['f']
        p_nazwa, p_flaga = "POLSKA", flaga_pl
        res = m['w'].split(" : ")
        wynik_tekst = f"{res[0]} : {res[1]}" # Wynik zostawiamy jak w tabeli, logika strony zajmie się resztą

    st.markdown(f'''
        <div class="wynik-row">
            <div class="data-spotkania">{m['d']} | {"DOM" if m['miejsce'] == 'dom' else 'WYJAZD'}</div>
            <div class="mecz-kontener">
                <img src="{l_flaga}" class="flaga-img">
                <span class="druzyna">{l_nazwa}</span>
                <span class="wynik-liczba" style="color: {kolor};">{wynik_tekst}</span>
                <span class="druzyna">{p_nazwa}</span>
                <img src="{p_flaga}" class="flaga-img">
            </div>
        </div>
    ''', unsafe_allow_html=True)
