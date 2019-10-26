import tweepy
import settings

def puttweet():
    CONSUMER_KEY = settings.CONSUMER_KEY
    CONSUMER_SECRET = settings.CONSUMER_SECRET

    ACCESS_TOKEN = settings.ACCESS_TOKEN
    ACCESS_TOKEN_SECRET = settings.ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    api.update_status("heroku,py乙")
