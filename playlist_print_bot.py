import tweepy
from tweepy.api import API
from tweepy.models import Media
from time import sleep

def twtTests():
    consumer_key = '#'
    consumer_secret = '#'
    access_token = '#-#'
    access_token_secret = '#'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    file = open("pl_info2.txt")
    lines = file.readlines()

    i = 0
    while (i < 914): #number of lines in the file, can be automated but I'm lazy 
        actualTweet = lines[i] + lines[i+1]
        api.update_status(status = actualTweet,)
        i += 2
        sleep(28800)

if __name__ == '__main__':
    twtTests()
