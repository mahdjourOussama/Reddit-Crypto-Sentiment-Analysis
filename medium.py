import pandas as pd
import numpy as np
import re  # RegEx : Regular expression
import os
from dotenv import load_dotenv
import praw
import matplotlib.pyplot as plt

# Load environment variables from the .env file
load_dotenv()
# Set up your Reddit API credentials
CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
REDDIT_USERNAME = os.environ["REDDIT_USERNAME"]
REDDIT_SECRET = os.environ["REDDIT_SECRET"]
USER_AGENT = "test agent"

# Authenticate using OAuth2
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    password=REDDIT_SECRET,
    user_agent=USER_AGENT,
    username=REDDIT_USERNAME,
)

# Hot new rising topics
headlines = set()
for submission in reddit.subreddit("bitcoin").hot(limit=None):
    headlines.add(submission.title)


# Create a dataframe from the scrapped data
reddit_df = pd.DataFrame(headlines)
reddit_df.columns = ["Titles"]
reddit_df.Titles.duplicated().sum()


# Create a function to clean the tweets
def cleanTxt(text):
    text = re.sub(r"@[A-Za-z0–9]+", "", text)  # Remove @mentions replace with blank
    text = re.sub(r"#", "", text)  # Remove the '#' symbol, replace with blank
    text = re.sub(r"RT[\s]+", "", text)  # Removing RT, replace with blank
    text = re.sub(r"https?:\/\/\S+", "", text)  # Remove the hyperlinks
    text = re.sub(r":", "", text)  # Remove :
    return text


# Cleaning the text
reddit_df["Titles"] = reddit_df["Titles"].apply(cleanTxt)
# Show the clean text
reddit_df.head()
print(reddit_df.head())
exit


# Next we have to remove emoji & Unicode from the Tweet data.
def remove_emoji(string):
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002500-\U00002BEF"  # chinese char
        "\U00002702-\U000027B0"
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\U0001f926-\U0001f937"
        "\U00010000-\U0010ffff"
        "\u2640-\u2642"
        "\u2600-\u2B55"
        "\u200d"
        "\u23cf"
        "\u23e9"
        "\u231a"
        "\ufe0f"  # dingbats
        "\u3030"
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r"", string)


# Cleaning the text
reddit_df["Titles"] = reddit_df["Titles"].apply(remove_emoji)
# Show the clean text
reddit_df.head()


from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS


# Create a function to get the subjectivity
def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity


# Create a function to get Polarity
def getPolarity(text):
    return TextBlob(text).sentiment.polarity


# Now we create a new column for what we just did and add it to the Tweet_df dataframe
reddit_df["Subjectivity"] = reddit_df["Titles"].apply(getSubjectivity)
reddit_df["Polarity"] = reddit_df["Titles"].apply(getPolarity)
# Now display data


# Group the range of Polarity into different categories
def getInsight(score):
    if score < 0:
        return "Negative"
    elif score == 0:
        return "Neutral"
    else:
        return "Positive"


reddit_df["Insight"] = reddit_df["Polarity"].apply(getInsight)
print(reddit_df.head(50))
stopwords = STOPWORDS

text = " ".join([twts for twts in reddit_df["Titles"]])  # To join all tweet
# generate word cloud
wordcloud = WordCloud(
    width=1000, height=600, max_words=100, stopwords=stopwords, background_color="black"
).generate(text)
# Display the generated image:
# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color="black").generate(text)

# Plot the word cloud
plt.figure(figsize=(20, 10), facecolor="k")
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
