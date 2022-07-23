import tweepy
import re
from dotenv import load_dotenv
import os


class TwitterService:
    def __init__(self):
        load_dotenv()
        self.twitter = tweepy.Client(os.getenv('TWITTER_BEARER_TOKEN'))
        self.base_query = 'lang:en -has:videos -has:media -is:retweet'

    def sanitize_tweet(self, tweet):
        tweet = re.sub('@[^\s]+', '', tweet)
        tweet = re.sub('http[^\s]+', '', tweet)
        tweet = re.sub('RT\s', '', tweet)
        tweet = re.sub('\\n', ' ', tweet)

        return tweet.strip()

    def getTweets(self, query, size):
        res = self.twitter.search_recent_tweets(query, max_results=size)

        # todo: support sizes over 100 using next_token
        # print(res.meta['next_token'])

        sanitized_tweets = map(lambda tweet: self.sanitize_tweet(tweet.text), res.data)
        raw_tweets = map(lambda tweet: tweet.text, res.data)

        return {
            'data': {
                'sanitized_tweets': list(sanitized_tweets),
                'raw_tweets': list(raw_tweets),
            },
            'errors': res.errors
        }

    def byEntity(self, entity, size):
        query = f'entity:"{entity}" {self.base_query}'
        print(f'twitter query: <{query}>')

        return self.getTweets(query, size)
    
    def byPhrase(self, phrase, size):
        query = f'{phrase} {self.base_query}'
        print(f'twitter query: <{query}>')

        return self.getTweets(query, size)

    def byExactPhrase(self, phrase, size):
        query = f'"{phrase}" {self.base_query}'
        print(f'twitter query: <{query}>')

        return self.getTweets(query, size)
