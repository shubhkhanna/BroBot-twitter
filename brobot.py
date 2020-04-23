import tweepy
import time
from time import sleep
import os
from os import environ

#Enter the keys and Secrets of your account
consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q = ('@ciies2 OR @elonmusk OR @narendramodi OR @DituGoogle OR #ciiesdit OR @khannashubh_')).items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found !
        tweet.retweet()
        print('Retweeted to : @' + tweet.user.screen_name)

        #Favorite the tweet !
        tweet.favorite()
        print('Liked the tweet')

        # Follow the user who tweeted !
        tweet.user.follow()
        print('Followed : @' + tweet.user.screen_name)

        # Add sleep method to space tweets by 900 seconds each !!
        sleep(900)

    except tweepy.TweepError as e:
        print(e.reason)


