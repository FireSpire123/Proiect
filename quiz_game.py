import streamlit as st
from PIL import Image
import os

# Lista cu întrebări, variante și imagini pentru răspunsuri
intrebari = [
    {
        "intrebare": "Ce faci dimineața când te ridici din pat?",
        "imagine": "imagine1.png",
        "variante": [
            {"text": "Mă spăl pe față și mă îmbrac", "corect": True, "imagine": "raspuns1.png"},
            {"text": "Mă culc din nou", "corect": False, "imagine": "raspuns2.png"},
            {"text": "Încep să mă joc cu jucăriile", "corect": False, "imagine": "raspuns3.png"}
        ]
    },
    {
        "intrebare": "Ce faci înainte de a mânca micul dejun?",
        "imagine": "imagine2.png",
        "variante": [
            {"text": "Îmi spăl mâinile", "corect": True, "imagine": "raspuns4.png"},
            {"text": "Ies afară", "corect": False, "imagine": "raspuns5.png"},
            {"text": "Mă pun în pat", "corect": False, "imagine": "raspuns6.png"}
        ]
    },
    {
        "intrebare": "Ce ai nevoie când ieși afară?",
        "imagine": "imagine3.png",
        "variante": [
            {"text": "Ochelari de soare", "corect": False, "imagine": "raspuns8.png"},
            {"text": "Umbrelă", "corect": True, "imagine": "raspuns7.png"},
            {"text": "Șlapi", "corect": False, "imagine": "raspuns9.png"}
        ]
    },
    {
        "intrebare": "Ce faci când te simți obosit după o zi lungă?",
        "imagine": "imagine4.png",
        "variante": [
            {"text": "Să te joci toată noaptea", "corect": False, "imagine": "raspuns10.png"},
            {"text": "Să bei foarte mult suc", "corect": False, "imagine": "raspuns11.png"},
            {"text": "Să îți iei puțin timp să te odihnești sau să te culci", "corect": True, "imagine": "raspuns12.png"}
        ]
    },
    {
        "intrebare": "Când trebuie să treci?",
        "imagine": "imagine5.png",
        "variante": [
            {"text": "Aici", "corect": True, "imagine": "raspuns13.png"},
            {"text": "Aici", "corect": False, "imagine": "raspuns14.png"},
        ]
    },
    {
        "intrebare": "Ce faci după ce ajungi acasă de la școală?",
        "imagine": "imagine6.png",
        "variante": [
            {"text": "Îmi fac temele", "corect": True, "imagine": "raspuns16.png"},
            {"text": "Alerg prin casă", "corect": False, "imagine": "raspuns17.png"},
            {"text": "Mă întind pe jos și mă culc", "corect": False, "imagine": "raspuns18.png"}
        ]
    },
    {
        "intrebare": "Ce faci în această situație?",
        "imagine": "imagine7.png",
        "variante": [
            {"text": "Mă pun să dorm", "corect": False, "imagine": "raspuns19.png"},
            {"text": "Fac curat", "corect": True, "imagine": "raspuns20.png"},
            {"text": "Mă apuc să mă joc", "corect": False, "imagine": "raspuns21.png"}
        ]
    },
    {
        "intrebare": "Ce faci după ce mănânci?",
        "imagine": "imagine8.png",
        "variante": [
            {"text": "Încep să arunc ce a rămas în farfurie", "corect": False, "imagine": "raspuns22.png"},
            {"text": "Pun farfuria in chiuveta și o spăl", "corect": True, "imagine": "raspuns23.png"},
            {"text": "Las farfuria pe masa", "corect": False, "imagine": "raspuns24.png"}
        ]
    },
    {
        "intrebare": "Ce faci înainte de culcare?",
        "imagine": "imagine9.png",
        "variante": [
            {"text": "Mă spăl pe dinți și mă pun în pijamale", "corect": True, "imagine": "raspuns25.png"},
            {"text": "Mănânc dulciuri", "corect": False, "imagine": "raspuns26.png"},
            {"text": "Mă uit la filme", "corect": False, "imagine": "raspuns27.png"}
        ]
    },
    {
        "intrebare": "Ce faci când termini de jucat?",
        "imagine": "imagine10.png",
        "variante": [
            {"text": "Îmi pun jucăriile la loc", "corect": True, "imagine": "raspuns28.png"},
            {"text": "Le las împrăștiate", "corect": False, "imagine": "raspuns29.png"},
            {"text": "Le arunc prin cameră", "corect": False, "imagine": "raspuns30.png"}
        ]
    }
]

index_intrebare = 0

# Funcție pentru a verifica răspunsul
def verifica_raspuns(raspuns_corect, raspuns_dat):
    return raspuns_corect == raspuns_dat

# Pagina principală
st.title("🎮 Joc Interactiv")

# Indexul întrebării curente
if 'index_intrebare' not in st.session_state:
    st.session_state.index_intrebare = 0

# Afișăm întrebarea curentă
def afiseaza_intrebare(index):
    intrebarea = intrebari[index]
    st.image(intrebarea["imagine"], use_column_width=True)
    st.write(intrebarea["intrebare"])

    for raspuns in intrebarea["variante"]:
        if st.button(raspuns["text"]):
            feedback = "Foarte bine!" if raspuns["corect"] else "Mai încearcă!"
            st.success(feedback) if raspuns["corect"] else st.error(feedback)
            st.session_state.index_intrebare += 1  # Trecem la următoarea întrebare

# Verificăm dacă sunt întrebări disponibile
if st.session_state.index_intrebare < len(intrebari):
    afiseaza_intrebare(st.session_state.index_intrebare)
else:
    st.write("Felicitări! Ai terminat toate întrebările.")
    if st.button("Reîncepe jocul"):
        st.session_state.index_intrebare = 0  # Resetăm jocul
