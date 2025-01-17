"""this module is used to analyse the sentiment of the data"""

import matplotlib.pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS
import pandas as pd


# Create a function to get the subjectivity
def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity


# Create a function to get Polarity
def getPolarity(text):
    return TextBlob(text).sentiment.polarity


def getInsight(score):
    if score < 0:
        return "Negative"
    elif score == 0:
        return "Neutral"
    else:
        return "Positive"


def analyze_sentement(df, target: str = "Titles"):
    # Now we create a new column for what we just did and add it to the Tweet_df dataframe
    df.dropna(subset=[target], inplace=True)
    df["Subjectivity"] = df[target].apply(getSubjectivity)
    df["Polarity"] = df[target].apply(getPolarity)
    # Now display data

    # Group the range of Polarity into different categories

    df["Insight"] = df["Polarity"].apply(getInsight)
    print(df.head(50))
    return df


if __name__ == "__main__":
    # test the functions
    df = pd.read_csv("./database/luna_reddit_posts.csv")
    analyze_sentement(df, "text")
