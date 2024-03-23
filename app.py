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
    local_css("style.css")  # Appliquer le CSS
    st.title("Projets")
    st.markdown("""
    ### Voici quelques-uns des projets significatifs sur lesquels j'ai travaillé, démontrant mes compétences en développement logiciel, et analyse de données :
    """)

    with st.expander("Modèle de Prédiction de Performance des Étudiants en Python (Fév 2024 - Mar 2024)"):
        st.markdown("""
        **Association :** Institute of Digital Sciences, Management and Cognition (IDMC).  
        **Description :** Développement d'une application Python pour prédire les performances académiques des étudiants universitaires à travers l'analyse de régression linéaire, en se basant sur leur engagement avec la plateforme d'apprentissage en ligne.  
        **Compétences :**
        - PyCharm 🐍
        - Python 🐍
        - Régression Linéaire 📈
        - EDA 🔍
        - Analyse des Données 📊
        - Machine Learning 🤖
        """)

    with st.expander("Simulation du Site Web de l'Euro 2024 avec React (Fév 2024)"):
        st.markdown("""
        **Association :** IDMC.  
        **Description :** Création d'un site web dynamique pour l'Euro 2024 utilisant React, avec des fonctionnalités telles que les mises à jour en temps réel, statistiques d'équipe, et calendriers de match.  
        **Compétences :**
        - React.js ⚛️
        - Conception Web Réactive 📱
        - Single Page Application 🖥️
        - Intégration API 📡
        """)

    with st.expander("Tableau de Bord de Rentabilité des Techniciens de Maintenance avec Power BI (Mar 2023 - Déc 2023)"):
        st.markdown("""
        **Association :** DBCALL | Réseau DEF.  
        **Description :** Développement d'un tableau de bord Power BI pour analyser la rentabilité des techniciens de maintenance.  
        **Compétences :**
        - Analyse des Données 📊
        - Power BI 🔌
        """)

    with st.expander("Système d'Approbation de Prêts Alimenté par ML (Sep 2023 - Oct 2023)"):
        st.markdown("""
        **Association :** AFPA.  
        **Description :** Conception d'un notebook ML pour automatiser les approbations de prêts à l'aide de classificateurs tels que Random Forest et SVM.  
        **Compétences :**
        - pandas 🐼
        - NumPy 🔢
        - Scikit-Learn 🤖
        """)

    with st.expander("Système de Gestion de Prospects avec Support Multi-Bases de Données en JAVA ET JAVA EE (Avr 2023 - Mai 2023)"):
        st.markdown("""
        **Association :** AFPA.  
        **Description :** Ingénierie d'un système de gestion de prospects clients en Java EE, utilisant des motifs de conception pour une intégration flexible de bases de données.  
        **Compétences :**
        - MongoDB 🍃
        - Java EE ☕
        - SQL 🗃️
        - Abstract Factory 🏭
        - UML 📐
        """)

    with st.expander("Site Web de Cinéma Local avec Vue.js et Intégration d'API de Films (Mar 2023 - Avr 2023)"):
        st.markdown("""
        **Association :** AFPA.  
        **Description :** Développement d'un site web pour un cinéma local avec Vue.js, intégrant des données de films en temps réel via des API.  
        **Compétences :**
        - Vue.js 🖼️
        - HTML5 🌐
        - CSS 🎨
        - JavaScript 📜
        - Intégration API 📡
        """)

    with st.expander("Système de Base de Données de Gestion de Musée avec SQL (Jan 2023 - Fév 2023)"):
        st.markdown("""
Association : AFPA.
Description : Direction du développement d'un système de base de données complet pour la gestion de musée, utilisant SQL pour un traitement robuste des données. Ce projet a impliqué le déploiement de la base de données dans un conteneur Docker pour faciliter la configuration et la scalabilité, ainsi que la conception et l'implémentation d'un schéma relationnel pour stocker et gérer efficacement les collections, expositions et informations des visiteurs du musée.
Compétences :
- SQL 🗃️
- Docker 🐳
- Conception de Base de Données 📐
- MCD (Modèle Conceptuel de Données) 📊
- MLD (Modèle Logique de Données) 🔗
- MPD (Modèle Physique de Données) 💾
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
