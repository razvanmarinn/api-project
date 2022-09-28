import tweepy
import apikey

auth = tweepy.OAuthHandler(
   apikey.twitter_key, apikey.secret_key_tw
)
auth.set_access_token(apikey.acces_token_tw, apikey.acces_token_secret_tw)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

print(public_tweets)