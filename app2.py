import streamlit as st
import random

# Afficher l'image
st.image("images/imgapp2.png", caption="Une Fée du SEO")



questions_optimisation_page = [
    "Comment optimisez-vous le contenu pour le SEO sur la page ?",
    "Quels sont les éléments clés à optimiser sur une page web ?",
    "Comment optimisez-vous les balises de titre pour le SEO ?",
    "Quelle est l'importance de la méta-description pour le SEO ?",
    "Comment gérez-vous le contenu dupliqué sur un site web ?",
    "Qu'est-ce qu'une bonne densité de mots-clés ?",
    "Comment utilisez-vous les balises H1, H2, H3 pour le référencement ?",
    "Quel est l'impact des images optimisées sur le SEO ?",
    "Comment assurez-vous que votre site est mobile-friendly ?",
    "Quelle est l'importance de la vitesse de chargement d'une page ?",
    "Comment gérez-vous le contenu obsolète sur un site web ?",
    "Quelles stratégies utilisez-vous pour améliorer l'expérience utilisateur ?",
    
]

questions_seo_technique = [
    "Quels outils utilisez-vous pour le SEO technique et pourquoi ?",
    "Comment gérez-vous le maillage interne sur un site web ?",
    "Comment surveillez-vous la santé technique d'un site web ?",
    "Quels outils utilisez-vous pour les audits SEO techniques ?",
    "Comment résolvez-vous les problèmes de crawl et d'indexation ?",
    "Quelle est l'importance du fichier sitemap XML ?",
    "Comment optimisez-vous un site pour la recherche vocale ?",
    "Quels sont les enjeux du SEO mobile ?",
    "Comment gérez-vous les redirections 301/302 ?",
    "Quelle est l'importance des backlinks internes ?",
    "Comment diagnostiquez-vous et corrigez-vous les erreurs 404 ?",
    "Quelle est l'importance de l'architecture du site pour le SEO ?",
]

questions_seo_horspage = [
    "Comment évaluez-vous la qualité d'un backlink ?",
    "Quelles stratégies utilisez-vous pour obtenir des backlinks ?",
    "Comment gérez-vous votre réputation en ligne ?",
    "Quel est l'impact des réseaux sociaux sur le SEO ?",
    "Comment utilisez-vous le guest blogging pour le SEO ?",
    "Quelles méthodes utilisez-vous pour le link building ?",
    "Comment mesurez-vous l'efficacité de votre SEO hors-page ?",
    "Quelle est votre approche pour le marketing de contenu ?",
    "Comment gérez-vous les liens toxiques ?",
    "Quelle est l'importance des avis en ligne pour le SEO ?",
]

questions_personnalité = [
    "Comment gérez-vous la pression et les deadlines serrées ?",
    "Quelles sont vos plus grandes forces en tant que consultant SEO ?",
    "Comment restez-vous informé des dernières tendances en SEO ?",
    "Comment gérez-vous les désaccords avec un client sur une stratégie SEO ?",
    "Quel a été votre plus grand défi en SEO et comment l'avez-vous surmonté ?",
    "Comment travaillez-vous en équipe ?",
    "Quelle est votre approche pour résoudre un problème complexe ?",
    "Comment gérez-vous les attentes des clients ?",
    "Quelles sont vos méthodes pour rester organisé et efficace ?",
    "Comment gérez-vous les échecs ou les résultats insatisfaisants ?"
]

questions_bonus_perso = [
    "Pourquoi avoir choisi le SEO comme carrière ?",
    "Qu'as-tu appris et retenu pendant les 6 dernières semaines de formation ?",
    "Pourquoi avoir choisi le SEO comme carrière ?",
    "Qu'as-tu appris et retenu pendant les 6 dernières semaines de formation ?",
    "Qu'apporterais-tu de plus qu'un autre candidat ?",
    "Quels sont les 3 piliers du SEO et quel est ton favori ?",
    "Pourriez-vous me définir des objectifs de positionnement et proposer une arborescence axée sur les requêtes informationnelles ?",
    "Pourriez-vous identifier les actions d'optimisations nécessaires pour répondre aux objectifs définis sur la partie éditoriale (hors technique) ?",
    "Pourriez-vous réaliser un brief SEO pour la rédaction de contenu ?",
    "Expliquez-nous une méthodologie d'analyse, de sélection et de qualification des requêtes ?"
]

st.title('Fée du SEO')
st.write("""
         Cette application génère des questions pour vous entrainer à passer des entretiens et ne plus être surpris.
         Sélectionnez les options pertinentes pour générer des questions.
         """)

# Sélecteur de thématique
theme = st.selectbox('Choisissez une thématique', ['Optimisation on page', 'SEO technique', 'SEO hors page', 'Personnalité du candidat', 'Bonus Perso'])
generate_button = st.button('Générer une Question')

if generate_button:
    st.header("Question Générée")

    if theme == 'Optimisation on page':
        question = random.choice(questions_optimisation_page)
    elif theme == 'SEO technique':
        question = random.choice(questions_seo_technique)
    elif theme == 'SEO hors page':
        question = random.choice(questions_seo_horspage)
    elif theme == 'Personnalité du candidat':
        question = random.choice(questions_personnalité)
    elif theme == 'Bonus Perso':
        question = random.choice(questions_bonus_perso)
    else:
        question = "Veuillez sélectionner une thématique."

    st.write(question)


st.markdown("""
    ### 🌟 En Quête d'Opportunités en SEO 🌟
    Hey là ! 👋 Je suis actuellement à la recherche d'une alternance pour un poste de Consultante SEO.
    
    Comme cette application le montre, je suis pleine de ressources, créative et prête à relever de nouveaux défis ! 💡🚀
    
    Si vous avez des opportunités, des conseils, ou si vous voulez juste papoter SEO, je suis toute ouïe ! 
    
    N'hésitez pas à m'envoyer un message pour un entretien, m'encourager ou simplement pour échanger sur le monde fascinant du SEO.
    
    J'ai hâte de collaborer sur des projets passionnants et d'apporter ma touche créative ! 🌈
    
    ### Restons Connectés !
    """, unsafe_allow_html=True)

url_linkedin = "https://www.linkedin.com/in/valérie-matime-seo/"
st.markdown(f"[Cliquez ici pour visiter mon profil LinkedIn !]({url_linkedin}) 🌐", unsafe_allow_html=True)

