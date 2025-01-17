"""this module is used to analyse the sentiment of the data"""

import matplotlib.pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
from dotenv import load_dotenv
import os
import openai

load_dotenv()

SENTIMENT_DIR = "./sentiments/"
os.makedirs(SENTIMENT_DIR, exist_ok=True)
PLOTS_DIR = "./plots/"
os.makedirs(SENTIMENT_DIR, exist_ok=True)


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


def analyze_sentement(df, target: str = "text"):
    # Now we create a new column for what we just did and add it to the Tweet_df dataframe
    df.dropna(subset=[target], inplace=True)
    df[f"{target}_Subjectivity"] = df[target].apply(getSubjectivity)
    df[f"{target}_Polarity"] = df[target].apply(getPolarity)
    # Now display data

    # Group the range of Polarity into different categories

    df[f"{target}_Insight"] = df[f"{target}_Polarity"].apply(getInsight)

    return df


def plot_word_cloud(df, target: str = "text", coin: str = "luna"):
    os.makedirs(f"{PLOTS_DIR}/{coin}", exist_ok=True)
    # Create a word cloud
    plt.figure(figsize=(20, 20))
    allWords = " ".join([twts for twts in df[target]])
    wordCloud = WordCloud(
        width=500, height=300, random_state=21, max_font_size=110
    ).generate(allWords)
    plt.imshow(wordCloud, interpolation="bilinear")
    plt.title(f"{target} Word Cloud")
    plt.axis("off")
    plt.savefig(f"{PLOTS_DIR}/{coin}/{target}_word_cloud.png")
    plt.show()


def analyse_database(df, coin: str = "luna"):
    # Analyze the data

    df = df[["comment", "text", "title"]]
    df = analyze_sentement(df, "text")
    # df = analyze_sentiment_openai(df, "text")
    df = analyze_sentement(df, "comment")
    # df = analyze_sentiment_openai(df, "comment")
    df["text_comment"] = df["text"] + df["comment"]
    df = analyze_sentement(df, "text_comment")
    # df = analyze_sentiment_openai(df, "text_comment")
    plot_word_cloud(df, "comment", coin=coin)
    plot_word_cloud(df, "text", coin=coin)
    df.to_csv(f"{SENTIMENT_DIR}/{coin}_reddit.csv", index=False)
    return df


# Set your OpenAI API key
# Set your OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]


# Function to get sentiment analysis using OpenAI
def get_sentiment(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or "gpt-4"
            messages=[
                {
                    "role": "system",
                    "content": "You are a sentiment analysis assistant. Respond with only one word: Positive, Negative, or Neutral.",
                },
                {
                    "role": "user",
                    "content": f"Analyze the sentiment of the following text: '{text}'",
                },
            ],
            max_tokens=1,  # Limit the response to a single word
            temperature=0.0,  # Keep it deterministic for consistent results
        )
        # Extract sentiment from the response
        sentiment = response["choices"][0]["message"]["content"]
        return sentiment.strip()  # Clean and return the result
    except Exception as e:
        return f"Error: {e}"


# Analyze sentiment for a DataFrame column
def analyze_sentiment_openai(df, target: str = "text"):
    # Drop rows with missing values in the target column
    df.dropna(subset=[target], inplace=True)

    # Apply the OpenAI sentiment analysis to each row in the target column
    df[f"{target}_Sentiment_OpenAI"] = df[target].apply(get_sentiment)

    return df


if __name__ == "__main__":
    # test the functions
    coin = "bitcoin"
    df = pd.read_csv(f"./database/{coin}_reddit.csv")
    analyse_database(df)
