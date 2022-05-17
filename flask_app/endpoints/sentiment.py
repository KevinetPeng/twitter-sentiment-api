from operator import itemgetter
from flask import (
    Blueprint, request, jsonify
)
from ..services.twitter_service import (
    TwitterService
)

bp = Blueprint('sentiment', __name__, url_prefix='/sentiment')
twitterService = TwitterService()


@bp.route('/entity/<entity>')
def getTopicSentiment(entity):
    size = request.args.get('size', default=25, type=int)
    data, errors = itemgetter('data', 'errors')(twitterService.byEntity(entity, size))

    if errors:
        return {
            'errors': jsonify(errors),
            'message': 'Error while fetching tweets.',
        }
    

    return {
        'data': data,
        'response_size': len(data),
    }
 