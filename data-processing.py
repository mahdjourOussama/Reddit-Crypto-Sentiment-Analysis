"""this module for fetchin and processing reddit data"""

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
USER_AGENT = "test agent"

# Authenticate using OAuth2
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    password=REDDIT_SECRET,
    user_agent=USER_AGENT,
    username=REDDIT_USERNAME,
)
# Search for posts related to RATP in a specific subreddit
subreddit_name = "paris"  # specific groupe
scope_query = "ratp"  # You can adjust this query based on your
# needs use OR to seperate words.
# Get the subreddit instance
subreddit = reddit.subreddit(subreddit_name)
# Retrieve top 10 hot posts containing the scope_query
ratp_submissions = subreddit.search(scope_query, sort="hot", limit=10)
for submission in ratp_submissions:
    submission = {
        "submission_title": submission.title,
        "submission_text": submission.selftext,
    }
    print(submission)
