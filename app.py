import streamlit as st
from PIL import Image

# Include CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def accueil():
    local_css("style.css")  # Appliquer le CSS

    st.title("Bienvenue sur Mon Portfolio Professionnel")

    # Introduction
    st.markdown("""
    ### 🌟 À propos de Moi
    Bienvenue ! Je suis **Bouchaib KHRIBECH**, un voyageur du monde des données. Mes 15 ans d'expérience en sciences forensiques m'ont équipé d'une rigueur et d'une perspective unique sur la data science.
    
    ### 💡 Ma Transition vers l'Informatique
    Transitionnant vers l'informatique, j'ai embrassé des technologies telles que **Python**, **PySpark**, **Java**, **SQL**, et la visualisation des données avec un enthousiasme contagieux. Mon parcours m'a permis de modeler l'avenir avec le **Machine Learning** et de peindre des histoires captivantes avec **Power BI** et **Azure Machine Learning**.
    
    ### 🚀 Passion pour l'Innovation
    Mon cœur bat au rythme de l'innovation, particulièrement dans les domaines de la santé et de la psychologie, où je cherche constamment à améliorer l'expérience utilisateur des produits qui impactent nos vies.
    
    ### 🏄‍♂️ Vie en dehors du Numérique
    En dehors du numérique, je trouve mon équilibre dans l'adrénaline et la liberté offertes par le **kitesurf**.
    """)

    st.markdown("""
    ### 📫 Contactez-Moi
    - Email : khribech.chouaib@gmail.com
    """, unsafe_allow_html=True)
     # Afficher le logo
    logo_path = 'images/image1.jpg'  
    st.image(logo_path, width=100)

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
    local_css("style.css")  # Appliquer le CSS
    st.title("Mon CV")

    # Introduction ou résumé
    st.markdown("""
    ### À propos de moi
    Je suis Bouchaib KHRIBECH, un spécialist en data science et analsye. Mon parcours m'a permis de développer une approche rigoureuse et innovante dans le domaine de l'informatique, avec une spécialisation en machine learning, analyse de données et développement logiciel.
    
    Découvrez plus en détail mon parcours professionnel et académique en téléchargeant mon CV.
    """)
    
    # Bouton de téléchargement du CV
    with open("cv_khribech_bouchaib.pdf", "rb") as file:
        st.download_button(
            label="📥 Télécharger le CV",
            data=file,
            file_name="cv_khribech_bouchaib.pdf",
            mime="application/pdf",
        )
    
    # Note : Streamlit ne supporte pas directement l'attribut 'style' dans st.download_button().
    # Pour styliser le bouton de téléchargement, il faudrait le faire via le fichier CSS global et non directement ici.


def contact():
    local_css("style.css")  # Appliquer le CSS

    st.markdown("""
    ### 📬 Me Contacter

    N'hésitez pas à me contacter pour toute question, opportunité, ou simplement pour échanger. Voici comment vous pouvez me joindre :
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <a href="mailto:khribech.chouaib@gmail.com" target="_blank">
            <button style='margin: 10px; padding: 10px; background-color: #4CAF50; color: white; border-radius: 5px; border: none; cursor: pointer;'>📧 Email</button>
        </a>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <a href="https://www.linkedin.com/in/khbouchaib/" target="_blank">
            <button style='margin: 10px; padding: 10px; background-color: #0e76a8; color: white; border-radius: 5px; border: none; cursor: pointer;'>🔗 LinkedIn</button>
        </a>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <a href="https://github.com/KHRIBECHBOUCHAIB" target="_blank">
            <button style='margin: 10px; padding: 10px; background-color: #333; color: white; border-radius: 5px; border: none; cursor: pointer;'>🐱 GitHub</button>
        </a>
        """, unsafe_allow_html=True)

# Navigation
# Appliquer le CSS globalement
local_css("style.css")

# Titre de la sidebar
st.sidebar.title("🧭 Navigation")

# Options de navigation avec emojis pour plus de visibilité
options_nav = {
    "Accueil": "🏠 Accueil",
    "Projets": "💼 Projets",
    "CV": "📄 CV",
    "Contact": "📞 Contact"
}

# Création des options de navigation dans la sidebar
page = st.sidebar.radio("Aller à", list(options_nav.keys()), format_func=lambda x: options_nav[x])

# Correspondance des pages aux fonctions
if page == "Accueil":
    accueil()
elif page == "Projets":
    projets()
elif page == "CV":
    cv()
elif page == "Contact":
    contact()