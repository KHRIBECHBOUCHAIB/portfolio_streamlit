import streamlit as st
from PIL import Image
import webbrowser


# Include CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def header():
    header_html = """
    <header class="header">
        <div class="content has-text-centered">
            <h1>Bienvenue sur mon portfolio professionnel</h1>
            <p>Découvrez mes projets et mes compétences en data science et en développement.</p>
        </div>
    </header>
    """
    st.write(header_html, unsafe_allow_html=True)



# Footer function
def footer():
    st.markdown("""
    <footer class="footer">
        <div class="content has-text-centered">
            <p>
                © 2024 Khribech Bouchaib. Tous droits réservés.
                <br>
                <a href="https://www.linkedin.com/in/khbouchaib/" target="_blank">LinkedIn</a>
                &middot;
                <a href="https://github.com/KHRIBECHBOUCHAIB" target="_blank">GitHub</a>
            </p>
        </div>
    </footer>
    """, unsafe_allow_html=True)


# Home page
def accueil():
    local_css("style.css")  # Appliquer le CSS

    # Add a header
    header()

    # Introduction
    st.markdown("""
    ### À propos de Moi
    En tant qu'enthousiaste des données, je apporte une perspective unique au domaine de la science des données, grâce à mes 15 ans d'expérience en science forensique. Ma transition vers l'informatique m'a permis d'explorer une variété de technologies, notamment Python, PySpark, Java, SQL et des outils de visualisation de données. J'ai développé un intérêt particulier pour l'apprentissage automatique et j'ai utilisé Power BI et Azure Machine Learning pour raconter des histoires convaincantes avec des données.

    Ma passion pour l'innovation se concentre particulièrement sur les domaines de la santé et de la psychologie, où je m'efforce d'améliorer l'expérience utilisateur des produits qui ont un impact sur la vie des gens. Dans mon rôle actuel de scientifique et d'analyste de données, je travaille avec des données psychologiques et je développe des interfaces conviviales pour des produits psychologiques. J'ai contribué à la modernisation des plateformes de diagnostic, au développement de chatbots utilisant l'IA, à la création de questionnaires en ligne et au développement de modèles d'apprentissage automatique et d'apprentissage en profondeur pour analyser et interpréter les données des patients.

    En plus de mes compétences techniques, je suis trilingue en espagnol, anglais et français et j'ai de l'expérience dans l'utilisation d'une variété d'outils et de bibliothèques, notamment Docker, Redis, MongoDB, Jupyterlab, Pandas, Sklearn, Matplotlib et NumPy. Je suis également expérimenté dans le développement front-end et back-end, ayant créé des sites Web à l'aide de Symfony PHP et travaillé avec HTML, CSS et JavaScript.

    Ma formation comprend une maîtrise en criminalistique de l'Institut de criminalistique de la Gendarmerie Royale de Rabat, au Maroc, ainsi qu'un diplôme d'ingénieur en bio-ingénierie et en génie biomédical de FST Settat. J'ai également suivi des programmes de formation en science des données, en intelligence économique et en développement logiciel à l'AFPA et à l'Institut des sciences numériques, de la gestion et de la cognition (IDMC). Plus récemment, j'ai obtenu une certification en data science de l'IDMC, qui m'a permis d'approfondir mes compétences en apprentissage automatique, en analyse de données et en visualisation de données.

    Dans mon temps libre, j'aime faire du kitesurf et trouver un équilibre en dehors du monde numérique. Je suis toujours à la recherche d'opportunités pour combiner mes passions pour les données et l'humanité afin de découvrir de nouveaux insights et de stimuler l'innovation.
    """)

 # Afficher le logo
    logo_path = 'images/image1.jpg'

    col1, col2, col3 = st.columns([6, 9, 2])
    with col2:
        st.image(logo_path, width=200)
    # Add a footer
    footer()
    
    
