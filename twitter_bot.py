# Import Dependencies
"""tweepy module provides access to Twitter via Python. keys module is where
 API, API Secret, Access Token, and Access Token Secret are stored
"""
import tweepy
import keys

# Assign keys
API_KEY = keys.API_KEY
API_SECRET = keys.API_SECRET
ACCESS_TOKEN = keys.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = keys.ACCESS_TOKEN_SECRET

# Initialize oauth handler and set access token
twitter_oauth = tweepy.OAuthHandler(API_KEY, API_SECRET)
twitter_oauth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Initialize tweepy api object using the authentication handler object
twitter_api = tweepy.API(twitter_oauth)

# Validates credentials. Prints exception if something is wrong.
class AuthenticationUnsuccessful(Exception):
    """Raised when authentication is not successful"""


try:
    print(twitter_api.verify_credentials())
    print("Successfully Logged In")
except tweepy.TweepyException as e:
    print(e)
except AuthenticationUnsuccessful as e:
    print(e)

# Sends a test tweet. Uncomment lines below to send your first tweet using tweepy!
# twitter_api.update_status(
#     status='Hello World! "This tweet was sent using #tweepy with python." \
# #techtwitter #blacktechtwitter'
# )
