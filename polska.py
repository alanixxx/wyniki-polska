import streamlit as st

st.set_page_config(page_title="Wyniki Polska", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    .wynik-row { display: flex; justify-content: center; align-items: center; margin: 40px 0; }
    .druzyna { font-size: 50px; font-weight: bold; padding: 0 30px; color: white; min-width: 300px; text-align: center; }
    .wynik-liczba { font-size: 80px; color: #FF0000; font-weight: 900; min-width: 200px; text-align: center; }
    .flaga { font-size: 70px; }
    </style>
    """, unsafe_allow_html=True)

mecze = [
    {"o": "Czechy", "f": "🇨🇿", "w": "2 : 1"},
    {"o": "Niemcy", "f": "🇩🇪", "w": "1 : 0"},
    {"o": "Francja", "f": "🇫🇷", "w": "3 : 3"}
]

st.markdown("<h1 style='text-align: center; font-size: 60px;'>POLSKA - WYNIKI</h1>", unsafe_allow_html=True)

for m in mecze:
    st.markdown(f'''
        <div class="wynik-row">
            <span class="flaga">🇵🇱</span>
            <span class="druzyna">POLSKA</span>
            <span class="wynik-liczba">{m['w']}</span>
            <span class="druzyna">{m['o'].upper()}</span>
            <span class="flaga">{m['f']}</span>
        </div>
    ''', unsafe_allow_html=True)
