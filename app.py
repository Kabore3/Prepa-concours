
import streamlit as st

st.set_page_config(
    page_title="PrépaConcours IA",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 PrépaConcours IA")
st.subheader("Préparation aux concours directs du Burkina Faso")

st.markdown("""
Bienvenue dans ton espace de préparation.

Cette plateforme permettra de :
- Réviser la culture générale
- Améliorer son français
- Étudier l'histoire et la géographie
- S'entraîner en mathématiques et sciences
- Préparer les concours de la Police, des Douanes
  et des Eaux et Forêts
""")

st.divider()

matiere = st.selectbox(
    "Choisis une matière",
    [
        "Culture générale",
        "Français",
        "Histoire",
        "Géographie",
        "Mathématiques",
        "Sciences",
        "Institutions"
    ]
)

niveau = st.selectbox(
    "Niveau de difficulté",
    ["Facile", "Intermédiaire", "Difficile"]
)

if st.button("Commencer les révisions"):
    st.info(f"Matière : {matiere} | Niveau : {niveau}")
    st.write("La banque de questions sera bientôt disponible.")
