from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from application.models.rest import Rest
from application import db

rest_fields = {
    'id': fields.Integer,
    'init_mood': fields.Integer,
    'end_mood': fields.Integer,
    'content_selected': fields.String,
    'focus_interval': fields.String,
    'rest_interval': fields.String
}

rest_list_fields = {
    'count': fields.Integer,
    'rests': fields.List(fields.Nested(rest_fields)),
}

rest_post_parser = reqparse.RequestParser()
rest_post_parser.add_argument(
    'init_mood',
    type=int,
    required=True,
    location=['json'],
    help='init mood parameter is required'
)
rest_post_parser.add_argument(
    'end_mood',
    type=int,
    required=True,
    location=['json'],
    help='end mood parameter is required'
)
rest_post_parser.add_argument(
    'content_selected',
    type=str,
    required=True,
    location=['json'],
    help='content parameter is required'
)
rest_post_parser.add_argument(
    'focus_interval',
    type=str,
    required=True,
    location=['json'],
    help='focus interval parameter is required'
)
rest_post_parser.add_argument(
    'rest_interval',
    type=str,
    required=True,
    location=['json'],
    help='rest interval parameter is required'
)

class RestsResource(Resource):
    def get(self, rest_id=None):
        if rest_id:
            rest = Rest.query.filter_by(id=rest_id).first()
            return marshal(rest, rest_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            rest = Rest.query.filter_by(**args).order_by(Rest.id)
            if limit:
                rest = rest.limit(limit)

            if offset:
                rest = rest.offset(offset)

            rest = rest.all()

            return marshal({
                'count': len(rest),
                'rests': [marshal(t, rest_fields) for t in rest]
            }, rest_list_fields)

    @marshal_with(rest_fields)
    def post(self):
        args = rest_post_parser.parse_args()

        rest = Rest(**args)
        db.session.add(rest)
        db.session.commit()

        return rest
