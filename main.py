import tweepy as twitter
import keys
from datetime import *

auth = twitter.OAuthHandler(keys.API_KEY, keys.API_KEY_SECRET)
auth.set_access_token(keys.ACCESS_TOKEN, keys.SECRET_ACESS_TOKEN)
API = twitter.API(auth)

def main():
    # 08/29/22 - 84 days
    date_format = "%m/%d/%Y"
    quit_date = datetime.strptime('06/06/2022', date_format)
    current_date = datetime.now()
    delta = (current_date - quit_date).days
    days_since_quit = str(delta)
    tweet = 'עברו ' + days_since_quit + ' ימים מאז הפעם האחרונה שעישנתי 💪🏽'
    API.update_status(tweet)

    
if __name__ == "__main__":
    main()
