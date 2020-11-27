from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from application.models.user import User
from application.models.timer import Timer
from application.models.rest import Rest
from application import db

user_fields = {
    'id': fields.Integer,
    'user_name': fields.String,
    'email': fields.String
}

user_list_fields = {
    'count': fields.Integer,
    'users': fields.List(fields.Nested(user_fields)),
}

timer_fields = {
    'id': fields.Integer,
    'work_interval': fields.String,
    'rest_interval': fields.String,
    'sound': fields.String,
    'mood': fields.Boolean,
    'user_id': fields.Integer
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
    'email',
    type=str,
    required=True,
    location=['json'],
    help='email parameter is required'
)

timer_post_parser = reqparse.RequestParser()
timer_post_parser.add_argument(
    'work_interval',
    type=str,
    required=True,
    location=['json'],
    help='work_interval parameter is required'
)
timer_post_parser.add_argument(
    'rest_interval',
    type=str,
    required=True,
    location=['json'],
    help='rest_interval parameter is required'
)
timer_post_parser.add_argument(
    'sound',
    type=str,
    required=True,
    location=['json'],
    help='sound parameter is required'
)
timer_post_parser.add_argument(
    'mood',
    type=bool,
    required=True,
    location=['json'],
    help='mood parameter is required'
)
timer_post_parser.add_argument(
    'user_id',
    type=int,
    required=True,
    location=['json'],
    help='user_id parameter is required'
)

rest_fields = {
    'id': fields.Integer,
    'mood_rating_1': fields.Integer,
    'mood_rating_2': fields.Integer,
    'content_selected': fields.String,
    'focus_interval': fields.String,
    'rest_interval': fields.String,
    'user_id': fields.Integer
}

rest_list_fields = {
    'count': fields.Integer,
    'rests': fields.List(fields.Nested(rest_fields)),
}

rest_post_parser = reqparse.RequestParser()
rest_post_parser.add_argument(
    'mood_rating_1',
    type=int,
    required=True,
    location=['json'],
    help='init mood parameter is required'
)
rest_post_parser.add_argument(
    'mood_rating_2',
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
rest_post_parser.add_argument(
    'user_id',
    type=int,
    required=True,
    location=['json'],
    help='user_id parameter is required'
)

class UserTimerResource(Resource):
    def get(self, user_id=None):
        if user_id:
            timer = Timer.query.filter_by(user_id=user_id).first()
            return marshal(timer, timer_fields)

    @marshal_with(timer_fields)
    def put(self, user_id=None):
        if user_id:
            existing_timer = Timer.query.filter_by(user_id=user_id).first()
            if existing_timer is None:
                args = timer_post_parser.parse_args()
                timer = Timer(**args)
                db.session.add(timer)
                db.session.commit()
                print ("timer created!")
                return timer
            else:
                print ("a timer already exists for that user...lets update it")
                if 'work_interval' in request.json:
                    existing_timer.work_interval = request.json['work_interval']

                if 'rest_interval' in request.json:
                    existing_timer.rest_interval = request.json['rest_interval']

                if 'sound' in request.json:
                    existing_timer.sound = request.json['sound']

                if 'mood' in request.json:
                    existing_timer.mood = request.json['mood']

                db.session.commit()
                return existing_timer

class UserRestsResource(Resource):
    def get(self, user_id=None, rest_id=None):
        if user_id:
            if rest_id:
                rest = Rest.query.filter_by(user_id=user_id, id=rest_id).first()
                return marshal(rest, rest_fields)
            else:
                args = request.args.to_dict()
                limit = args.get('limit', 0)
                offset = args.get('offset', 0)

                args.pop('limit', None)
                args.pop('offset', None)

                rest = Rest.query.filter_by(user_id=user_id, **args).order_by(Rest.id)
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
    def post(self, user_id=None):
        if user_id:
            args = rest_post_parser.parse_args()

            rest = Rest(**args)
            db.session.add(rest)
            db.session.commit()

            return rest

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

        existing_user = User.query.filter_by(email=args.email).first()
        if existing_user is None:
            user = User(**args)
            db.session.add(user)
            db.session.commit()
            print ("user created!")
            return user
        else:
            print ("a user already exists with that email...")
            return existing_user
