from operator import itemgetter
from tokenize import Double
from flask import (
    Blueprint, request
)
from ..services.twitter_service import (
    TwitterService
)
from ..utils.sentiment import (
    Sentiment
)

bp = Blueprint('sentiment', __name__, url_prefix='/sentiment')
twitterService = TwitterService()
sentiment = Sentiment()

default_threshold = 0.05


@bp.route('/entity/<entity>')
def getTopicSentiment(entity):
    size = request.args.get('size', default=25, type=int)
    sentiment_threshold = request.args.get('threshold', default_threshold, type=float)

    tweets, errors = itemgetter('data', 'errors')(twitterService.byEntity(entity, size))
    sanitized_tweets, raw_tweets = tweets['sanitized_tweets'], tweets['raw_tweets']

    if errors:
        print('error in entity endpoint')
        raise Exception()
    
    sentiment_data = sentiment.getSentiment(sanitized_tweets, sentiment_threshold)

    return {
        'sentiment_summary': sentiment_data['summary'],
        'sample_size': len(raw_tweets),
        'raw_tweets': raw_tweets,
        'raw_sentiments': sentiment_data['sentiment_list'],
    }
