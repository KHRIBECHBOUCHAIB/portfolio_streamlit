import streamlit as st
from PIL import Image

# Include CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Pages du portfolio
def accueil():
    local_css("style.css")  # Apply CSS
    # Définir le chemin relatif ou absolu vers l'image
    logo_path = 'images/image1.jpg'  
    st.image(logo_path, width=200)
    st.title("Accueil")
    st.markdown("Bienvenue sur mon portfolio professionnel ! Un voyageur du monde des données. De la scène de crime à la scène de code, mes 15 ans en sciences forensiques m'ont doté d'une rigueur et d'une perspective unique sur la data science. Transitionnant vers l'informatique, j'ai embrassé Python, pyspark, java, sql et la visualisation des données avec un enthousiasme contagieux. J'ai non seulement modelé l'avenir avec le machine learning mais j'ai aussi peint des histoires de données avec Power BI et Azure Machine Learning. Mon coeur bat au rythme de l'innovation en santé et psychologie, cherchant à améliorer l'UX des produits qui touchent des vies. En dehors du numérique, je trouve mon équilibre dans les embruns du kitesurf.")

def projets():
    local_css("style.css")  # Apply CSS
    st.title("Projets")
    st.markdown("""
    Voici quelques projets sur lesquels j'ai travaillé :
    
    - **Développement UX pour produits psychologiques** : Création d'interfaces utilisateur centrées sur l'expérience dans le domaine de la santé mentale.
    - **Analyse et visualisation de données** : Utilisation de Python et ses bibliothèques pour traiter et visualiser des données complexes.
    - **Application web avec Symfony** : Développement complet d'un site web pour une régie publicitaire.
    """)

def cv():
    local_css("style.css")  # Apply CSS
    st.title("Mon CV")
    st.markdown("Vous pouvez télécharger mon CV pour plus de détails sur mon parcours professionnel et académique.")
    with open("cv_khribech_bouchaib.pdf", "rb") as file:  # Adjust the path to your CV
        btn = st.download_button(
            label="Télécharger le CV",
            data=file,
            file_name="cv_khribech_bouchaib.pdf",
            mime="application/octet-stream"
        )

def contact():
    local_css("style.css")  # Apply CSS
    st.title("Contact")
    st.markdown("""
    Vous pouvez me contacter via :
    
    - Email : khribech.chouaib@gmail.com
    - LinkedIn : [khbouchaib](https://www.linkedin.com/in/khbouchaib/)
    """)

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à", ["Accueil", "Projets", "CV", "Contact"])

if page == "Accueil":
    accueil()
elif page == "Projets":
    projets()
elif page == "CV":
    cv()
elif page == "Contact":
    contact()
