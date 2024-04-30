import streamlit as st
from PIL import Image
import webbrowser


# Include CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Header function
def header():
    st.markdown('<p class="header">Bienvenue sur mon portfolio professionnel</p>', unsafe_allow_html=True)

# Footer function
def footer():
    st.markdown("""
    <footer class="footer">
        <div class="content has-text-centered">
            <p>
                by <a href="https://www.linkedin.com/in/khbouchaib/" target="_blank">Khribech Bouchaib</a>. Tous droits réservés © 2024.
            </p>
        </div>
    </footer>
    """, unsafe_allow_html=True)

# Home page
def accueil():
    local_css("style.css")  # Appliquer le CSS

    # Add a header
    header()

    # Afficher le logo
    logo_path = 'images/image1.jpg'

    col1, col2, col3 = st.columns([6, 9, 2])
    with col2:
        st.image(logo_path, width=200)

    # Introduction
    st.markdown("""
    ### 🌟 À propos de Moi
    En tant qu'enthousiaste des données, je apporte une perspective unique au domaine de la science des données, grâce à mes 15 ans d'expérience en science forensique. Ma transition vers l'informatique m'a permis d'explorer une variété de technologies, notamment Python, PySpark, Java, SQL et des outils de visualisation de données. J'ai développé un intérêt particulier pour l'apprentissage automatique et j'ai utilisé Power BI et Azure Machine Learning pour raconter des histoires convaincantes avec des données.

    Ma passion pour l'innovation se concentre particulièrement sur les domaines de la santé et de la psychologie, où je m'efforce d'améliorer l'expérience utilisateur des produits qui ont un impact sur la vie des gens. Dans mon rôle actuel de scientifique et d'analyste de données, je travaille avec des données psychologiques et je développe des interfaces conviviales pour des produits psychologiques. J'ai contribué à la modernisation des plateformes de diagnostic, au développement de chatbots utilisant l'IA, à la création de questionnaires en ligne et au développement de modèles d'apprentissage automatique et d'apprentissage en profondeur pour analyser et interpréter les données des patients.

    En plus de mes compétences techniques, je suis trilingue en espagnol, anglais et français et j'ai de l'expérience dans l'utilisation d'une variété d'outils et de bibliothèques, notamment Docker, Redis, MongoDB, Jupyterlab, Pandas, Sklearn, Matplotlib et NumPy. Je suis également expérimenté dans le développement front-end et back-end, ayant créé des sites Web à l'aide de Symfony PHP et travaillé avec HTML, CSS et JavaScript.

    Ma formation comprend une maîtrise en criminalistique de l'Institut de criminalistique de la Gendarmerie Royale de Rabat, au Maroc, ainsi qu'un diplôme d'ingénieur en bio-ingénierie et en génie biomédical de FST Settat. J'ai également suivi des programmes de formation en science des données, en intelligence économique et en développement logiciel à l'AFPA et à l'Institut des sciences numériques, de la gestion et de la cognition (IDMC). Plus récemment, j'ai obtenu une certification en data science de l'IDMC, qui m'a permis d'approfondir mes compétences en apprentissage automatique, en analyse de données et en visualisation de données.

    Dans mon temps libre, j'aime faire du kitesurf et trouver un équilibre en dehors du monde numérique. Je suis toujours à la recherche d'opportunités pour combiner mes passions pour les données et l'humanité afin de découvrir de nouveaux insights et de stimuler l'innovation.
    """)

    # Add a footer
    footer()
# Skills page
def competences():
    local_css("style.css")  # Appliquer le CSS

    # Add a header
    header()

    # Skills section
    st.markdown("""
    ### 💻 Compétences Techniques
    - **Programmation** : Python, Java, SQL, HTML/CSS
    - **Data Science** : Pandas, NumPy, Matplotlib, Scikit-Learn, TensorFlow, PyTorch
    - **Big Data** : PySpark, Hadoop
    - **Visualisation de données** : Power BI, Tableau, Matplotlib, Seaborn
    - **Déploiement** : Docker, Azure, Heroku
    - **Outils** : Git, GitHub, Jupyter Notebook, PyCharm, Visual Studio Code
    """)

    # Soft skills section
    st.markdown("""
    ### 💪 Soft Skills
    - **Rigueur** : Mon expérience en sciences forensiques m'a appris à être rigoureux et à prêter attention aux détails.
    - **Créativité** : J'aime trouver des solutions innovantes aux problèmes complexes.
    - **Travail d'équipe** : Je suis un joueur d'équipe et je crois en la collaboration pour atteindre les objectifs communs.
    - **Communication** : Je suis capable de communiquer efficacement mes idées et mes résultats, tant à l'oral qu'à l'écrit.
    - **Adaptabilité** : Je suis flexible et capable de m'adapter à de nouveaux environnements et technologies.
    """)

    # Add a footer
    footer()

