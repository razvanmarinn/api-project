import tweepy
import requests
import time
import apikey



search_term = ['bitcoin', 'eth', 'egld']


class MyStreaming(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            print(tweet.text)
            time.sleep(0.2)
            

stream = MyStreaming(apikey.bearer_token)


for term in search_term:
    stream.add_rules(tweepy.StreamRule(term))


stream.filter(tweet_fields = ['referenced_tweets'])


