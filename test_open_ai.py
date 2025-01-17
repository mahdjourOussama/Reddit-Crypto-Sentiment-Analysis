"""This module is used to analyze the sentiment of data using OpenAI."""

import pandas as pd
import openai
from dotenv import load_dotenv
import os


load_dotenv()

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
def analyze_sentiment(df, target: str = "Titles"):
    # Drop rows with missing values in the target column
    df.dropna(subset=[target], inplace=True)

    # Apply the OpenAI sentiment analysis to each row in the target column
    df["Sentiment"] = df[target].apply(get_sentiment)

    # Display and return the updated DataFrame
    print(df.head(50))
    return df


if __name__ == "__main__":
    # Test the sentiment analysis
    df = pd.read_csv("./database/luna_reddit_posts.csv")
    analyze_sentiment(df, "text")
