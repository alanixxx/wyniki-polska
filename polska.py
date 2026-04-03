import streamlit as st

st.set_page_config(page_title="Wyniki Polska", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    .wynik-row { display: flex; flex-direction: column; align-items: center; margin: 25px 0; }
    .mecz-kontener { display: flex; justify-content: center; align-items: center; width: 100%; }
    .druzyna { font-size: 40px; font-weight: bold; color: white; width: 350px; text-align: center; }
    .wynik-liczba { font-size: 65px; font-weight: 900; min-width: 160px; text-align: center; }
    .flaga-img { width: 90px; height: auto; border-radius: 8px; box-shadow: 0 0 10px rgba(255,255,255,0.1); }
    .data-spotkania { font-size: 16px; color: #888888; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# s: W(wygrana), L(przegrana), D(remis) | miejsce: dom / wyjazd
mecze = [
    {"o": "Szwecja", "f": "https://flagcdn.com/w160/se.png", "w": "2 : 3", "d": "31.03.2026", "s": "L", "miejsce": "dom"},
    {"o": "Albania", "f": "https://flagcdn.com/w160/al.png", "w": "2 : 1", "d": "26.03.2026", "s": "W", "miejsce": "dom"},
    {"o": "Malta", "f": "https://flagcdn.com/w160/mt.png", "w": "3 : 2", "d": "17.11.2025", "s": "W", "miejsce": "wyjazd"},
    {"o": "Holandia", "f": "https://flagcdn.com/w160/nl.png", "w": "1 : 1", "d": "14.11.2025", "s": "D", "miejsce": "dom"},
    {"o": "Litwa", "f": "https://flagcdn.com/w160/lt.png", "w": "2 : 0", "d": "12.10.2025", "s": "W", "miejsce": "wyjazd"}
]

st.markdown("<h1 style='text-align: center; font-size: 55px; margin-bottom: 50px;'>POLSKA - OSTATNIE MECZE</h1>", unsafe_allow_html=True)

flaga_pl = "https://flagcdn.com/w160/pl.png"

for m in mecze:
    # Ustalanie koloru wyniku
    kolor = "#FFFFFF"
    if m['s'] == "W": kolor = "#00FF00"
    elif m['s'] == "L": kolor = "#FF0000"

    # Logika gospodarza: jeśli mecz był na wyjeździe, Polska leci na prawo
    if m['miejsce'] == "dom":
        lewa_n, lewa_f = "POLSKA", flaga_pl
        prawa_n, prawa_f = m['o'].upper(), m['f']
        wynik_str = m['w']
    else:
        lewa_n, lewa_f = m['o'].upper(), m['f']
        prawa_n, prawa_f = "POLSKA", flaga_pl
        # Odwracamy wynik, żeby pasował do stron (Polska zawsze druga na wyjeździe)
        czesci = m['w'].split(" : ")
        wynik_str = f"{czesci[1]} : {czesci[0]}"

    st.markdown(f'''
        <div class="wynik-row">
            <div class="data-spotkania">{m['d']} | {"STADION NARODOWY" if m['miejsce'] == 'dom' else 'WYJAZD'}</div>
            <div class="mecz-kontener">
                <img src="{lewa_f}" class="flaga-img">
                <span class="druzyna">{lewa_n}</span>
                <span class="wynik-liczba" style="color: {kolor};">{wynik_str}</span>
                <span class="druzyna">{prawa_n}</span>
                <img src="{prawa_f}" class="flaga-img">
            </div>
        </div>
    ''', unsafe_allow_html=True)
    
