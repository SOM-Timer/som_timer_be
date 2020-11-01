from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from application.models.timer import Timer
from application import db

timer_fields = {
    'id': fields.Integer,
    'work_interval': fields.String,
    'rest_interval': fields.String,
    'sound': fields.String
}

timer_list_fields = {
    'count': fields.Integer,
    'timers': fields.List(fields.Nested(timer_fields)),
}

class TimersResource(Resource):
    def get(self, timer_id=None):
        if timer_id:
            timer = Timer.query.filter_by(id=timer_id).first()
            return marshal(timer, timer_fields)

    @marshal_with(timer_fields)
    def put(self, timer_id=None):
        timer = Timer.query.get(timer_id)

        if 'work_interval' in request.json:
            timer.work_interval = request.json['work_interval']

        if 'rest_interval' in request.json:
            timer.rest_interval = request.json['rest_interval']

        if 'sound' in request.json:
            timer.sound = request.json['sound']

        db.session.commit()
        return timer
