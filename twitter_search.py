from textblob import TextBlob
from tweepy import OAuthHandler
from db_connect import *
import tweepy
import json
import sys
import re


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        try:
            if status._json['text'][:2] == 'RT':
                status._json['text'] = re.match(r'.*:(.*)' , status._json['text']).group(1)
            insert_row(status._json['text'],
                      status._json['user']['location'],
                      status._json['user']['followers_count'])
        except (KeyboardInterrupt, SystemExit):
            sys.exit()

consumer_key = "b6DRufuzlz7fGdoNe2ixrQnwv"
consumer_secret = "NtNIDO2GdODnt23Q4trOuviww1ACz8qjMmEFyvqS8KEVVy5oRb"
access_token = "543698120-hRu6ls2BlDZPAf6rTtzmFcipJYh4GE4dPptyuznI"
access_secret = "Wz0ZbPPZaK6MtOiaAy6pewFYjiLlyVkQlC6QDBBKzIMlY"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['democrats','democrat',
                       'republicans','republican'], async=True)
