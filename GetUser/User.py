# -*- coding: utf-8 -*-
 
import tweepy
import urllib
import datetime
import sys
import csv 
import pytest
from tweepy import OAuthHandler
from tweepy import Cursor

CONSUMER_KEY = 'WrpU07endjNhOFEgblLSi8TuJ'
CONSUMER_SECRET = 'lRDwyzgKpaRrd9q5qrfIeiyj8f35beWZsEU8ZDcK6LrP4TpOEB'
ACCESS_KEY = '1023819858-776WgZFmW9w9XFHp93YiEOsHdpl0LWb0nXASGYW'
ACCESS_SECRET = '9Z7nETf3IW2blOAjdkd3NQ8WK7q1JrAr19xI5d6q6fHad'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

result = []

csvFile = open('User.csv', 'a')
csvWriter = csv.writer(csvFile)

def get_TweetbyUser(keyword):
    page_count = 0  
    for tweets in tweepy.Cursor(
            api.search, 
            q=keyword, 
            count=100,
            result_type="recent", 
            include_entities=True
            ).pages():  

        page_count += 1  
        if page_count >= 2:  
            break

        for tweet in tweets:
            accounts = { "fullname:"+ keyword, "href:/"+ tweet.user.name, "id:" + tweet.id_str }
            hashtags = ["hashtags:" + "#" + str(tweet.entities.get('hashtags'))]
            _date = tweet.created_at
            dt = ["date: "+ _date.strftime("%I:%M %p - %d %B %Y")]
            likes = ["likes:" + str(tweet.favorite_count)]
            replies = ["replies: None"] # This object is only available with the Premium and Enterprise tier products.
            retweet = ["retweets:" + str(tweet.retweet_count)]
            text = ["text:" + str(tweet.text)]

            csvWriter.writerow(accounts)
            csvWriter.writerow(dt)
            csvWriter.writerow(hashtags)
            csvWriter.writerow(likes)
            csvWriter.writerow(replies)
            csvWriter.writerow(retweet)
            csvWriter.writerow(text)
            csvWriter.writerow('--------------------------------------------------------')
    
            result.append(accounts)
            result.append(dt)
            result.append(hashtags)
            result.append(likes)
            result.append(replies) 
            result.append(retweet)
            result.append(text)
            
    print(result)
    
def _executive(keyword):

    if keyword is not None :
        get_TweetbyUser(keyword)
    else :
        print("Please Check the Username you wrote")

data_now = str(input("UserName:"))
keyword = data_now
_executive(keyword)