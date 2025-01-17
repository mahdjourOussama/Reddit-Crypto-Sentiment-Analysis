"""this module is a streamlit app that uses the data from the reddit API to visualize the data in the form of graphs and charts"""

import streamlit as st
import pandas as pd
from data_processing import fetch_reddit_post
from sentiment_analyses import analyse_database
from data_vizualization import (
    plot_sentiments,
)

st.set_page_config()

# Input de l'utilisateur
st.markdown(
    "<h1 style='font-size:38px; font-weight:bold;'>Quelle Cryptomonnaie vous intéresse ?</h1>",
    unsafe_allow_html=True,
)
coin = st.text_input("")
if coin:
    st.markdown(
        f"<h2 style='font-size:32px; font-weight:bold;'>Analyse des données pour {coin}</h2>",
        unsafe_allow_html=True,
    )

    # Texte personnalisé avec style

    # Charger et afficher les données
    data = fetch_reddit_post(coin_name=coin, limit=10)
    sentiments = analyse_database(data, coin)
    data_sentiments = sentiments[
        ["title", "text_Insight", "comment_Insight", "text_comment_Insight"]
    ]
    st.dataframe(data_sentiments.head(10), use_container_width=True)
    targets = ["text", "comment", "text_comment"]
    for target in targets:
        plot = plot_sentiments(data_sentiments, target)
        st.write(target)
        st.pyplot(plot)
