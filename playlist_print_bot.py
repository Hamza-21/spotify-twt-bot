import tweepy
from tweepy.api import API
from tweepy.models import Media
from time import sleep

def twtTests():
    consumer_key = 'rKYbtbfD9EvcMFzSYTDkucht7'
    consumer_secret = 'gEDV1EEPem36fsKnG68QVphCm0sd6lMn2Crap9UNPZnfxI36ju'
    access_token = '1436718387099357188-Wcgh99lTznRf4ViwIhpTwOam29HdJR'
    access_token_secret = 'uJvM3m34RGrbTFVSWzBDTIFKUiOj82zLkC0y2u2QR4CJS'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    file = open("pl_info2.txt")
    lines = file.readlines()

    i = 0
    while (i < 5):
        actualTweet = lines[i] + lines[i+1]
        api.update_status(status = actualTweet,)
        i += 2
        sleep(5)

if __name__ == '__main__':
    twtTests()