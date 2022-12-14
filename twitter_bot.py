# Import Dependencies
"""tweepy module provides access to Twitter via Python. keys module is where
 API, API Secret, Access Token, and Access Token Secret are stored
"""
import time
import tweepy
import colorama
from colorama import Back
import keys

# Initialize colorama
colorama.init(autoreset=True)

# Font color for print statements
twitter_color = Back.BLUE

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
twitter_api = tweepy.API(twitter_auth, wait_on_rate_limit=True)

# Prints exception if something is wrong with authentication.
class AuthenticationUnsuccessful(Exception):
    """Raised when authentication is not successful"""


# Prints exception if something is wrong with retweeting or liking a tweet.
class RetweetUnsuccessful(Exception):
    """Raised when retweet/like is not successful"""


# Prints exception if something is wrong with following.
class FollowUnsuccessful(Exception):
    """Raised when a follow request is not successful"""


# Tries to validate credentials
try:
    print(twitter_api.verify_credentials())
    print(twitter_color + "Successfully Logged In")
except tweepy.TweepyException as e:
    print(e)
except AuthenticationUnsuccessful as e:
    print(e)

# Send a test tweet. Uncomment lines below to test twitter-bot!
# twitter_api.update_status(
#     status='Hello World! "This tweet was sent using #tweepy with python." \
# #YourHashTagHere'
# )

# Initialize oauth handler and set access token
twitter_client = tweepy.Client(
    BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
twitter_auth = tweepy.OAuth1UserHandler(
    API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)

# Initialize tweepy api object using the authentication handler object
twitter_api = tweepy.API(twitter_auth, wait_on_rate_limit=True)

# Class for StreamingClient
class TwitterStream(tweepy.StreamingClient):
    """The bot will start a stream that retweets and likes tweets based on stream.add_rules"""

    def on_connect(self):
        """Prints Sucessfully Connected once stream is initialized"""
        print(twitter_color + "Successfully Connected via Twitter Stream")
        print("----------------------------------------------------------")

        # Follows new followers on connect
        twitter_follow = tweepy.Cursor(twitter_api.get_followers).items()

        for follower in twitter_follow:

            if not follower.following:

                try:
                    follower.follow()
                    print(
                        twitter_color + "Now Following: " + "@" + follower.screen_name
                    )
                    print("----------------------------------------------------------")

                except FollowUnsuccessful as follow_exception:
                    print(follow_exception)

    def on_tweet(self, tweet):
        """Functions that checks if a tweet passes through the stream"""
        if not twitter_client.retweet(tweet.id) or twitter_client.like(tweet.id):

            try:
                # Retweet the tweet
                twitter_client.retweet(tweet.id)
                print(twitter_color + "Tweet Successfully Retweeted")

                # Favorites the tweet
                twitter_client.like(tweet.id)
                print(twitter_color + "Tweet Successfully Liked")
                print("\n")

                # Prints the tweet on screen
                print(tweet.text)
                print("----------------------------------------------------------")

                # Starts a delay between tweets
                time.sleep(5)

            except RetweetUnsuccessful as exception:
                print(exception)


# Creates the stream object
stream = TwitterStream(bearer_token=BEARER_TOKEN)


# More settings for add_rules can be found here:
# https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule#examples

# Stream rules for twitter-bot to track. Uncomment line below to enable. Change #YourHashTagHere!
# stream.add_rules(tweepy.StreamRule('"#YourHashTagHere" lang:en -is:retweet -is:reply -is:quote'))

# Stream Rules Example # 2
# stream.add_rules(tweepy.StreamRule('"Python" lang:en -is:retweet -is:reply -is:quote'))

# Stream Rules Example # 3
# stream.add_rules(tweepy.StreamRule("from:usernamehere"))

# Deletes Stream rules added in previous stream.add_rules(). Uncomment #stream.delete_rules below
# You can obtain a list of rule ids from making a request to the following api endpoint:
# curl "https://api.twitter.com/2/tweets/search/stream/rules" -H "Authorization: Bearer XXXXXXXXXXX"

# stream.delete_rules(
#     ids=["1590108706184007690", "1590143217504342719"]
# )

# Starts the Stream
stream.filter()
