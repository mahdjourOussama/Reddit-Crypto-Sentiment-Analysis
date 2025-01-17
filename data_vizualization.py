"""this module is used to visualize the data in the form of graphs and charts"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# def plot_cooment_score(df):
#     plt.figure(figsize=(10, 6))
#     sns.histplot(df["comment_score"], bins=30, kde=True)
#     plt.title("Distribution des scores des commentaires")
#     plt.xlabel("Score")
#     plt.ylabel("Fréquence")
#     plt.show()


# def plot_analyse_temporal_post(df):
#     # Conversion de la colonne 'created_utc' en format datetime
#     df["created_utc"] = pd.to_datetime(df["created_utc"], unit="s")

#     # Graphique temporel des posts par mois
#     df["month"] = df["created_utc"].dt.to_period("M")
#     posts_per_month = df.groupby("month").size()

#     # Plot de la tendance des posts par mois
#     plt.figure(figsize=(10, 6))
#     posts_per_month.plot(kind="line")
#     plt.title("Nombre de posts par mois")
#     plt.xlabel("Mois")
#     plt.ylabel("Nombre de posts")
#     plt.xticks(rotation=45)
#     plt.show()


# def plot_sentiment_insight(df):
#     plt.figure(figsize=(10, 6))
#     sns.countplot(data=df, x="Sentiment", order=["Positive", "Negative", "Neutral"])
#     plt.title("Distribution des sentiments")
#     plt.xlabel("Sentiment")
#     plt.ylabel("Fréquence")
#     plt.show()


# def plot_score_post(df):
#     # Analyse des scores des posts (moyenne par mois)
#     df["month"] = df["created_utc"].dt.to_period("M")
#     average_scores_by_month = df.groupby("month")["score"].mean()

#     # Graphique de la moyenne des scores des posts par mois
#     plt.figure(figsize=(10, 6))
#     average_scores_by_month.plot(kind="line", marker="o")
#     plt.title("Moyenne des scores des posts par mois")
#     plt.xlabel("Mois")
#     plt.ylabel("Moyenne des scores")
#     plt.xticks(rotation=45)
#     plt.show()


def plot_sentiments(df, target):
    # Barplot du nombre de commentaires positifs et négatifs
    figure = plt.figure(figsize=(10, 6))
    # plt.figure(figsize=(10, 6))
    sns.countplot(x=f"{target}_Insight", data=df, palette="coolwarm")
    plt.title(f"Nombre de {target} positifs vs négatifs")
    plt.xlabel("Insight")
    plt.ylabel(f"Nombre de {target}")
    return figure
