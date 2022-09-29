import tweepy
import requests
import pandas as pd
import apikey

client = tweepy.Client( bearer_token=apikey.bearer_token,
                        consumer_key=apikey.twitter_key, 
                        consumer_secret=apikey.secret_key_tw, 
                        access_token=apikey.acces_token_tw, 
                        access_token_secret=apikey.acces_token_secret_tw, 
                        return_type = requests.Response,
                        wait_on_rate_limit=True)

def twitter_api_pull():
    query = 'bitcoin'

# get max. 100 tweets 
    tweets = client.get_recent_tweets_count(query = query , granularity = 'day')
    reindex = ['start', 'end', 'tweet_count']
    tweets_dict = tweets.json()
    tweets_data = tweets_dict['data']
    df_tw = pd.json_normalize(tweets_data)
    df_tw=df_tw.reindex(columns=reindex)
    df_tw['start'] = pd.to_datetime(df_tw['start'], errors='coerce').dt.strftime("%m/%d/%y")
    df_tw['end'] = pd.to_datetime(df_tw['end'], errors='coerce').dt.strftime("%m/%d/%y")
    df_tw.to_csv('csv/twitter_count_7d.csv' , mode = "a+" , index= False)
    print(df_tw)

