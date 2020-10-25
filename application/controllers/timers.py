
from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from application.models.timer import Timer
from application import db

timer_fields = {
    'id': fields.Integer,
    'work_interval': fields.String,
    'rest_interval': fields.String
}

timer_list_fields = {
    'count': fields.Integer,
    'timers': fields.List(fields.Nested(timer_fields)),
}

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

class TimersResource(Resource):
    def get(self, timer_id=None):
        if timer_id:
            timer = Timer.query.filter_by(id=timer_id).first()
            return marshal(timer, timer_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            timer = Timer.query.filter_by(**args).order_by(Timer.id)
            if limit:
                timer = timer.limit(limit)

            if offset:
                timer = timer.offset(offset)

            timer = timer.all()

            return marshal({
                'count': len(timer),
                'timers': [marshal(t, timer_fields) for t in timer]
            }, timer_list_fields)

    @marshal_with(timer_fields)
    def post(self):
        args = timer_post_parser.parse_args()

        timer = Timer(**args)
        db.session.add(timer)
        db.session.commit()

        return timer

    @marshal_with(timer_fields)
    def put(self, timer_id=None):
        timer = Timer.query.get(timer_id)

        if 'work_interval' in request.json:
            timer.name = request.json['work_interval']

        if 'rest_interval' in request.json:
            timer.description = request.json['rest_interval']

        db.session.commit()
        return timer

    @marshal_with(timer_fields)
    def delete(self, timer_id=None):
        timer = Timer.query.get(timer_id)

        db.session.delete(timer)
        db.session.commit()

        return timer
