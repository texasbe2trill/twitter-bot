# Import Dependencies
"""tweepy module provides access to Twitter via Python. keys module is where
 API, API Secret, Access Token, and Access Token Secret are stored
"""
import time
import tweepy
import keys

# Assign keys
API_KEY = keys.API_KEY
API_SECRET = keys.API_SECRET
ACCESS_TOKEN = keys.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = keys.ACCESS_TOKEN_SECRET
BEARER_TOKEN = keys.BEARER_TOKEN

# Initialize oauth handler and set access token
twitter_client = tweepy.Client(
    BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
twitter_auth = tweepy.OAuth1UserHandler(
    API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)

# Initialize tweepy api object using the authentication handler object
twitter_api = tweepy.API(twitter_auth)

# Validates credentials. Prints exception if something is wrong.
class AuthenticationUnsuccessful(Exception):
    """Raised when authentication is not successful"""


# Prints exception if something is wrong with retweeting or liking a tweet.
class RetweetUnsuccessful(Exception):
    """Raised when retweet/like is not successful"""


try:
    print(twitter_api.verify_credentials())
    print("Successfully Logged In")
except tweepy.TweepyException as e:
    print(e)
except AuthenticationUnsuccessful as e:
    print(e)

# Send a test tweet. Uncomment lines below to test twitter-bot!
# twitter_api.update_status(
#     status='Hello World! "This tweet was sent using #tweepy with python." \
# #techtwitter #blacktechtwitter'
# )

# Initialize oauth handler and set access token
twitter_client = tweepy.Client(
    BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
twitter_auth = tweepy.OAuth1UserHandler(
    API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)

# Initialize tweepy api object using the authentication handler object
twitter_api = tweepy.API(twitter_auth)

# Class for StreamingClient
class TwitterStream(tweepy.StreamingClient):
    """The bot will start a stream that retweets and likes tweets based on stream.add_rules"""

    def on_connect(self):
        """Prints Sucessfully Connected once stream is initialized"""
        print("Successfully Connected via Twitter Stream")

    def on_tweet(self, tweet):
        """Functions that checks if a tweet passes through the stream"""
        if not twitter_client.retweet(tweet.id) or twitter_client.like(tweet.id):

            try:
                # Retweet the tweet
                twitter_client.retweet(tweet.id)
                print("Tweet Successfully Retweeted")
                print(tweet.text)

                # Favorites the tweet
                twitter_client.like(tweet.id)
                print("Tweet Successfully Liked")
                print(tweet.text)

                # Starts a delay between tweets
                time.sleep(0.5)

            except RetweetUnsuccessful as exception:
                print(exception)


# Creates the stream object
stream = TwitterStream(bearer_token=BEARER_TOKEN)

# Stream rules for twitter-bot to track. Uncomment line below to enable. Change #BrooklynNets!
# stream.add_rules(tweepy.StreamRule("#BrooklynNets"))

# Starts the Stream
stream.filter()
