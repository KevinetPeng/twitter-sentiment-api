import tweepy
import re
from dotenv import load_dotenv
import os


class TwitterService:
    def __init__(self):
        load_dotenv()
        self.twitter = tweepy.Client(os.getenv('TWITTER_BEARER_TOKEN'))

    def sanitize_tweet(self, tweet):
        tweet = re.sub('@[^\s]+', '', tweet)
        tweet = re.sub('http[^\s]+', '', tweet)
        tweet = re.sub('RT\s', '', tweet)

        return tweet.strip()

    def byEntity(self, keyword, size):
        res = self.twitter.search_recent_tweets(
            f'entity:"{keyword}" lang:en', max_results=size)

        return {
            'data': list(map(
                lambda tweet: self.sanitize_tweet(tweet.text), res.data
            )),
            'errors': res.errors
        }