# Skills page
def competences():
    local_css("style.css")  # Appliquer le CSS

    # Add a header
    header()

    # Skills section
    st.markdown("""
    ### Compétences Techniques
    - **Programmation** : Python, Java, SQL, HTML/CSS
    - **Data Science** : Pandas, NumPy, Matplotlib, Scikit-Learn, TensorFlow, PyTorch
    - **Big Data** : PySpark, Hadoop
    - **Visualisation de données** : Power BI, Tableau, Matplotlib, Seaborn
    - **Déploiement** : Docker, Azure, Heroku
    - **Outils** : Git, GitHub, Jupyter Notebook, PyCharm, Visual Studio Code
    """)

    # Soft skills section
    st.markdown("""
    ###  Soft Skills
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



def cv():
    local_css("style.css")  # Apply the CSS

    # Add a header
    header()

    # Introduction or summary
    st.markdown("""
    <div class="content">
        <h2>Mon Curriculum Vitae</h2>
        <p>Spécialiste en science des données et en analyse, j'ai développé des compétences avancées en apprentissage automatique, analyse de données, et développement de logiciels à travers divers secteurs industriels. Mon expertise me permet d'apporter des solutions innovantes et efficaces aux défis technologiques actuels.</p>
        <p>Je suis passionné par l'impact transformateur de la technologie et je cherche constamment à appliquer mes connaissances pour aider les entreprises à atteindre leurs objectifs stratégiques. Pour une vue complète de mon parcours professionnel et de mes compétences, je vous invite à télécharger mon CV.</p>
        <p>Intéressé par une collaboration? Explorez comment mes compétences et mon expérience pourraient bénéficier à votre projet ou organisation.</p>
    </div>
    """, unsafe_allow_html=True)

    # Centering the download button using inline HTML for aesthetics
    st.markdown("<div style='text-align: center;'></div>", unsafe_allow_html=True)

    # Open the file here and keep it open for the download button
    file = open("cv_khribech_bouchaib.pdf", "rb")
    st.download_button(
        label="Télécharger mon CV",
        data=file,
        file_name="cv_khribech_bouchaib.pdf",
        mime="application/pdf",
        key="download-cv"
    )
    file.close()  # Close the file after the button

    # Add some space
    st.markdown("<br>", unsafe_allow_html=True)

    # Add a footer
    footer()


    
def contact():
    # Add your CSS
    local_css("style.css")

    # Add a header
    header()

    # Contact form header with enhanced styling
    st.markdown("### Remplissez le formulaire")
    st.markdown("Veuillez entrer vos informations dans les champs ci-dessous pour me contacter.")

    # Form fields with clear labeling
    with st.form(key='contact_form'):
        name = st.text_input("Nom et prénoms", placeholder="Entrez votre nom complet")
        country = st.text_input("Pays", placeholder="Entrez votre pays")
        entreprise = st.text_input("Entreprise", placeholder="Nom de votre entreprise")
        email = st.text_input("Email", placeholder="exemple@domaine.com")
        message = st.text_area("Message", placeholder="Écrivez votre message ici...", height=150)

        # Submit button
        submit_button = st.form_submit_button("Envoyer")

    if submit_button:
        import requests
        data = {
            "name": name,
            "pays": country,
            "email": email,
            "entreprise": entreprise,
            "message": message
        }
        # Simulating POST request for demonstration (replace URL with your actual endpoint)
        response = requests.post("https://formspree.io/f/xjvnlyqz", data=data)
        if response.ok:
            st.success("Votre message a été envoyé avec succès !")
        else:
            st.error("Erreur lors de l'envoi du message. Veuillez réessayer.")

    # Add a footer
    footer()
    
from PIL import Image

def gallery():

    # Add your CSS
    local_css("style.css")

    # Add a header
    header()

    st.write("Voici quelques-unes de mes photos préférées de mes passe-temps")

    col1, col2, col3 = st.columns(3)
    with col1:
        image = Image.open("images/image6.jpg")
        image = image.resize((250, 400))
        st.image(image)
    with col2:
        image = Image.open("images/image5.jpg")
        image = image.resize((250, 400))
        st.image(image)
    with col3:
        image = Image.open("images/image4.jpg")
        image = image.resize((250, 400))
        st.image(image)

    col1, col2, col3 = st.columns(3)
    with col1:
        image = Image.open("images/image2.jpg")
        image = image.resize((500, 400))
        st.image(image)
    with col2:
        image = Image.open("images/image3.jpg")
        image = image.resize((500, 400))
        st.image(image)
        
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
    "Contact": "Contact",
    "Photos": "Photos"
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
elif selected_page == "Photos":
    gallery()
