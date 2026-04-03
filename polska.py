import streamlit as st

st.set_page_config(page_title="Wyniki Polska", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    .wynik-row { display: flex; justify-content: center; align-items: center; margin: 40px 0; }
    .druzyna { font-size: 50px; font-weight: bold; padding: 0 30px; color: white; min-width: 300px; text-align: center; }
    .wynik-liczba { font-size: 80px; color: #FF0000; font-weight: 900; min-width: 200px; text-align: center; }
    .flaga-img { width: 100px; height: auto; border-radius: 10px; box-shadow: 0 0 15px rgba(255,255,255,0.2); }
    </style>
    """, unsafe_allow_html=True)

# Linki do prawdziwych zdjęć flag (PNG)
mecze = [
    {"o": "Czechy", "f": "https://flagcdn.com/w160/cz.png", "w": "2 : 1"},
    {"o": "Niemcy", "f": "https://flagcdn.com/w160/de.png", "w": "1 : 0"},
    {"o": "Francja", "f": "https://flagcdn.com/w160/fr.png", "w": "3 : 3"}
]

st.markdown("<h1 style='text-align: center; font-size: 60px;'>POLSKA - WYNIKI</h1>", unsafe_allow_html=True)

for m in mecze:
    st.markdown(f'''
        <div class="wynik-row">
            <img src="https://flagcdn.com/w160/pl.png" class="flaga-img">
            <span class="druzyna">POLSKA</span>
            <span class="wynik-liczba">{m['w']}</span>
            <span class="druzyna">{m['o'].upper()}</span>
            <img src="{m['f']}" class="flaga-img">
        </div>
    ''', unsafe_allow_html=True)
