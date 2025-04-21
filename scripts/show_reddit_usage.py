#!/usr/bin/env python
import logging
import sys

# Add project root to the Python path
# This allows running the script directly from the scripts directory
# Adjust the path depth (../) if the scripts directory is moved
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from tools.reddit import RedditClient

# Configure basic logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    logging.info("Attempting to create RedditClient...")
    # Create an instance of the client wrapper
    reddit_client_wrapper = RedditClient()

    # Get the actual PRAW client instance
    praw_client = reddit_client_wrapper.get_client() # or reddit_client_wrapper.client

    if praw_client:
        logging.info("Reddit client obtained successfully. Testing API call...")
        # Use the PRAW client as before
        try:
            subreddit_name = "python"
            logging.info(f"Fetching top 5 hot posts from r/{subreddit_name}...")
            subreddit = praw_client.subreddit(subreddit_name)
            for i, submission in enumerate(subreddit.hot(limit=5)):
                logging.info(f"  {i+1}. {submission.title} (Score: {submission.score})")
            logging.info("Successfully fetched posts.")
        except Exception as e:
            logging.error(f"Error fetching from Reddit: {e}")
    else:
        logging.error("Failed to initialize Reddit client. Check environment variables and logs.") 