# Projects page
def projets():
    local_css("style.css")  # Appliquer le CSS

    # Add a header
    header()

    st.markdown("""
    ### Voici quelques-uns des projets sur lesquels j'ai travaillé:
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
        **Association :** Institute of Digital Sciences, Management and Cognition (IDMC). 
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
        **Association :** Agence nationale pour la formation professionnelle des adultes(AFPA).  
        **Description :** Conception d'un notebook ML pour automatiser les approbations de prêts à l'aide de classificateurs tels que Random Forest et SVM.  
        **Compétences :**
        - pandas 🐼
        - NumPy 🔢
        - Scikit-Learn 🤖
        """)

    with st.expander("Système de Gestion de Prospects avec Support Multi-Bases de Données en JAVA ET JAVA EE (Avr 2023 - Mai 2023)"):
        st.markdown("""
        **Association :** Agence nationale pour la formation professionnelle des adultes(AFPA).   
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
        **Association :** Agence nationale pour la formation professionnelle des adultes(AFPA).   
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

    # Add a footer
    footer()

# CV page
def cv():
    local_css("style.css")  # Appliquer le CSS

    # Add a header
    header()



    # Introduction ou résumé
    st.markdown("""
    ### Mon Curriculum Vitae
   Spécialiste en science des données et en analyse, j'ai développé des compétences avancées en apprentissage automatique, analyse de données, et développement de logiciels à travers divers secteurs industriels. Mon expertise me permet d'apporter des solutions innovantes et efficaces aux défis technologiques actuels.

Je suis passionné par l'impact transformateur de la technologie et je cherche constamment à appliquer mes connaissances pour aider les entreprises à atteindre leurs objectifs stratégiques. Pour une vue complète de mon parcours professionnel et de mes compétences, je vous invite à télécharger mon CV.

Intéressé par une collaboration? Explorez comment mes compétences et mon expérience pourraient bénéficier à votre projet ou organisation.
    """)

    # Bouton de téléchargement du CV
    with open("cv_khribech_bouchaib.pdf", "rb") as file:
        st.download_button(
            label="Télécharger le CV",
            data=file,
            file_name="cv_khribech_bouchaib.pdf",
            mime="application/pdf",
        )

    # Add a footer
    footer()
    
import streamlit as st

def contact():
    # Add your CSS
    local_css("style.css")

    # Add a header
    header()

    st.title("Contactez-Moi")

    # Contact form
    st.markdown("""
    ### 📧 Remplissez le formulaire : 
    """)

    # Form fields
    name = st.text_input("Nom")
    email = st.text_input("Email")
    message = st.text_area("Message")

    # Submit button
    if st.button("Envoyer"):
        import requests
        data = {
            "name": name,
            "email": email,
            "message": message
        }
        response = requests.post("https://formspree.io/f/xjvnlyqz", data=data)
        if response.ok:
            st.markdown(" Votre message a été envoyé avec succès !")
        else:
            st.markdown(" Erreur lors de l'envoi du message. Veuillez réessayer.")

    st.markdown("""
    ### 🌐 Les réseaux sociaux : 
    """)
    # Add social media links as buttons
    col1, col2, col3 = st.columns(3)
    with col1:
      if st.button("LinkedIn"):
        webbrowser.open_new_tab("https://www.linkedin.com/in/khbouchaib/")
    with col2:
      if st.button("GitHub"):
        webbrowser.open_new_tab("https://github.com/KHRIBECHBOUCHAIB")
    with col3:
      if st.button("Twitter"):
        webbrowser.open_new_tab("https://twitter.com/bouchaib_k")

    # Add a footer
    footer()

# Navigation
# Appliquer le CSS globalement
local_css("style.css")

# Titre de la sidebar
st.sidebar.title("🧭 Navigation")

# Options de navigation avec emojis pour plus de visibilité
options_nav = {
    "Accueil": "Accueil",
    "Compétences": "Compétences",
    "Projets": "Projets",
    "CV": "Curriculum vitæ",
    "Contact": "Contact"
}

# Création des options de navigation dans la sidebar
selected_page = st.sidebar.selectbox("Aller à", list(options_nav.keys()), format_func=lambda x: options_nav[x])

# Correspondance des pages aux fonctions
if selected_page == "Accueil":
    accueil()
elif selected_page == "Compétences":
    competences()
elif selected_page == "Projets":
    projets()
elif selected_page == "CV":
    cv()
elif selected_page == "Contact":
    contact()
