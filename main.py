import tweepy as twitter
import keys
from datetime import datetime

auth = twitter.OAuthHandler(keys.API_KEY, keys.API_KEY_SECRET)
auth.set_access_token(keys.ACCESS_TOKEN, keys.SECRET_ACESS_TOKEN)
api = twitter.API(auth)

def twitter_bot()