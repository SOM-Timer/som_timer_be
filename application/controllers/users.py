from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from application.models.user import User
from application import db

user_fields = {
    'id': fields.Integer,
    'user_name': fields.String,
    'token': fields.String
}

user_list_fields = {
    'count': fields.Integer,
    'users': fields.List(fields.Nested(user_fields)),
}

user_post_parser = reqparse.RequestParser()
user_post_parser.add_argument(
    'user_name',
    type=str,
    required=True,
    location=['json'],
    help='user_name parameter is required'
)
user_post_parser.add_argument(
    'token',
    type=str,
    required=True,
    location=['json'],
    help='token parameter is required'
)

class UsersResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = User.query.filter_by(id=user_id).first()
            return marshal(user, user_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            user = User.query.filter_by(**args).order_by(User.id)
            if limit:
                user = user.limit(limit)

            if offset:
                user = user.offset(offset)

            user = user.all()

            return marshal({
                'count': len(user),
                'users': [marshal(t, user_fields) for t in user]
            }, user_list_fields)

    @marshal_with(user_fields)
    def post(self):
        args = user_post_parser.parse_args()

        user = User(**args)
        db.session.add(user)
        db.session.commit()

        return user