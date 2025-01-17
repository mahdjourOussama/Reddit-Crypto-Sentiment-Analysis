"""this module for fetchin and processing reddit data"""

import pandas as pd
import os
from dotenv import load_dotenv
import praw

# Load environment variables from the .env file
load_dotenv()
# Set up your Reddit API credentials
CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
REDDIT_USERNAME = os.environ["REDDIT_USERNAME"]
REDDIT_SECRET = os.environ["REDDIT_SECRET"]
USER_AGENT = "crypto Agent"

# Authenticate using OAuth2
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    password=REDDIT_SECRET,
    user_agent=USER_AGENT,
    username=REDDIT_USERNAME,
)

subreddit_name = "CryptoCurrency"  # specific groupe

DATA_DIR = "./database/"


def fetch_reddit_post(coin_name: str = "bitcoin", limit: int = 10) -> pd.DataFrame:
    """Fetch the top 10 hot posts containing the coin_name in the subreddit_name"""

    subreddit = reddit.subreddit(subreddit_name)
    submissions = subreddit.search(coin_name, sort="new", limit=limit)
    df = pd.DataFrame(
        [
            {
                "title": submission.title,
                "text": submission.selftext,
                "score": submission.score,
                "num_comments": submission.num_comments,
                "upvote_ratio": submission.upvote_ratio,
                "id": submission.id,
                "url": submission.url,
                "comment": comment.body,
                "comment_score": comment.score,
                "created_utc": submission.created_utc,
            }
            for submission in submissions
            for comment in submission.comments
        ]
    )
    df = clean_data(df)
    df.to_csv(f"{DATA_DIR}/{scope_query}_reddit.csv", index=False)
    return df


def clean_data(data):
    """
    Clean the fetched Reddit data.

    Parameters:
        data (pd.DataFrame): Raw data fetched from Reddit.

    Returns:
        pd.DataFrame: Cleaned data.
    """
    target = ["title", "text", "comment"]
    # Drop rows with missing titles or text
    data = data.dropna(subset=target)

    # Convert created_utc to datetime
    data["created_datetime"] = pd.to_datetime(data["created_utc"], unit="s")

    # Drop duplicate posts based on title and text
    data = data.drop_duplicates(subset=target)

    return data


if __name__ == "__main__":
    DATA_DIR = "./database/"
    # test the functions
    scope_query = "luna"  # You can adjust this query based on your
    df = fetch_reddit_post(scope_query, 1)
    print(df.head())
