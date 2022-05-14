from flask import (
    Blueprint, request
)

bp = Blueprint('sentiment', __name__, url_prefix='/sentiment')


@bp.route('/<topic>')
def getTopicSentiment(topic):
    size = request.args.get('size', default = 25, type = int)

    return {
        "data": "searched for: " + topic,
        "size param": size
    }
