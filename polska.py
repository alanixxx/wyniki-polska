import streamlit as st

st.set_page_config(page_title="Ostatnie mecze reprezentacji Polski", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    .wynik-row { display: flex; flex-direction: column; align-items: center; margin: 30px 0; border-bottom: 1px solid #222; padding-bottom: 20px; }
    .mecz-kontener { display: flex; justify-content: center; align-items: center; width: 100%; }
    .druzyna { font-size: 35px; font-weight: bold; color: white; width: 320px; text-align: center; }
    .wynik-liczba { font-size: 55px; font-weight: 900; min-width: 250px; text-align: center; line-height: 1.1; }
    .karne-info { font-size: 20px; color: #aaaaaa; vertical-align: middle; margin: 0 10px; font-weight: normal; }
    .flaga-img { width: 85px; height: auto; border-radius: 8px; box-shadow: 0 0 12px rgba(255,255,255,0.15); }
    .info-linia { font-size: 14px; color: #777777; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 1px; font-weight: bold; }
    .turniej-extra { color: #FFD700; font-weight: 900; }
    </style>
    """, unsafe_allow_html=True)

def formatuj_wynik(wynik_str, kolor):
    if "(" in wynik_str:
        c = wynik_str.split(" ")
        return f'<span class="karne-info">{c[0]}</span><span style="color: {kolor};">{c[1]} {c[2]} {c[3]}</span><span class="karne-info">{c[4]}</span>'
    return f'<span style="color: {kolor};">{wynik_str}</span>'

# WSZYSTKIE MECZE ZE WSZYSTKICH PRZESŁANYCH SCREENÓW
mecze = [
    # --- 2026 ---
    {"o": "Szwecja", "f": "https://flagcdn.com/w160/se.png", "w": "3 : 2", "d": "31.03.2026", "s": "L", "miejsce": "wyjazd", "t": "MŚ - Kwalifikacje (Baraże)", "wazne": True},
    {"o": "Albania", "f": "https://flagcdn.com/w160/al.png", "w": "2 : 1", "d": "26.03.2026", "s": "W", "miejsce": "dom", "t": "MŚ - Kwalifikacje (Baraże)", "wazne": True},
    
    # --- 2025 ---
    {"o": "Malta", "f": "https://flagcdn.com/w160/mt.png", "w": "2 : 3", "d": "17.11.2025", "s": "W", "miejsce": "wyjazd", "t": "MŚ - Kwalifikacje", "wazne": False},
    {"o": "Holandia", "f": "https://flagcdn.com/w160/nl.png", "w": "1 : 1", "d": "14.11.2025", "s": "D", "miejsce": "dom", "t": "MŚ - Kwalifikacje", "wazne": False},
    {"o": "Litwa", "f": "https://flagcdn.com/w160/lt.png", "w": "0 : 2", "d": "12.10.2025", "s": "W", "miejsce": "wyjazd", "t": "MŚ - Kwalifikacje", "wazne": False},
    {"o": "Nowa Zelandia", "f": "https://flagcdn.com/w160/nz.png", "w": "1 : 0", "d": "09.10.2025", "s": "W", "miejsce": "dom", "t": "Mecz towarzyski", "wazne": False},
    {"o": "Finlandia", "f": "https://flagcdn.com/w160/fi.png", "w": "3 : 1", "d": "07.09.2025", "s": "W", "miejsce": "dom", "t": "MŚ - Kwalifikacje", "wazne": False},
    {"o": "Holandia", "f": "https://flagcdn.com/w160/nl.png", "w": "1 : 1", "d": "04.09.2025", "s": "D", "miejsce": "wyjazd", "t": "MŚ - Kwalifikacje", "wazne": False},
    {"o": "Finlandia", "f": "https://flagcdn.com/w160/fi.png", "w": "2 : 1", "d": "10.06.2025", "s": "L", "miejsce": "wyjazd", "t": "MŚ - Kwalifikacje", "wazne": False},
    {"o": "Mołdawia", "f": "https://flagcdn.com/w160/md.png", "w": "2 : 0", "d": "06.06.2025", "s": "W", "miejsce": "dom", "t": "Mecz towarzyski", "wazne": False},
    {"o": "Malta", "f": "https://flagcdn.com/w160/mt.png", "w": "2 : 0", "d": "24.03.2025", "s": "W", "miejsce": "dom", "t": "MŚ - Kwalifikacje", "wazne": False},
    {"o": "Litwa", "f": "https://flagcdn.com/w160/lt.png", "w": "1 : 0", "d": "21.03.2025", "s": "W", "miejsce": "dom", "t": "MŚ - Kwalifikacje", "wazne": False},

    # --- 2024 ---
    {"o": "Szkocja", "f": "https://flagcdn.com/w160/gb-sct.png", "w": "1 : 2", "d": "18.11.2024", "s": "L", "miejsce": "dom", "t": "Liga Narodów", "wazne": False},
    {"o": "Portugalia", "f": "https://flagcdn.com/w160/pt.png", "w": "5 : 1", "d": "15.11.2024", "s": "L", "miejsce": "wyjazd", "t": "Liga Narodów", "wazne": False},
    {"o": "Chorwacja", "f": "https://flagcdn.com/w160/hr.png", "w": "3 : 3", "d": "15.10.2024", "s": "D", "miejsce": "dom", "t": "Liga Narodów", "wazne": False},
    {"o": "Portugalia", "f": "https://flagcdn.com/w160/pt.png", "w": "1 : 3", "d": "12.10.2024", "s": "L", "miejsce": "dom", "t": "Liga Narodów", "wazne": False},
    {"o": "Chorwacja", "f": "https://flagcdn.com/w160/hr.png", "w": "1 : 0", "d": "08.09.2024", "s": "L", "miejsce": "wyjazd", "t": "Liga Narodów", "wazne": False},
    {"o": "Szkocja", "f": "https://flagcdn.com/w160/gb-sct.png", "w": "2 : 3", "d": "05.09.2024", "s": "W", "miejsce": "wyjazd", "t": "Liga Narodów", "wazne": False},
    {"o": "Francja", "f": "https://flagcdn.com/w160/fr.png", "w": "1 : 1", "d": "25.06.2024", "s": "D", "miejsce": "wyjazd", "t": "EURO 2024", "wazne": True},
    {"o": "Austria", "f": "https://flagcdn.com/w160/at.png", "w": "1 : 3", "d": "21.06.2024", "s": "L", "miejsce": "dom", "t": "EURO 2024", "wazne": True},
    {"o": "Holandia", "f": "https://flagcdn.com/w160/nl.png", "w": "1 : 2", "d": "16.06.2024", "s": "L", "miejsce": "dom", "t": "EURO 2024", "wazne": True},
    {"o": "Turcja", "f": "https://flagcdn.com/w160/tr.png", "w": "2 : 1", "d": "10.06.2024", "s": "W", "miejsce": "dom", "t": "Mecz towarzyski", "wazne": False},
    {"o": "Ukraina", "f": "https://flagcdn.com/w160/ua.png", "w": "3 : 1", "d": "07.06.2024", "s": "W", "miejsce": "dom", "t": "Mecz towarzyski", "wazne": False},
    {"o": "Walia", "f": "https://flagcdn.com/w160/gb-wls.png", "w": "(4) 0 : 0 (5)", "d": "26.03.2024", "s": "W", "miejsce": "wyjazd", "t": "EURO - Kwalifikacje (Baraże - Awans)", "wazne": True},
    {"o": "Estonia", "f": "https://flagcdn.com/w160/ee.png", "w": "5 : 1", "d": "21.03.2024", "s": "W", "miejsce": "dom", "t": "EURO - Kwalifikacje (Baraże)", "wazne": True},

    # --- 2023 ---
    {"o": "Łotwa", "f": "https://flagcdn.com/w160/lv.png", "w": "2 : 0", "d": "21.11.2023", "s": "W", "miejsce": "dom", "t": "Mecz towarzyski", "wazne": False},
    {"o": "Czechy", "f": "https://flagcdn.com/w160/cz.png", "w": "1 : 1", "d": "17.11.2023", "s": "D", "miejsce": "dom", "t": "EURO - Kwalifikacje", "wazne": False},
    {"o": "Mołdawia", "f": "https://flagcdn.com/w160/md.png", "w": "1 : 1", "d": "15.10.2023", "s": "D", "miejsce": "dom", "t": "EURO - Kwalifikacje", "wazne": False},
    {"o": "Wyspy Owcze", "f": "https://flagcdn.com/w160/fo.png", "w": "0 : 2", "d": "12.10.2023", "s": "W", "miejsce": "wyjazd", "t": "EURO - Kwalifikacje", "wazne": False},
    {"o": "Albania", "f": "https://flagcdn.com/w160/al.png", "w": "2 : 0", "d": "10.09.2023", "s": "L", "miejsce": "wyjazd", "t": "EURO - Kwalifikacje", "wazne": False},
    {"o": "Wyspy Owcze", "f": "https://flagcdn.com/w160/fo.png", "w": "2 : 0", "d": "07.09.2023", "s": "W", "miejsce": "dom", "t": "EURO - Kwalifikacje", "wazne": False},
    {"o": "Mołdawia", "f": "https://flagcdn.com/w160/md.png", "w": "3 : 2", "d": "20.06.2023", "s": "L", "miejsce": "wyjazd", "t": "EURO - Kwalifikacje", "wazne": False},
    {"o": "Niemcy", "f": "https://flagcdn.com/w160/de.png", "w": "1 : 0", "d": "16.06.2023", "s": "W", "miejsce": "dom", "t": "Mecz towarzyski", "wazne": False},
    {"o": "Albania", "f": "https://flagcdn.com/w160/al.png", "w": "1 : 0", "d": "27.03.2023", "s": "W", "miejsce": "dom", "t": "EURO - Kwalifikacje", "wazne": False},
    {"o": "Czechy", "f": "https://flagcdn.com/w160/cz.png", "w": "3 : 1", "d": "24.03.2023", "s": "L", "miejsce": "wyjazd", "t": "EURO - Kwalifikacje", "wazne": False},

    # --- 2022 ---
    {"o": "Francja", "f": "https://flagcdn.com/w160/fr.png", "w": "3 : 1", "d": "04.12.2022", "s": "L", "miejsce": "wyjazd", "t": "MŚ - 1/8 Finału", "wazne": True},
    {"o": "Argentyna", "f": "https://flagcdn.com/w160/ar.png", "w": "0 : 2", "d": "30.11.2022", "s": "L", "miejsce": "dom", "t": "Mistrzostwa Świata", "wazne": True},
    {"o": "Arabia Saudyjska", "f": "https://flagcdn.com/w160/sa.png", "w": "2 : 0", "d": "26.11.2022", "s": "W", "miejsce": "dom", "t": "Mistrzostwa Świata", "wazne": True},
    {"o": "Meksyk", "f": "https://flagcdn.com/w160/mx.png", "w": "0 : 0", "d": "22.11.2022", "s": "D", "miejsce": "wyjazd", "t": "Mistrzostwa Świata", "wazne": True},
    {"o": "Chile", "f": "https://flagcdn.com/w160/cl.png", "w": "1 : 0", "d": "16.11.2022", "s": "W", "miejsce": "dom", "t": "Mecz towarzyski", "wazne": False},
    {"o": "Walia", "f": "https://flagcdn.com/w160/gb-wls.png", "w": "0 : 1", "d": "25.09.2022", "s": "W", "miejsce": "wyjazd", "t": "Liga Narodów", "wazne": False},
    {"o": "Holandia", "f": "https://flagcdn.com/w160/nl.png", "w": "0 : 2", "d": "22.09.2022", "s": "L", "miejsce": "dom", "t": "Liga Narodów", "wazne": False},
    {"o": "Belgia", "f": "https://flagcdn.com/w160/be.png", "w": "0 : 1", "d": "14.06.2022", "s": "L", "miejsce": "dom", "t": "Liga Narodów", "wazne": False},
    {"o": "Holandia", "f": "https://flagcdn.com/w160/nl.png", "w": "2 : 2", "d": "11.06.2022", "s": "D", "miejsce": "wyjazd", "t": "Liga Narodów", "wazne": False},
    {"o": "Belgia", "f": "https://flagcdn.com/w160/be.png", "w": "6 : 1", "d": "08.06.2022", "s": "L", "miejsce": "wyjazd", "t": "Liga Narodów", "wazne": False},
    {"o": "Walia", "f": "https://flagcdn.com/w160/gb-wls.png", "w": "2 : 1", "d": "01.06.2022", "s": "W", "miejsce": "dom", "t": "Liga Narodów", "wazne": False},
    {"o": "Szwecja", "f": "https://flagcdn.com/w160/se.png", "w": "2 : 0", "d": "29.03.2022", "s": "W", "miejsce": "dom", "t": "MŚ - Kwalifikacje (Baraże - Awans)", "wazne": True},
    {"o": "Szkocja", "f": "https://flagcdn.com/w160/gb-sct.png", "w": "1 : 1", "d": "24.03.2022", "s": "D", "miejsce": "wyjazd", "t": "Mecz towarzyski", "wazne": False},

    # --- 2021 ---
    {"o": "Węgry", "f": "https://flagcdn.com/w160/hu.png", "w": "1 : 2", "d": "15.11.2021", "s": "L", "miejsce": "dom", "t": "MŚ - Kwalifikacje", "wazne": False},
    {"o": "Andora", "f": "https://flagcdn.com/w160/ad.png", "w": "1 : 4", "d": "12.11.2021", "s": "W", "miejsce": "wyjazd", "t": "MŚ - Kwalifikacje", "wazne": False},
    {"o": "Albania", "f": "https://flagcdn.com/w160/al.png", "w": "0 : 1", "d": "12.10.2021", "s": "W", "miejsce": "wyjazd", "t": "MŚ - Kwalifikacje", "wazne": False}
]

st.markdown("<h1 style='text-align: center; font-size: 45px; margin-bottom: 40px;'>OSTATNIE MECZE REPREZENTACJI POLSKI</h1>", unsafe_allow_html=True)

flaga_pl = "https://flagcdn.com/w160/pl.png"

for m in mecze:
    kolor_wyniku = "#FFFFFF"
    if m['s'] == "W": kolor_wyniku = "#00FF00"
    elif m['s'] == "L": kolor_wyniku = "#FF0000"

    klasa_turnieju = 'class="turniej-extra"' if m['wazne'] else ""

    if m['miejsce'] == "dom":
        l_n, l_f = "POLSKA", flaga_pl
        p_n, p_f = m['o'].upper(), m['f']
        w_wyswietl = formatuj_wynik(m['w'], kolor_wyniku)
    else:
        l_n, l_f = m['o'].upper(), m['f']
        p_n, p_f = "POLSKA", flaga_pl
        if "(" in m['w']:
            c = m['w'].split(" ")
            w_odwrocony = f"{c[0]} {c[1]} {c[2]} {c[3]} {c[4]}"
            w_wyswietl = formatuj_wynik(w_odwrocony, kolor_wyniku)
        else:
            res = m['w'].split(" : ")
            w_wyswietl = formatuj_wynik(f"{res[0]} : {res[1]}", kolor_wyniku)

    st.markdown(f'''
        <div class="wynik-row">
            <div class="info-linia">
                {m['d']} | <span {klasa_turnieju}>{m['t']}</span> | {"DOM" if m['miejsce'] == 'dom' else 'WYJAZD'}
            </div>
            <div class="mecz-kontener">
                <img src="{l_f}" class="flaga-img">
                <span class="druzyna">{l_n}</span>
                <span class="wynik-liczba">{w_wyswietl}</span>
                <span class="druzyna">{p_n}</span>
                <img src="{p_f}" class="flaga-img">
            </div>
        </div>
    ''', unsafe_allow_html=True)
