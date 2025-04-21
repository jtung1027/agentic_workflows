import logging
import os

import praw

# Configure logging - you might want to integrate this with a broader project logger
logger = logging.getLogger(__name__)


class RedditClient:
    """
    A wrapper class for the PRAW Reddit client.

    Handles initialization using environment variables and provides access
    to the underlying PRAW client instance.
    """

    def __init__(self):
        """
        Initializes the RedditClient by creating a PRAW Reddit instance.

        Reads credentials (REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT)
        from environment variables.
        The `self.client` attribute will be None if initialization fails.
        """
        self.client: praw.Reddit | None = None
        try:
            client_id = os.environ["REDDIT_CLIENT_ID"]
            client_secret = os.environ["REDDIT_CLIENT_SECRET"]
            user_agent = os.environ["REDDIT_USER_AGENT"]
            # Optional: username and password for script-type apps that need user context
            # username = os.environ.get("REDDIT_USERNAME")
            # password = os.environ.get("REDDIT_PASSWORD")

            logger.debug("Initializing PRAW Reddit client...")
            self.client = praw.Reddit(
                client_id=client_id,
                client_secret=client_secret,
                user_agent=user_agent,
                # Uncomment the following lines if using username/password
                # username=username,
                # password=password,
            )
            # Optionally verify authentication immediately (e.g., for non-read-only bots)
            # self.client.user.me()
            logger.info("Reddit client initialized successfully.")

        except KeyError as e:
            logger.error(f"Missing Reddit environment variable: {e}. Reddit client not initialized.")
            self.client = None  # Ensure client is None on failure
        except Exception as e:
            logger.error(f"Failed to initialize PRAW Reddit client: {e}")
            self.client = None  # Ensure client is None on failure

    def get_client(self) -> praw.Reddit | None:
        """Returns the initialized PRAW Reddit client instance, or None if initialization failed."""
        return self.client


# Example of how you might manage a single instance (optional)
# _reddit_client_instance = None
#
# def get_reddit_instance():
#     global _reddit_client_instance
#     if _reddit_client_instance is None:
#         _reddit_client_instance = RedditClient()
#     return _reddit_client_instance
