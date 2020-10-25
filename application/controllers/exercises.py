from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from application.models.exercise1 import Exercise
from application import db

exercise_fields = {
    'id': fields.Integer,
    'url': fields.String,
    'duration': fields.String,
    'category': fields.Enum
}

exercise_list_fields = {
    'count': fields.Integer,
    'exercises': fields.List(fields.Nested(exercise_fields)),
}

exercise_post_parser = reqparse.RequestParser()
exercise_post_parser.add_argument(
    'url',
    type=str,
    required=True,
    location=['json'],
    help='url parameter is required'
)
exercise_post_parser.add_argument(
    'duration',
    type=str,
    required=True,
    location=['json'],
    help='duration parameter is required'
)
exersise_post_parser.add_argument(
    'category',
    type=str,
    required=True,
    location=['json'],
    help='category parameter is required'
)

class ExercisesResource(Resource):
    def get(self, exercise_id=None):
        if exercise_id:
            exercise = Exercise.query.filter_by(id=exercise_id).first()
            return marshal(exercise, exercise_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            exercise = Exercise.query.filter_by(**args).order_by(Exercise.id)
            if limit:
                exercise = exercise.limit(limit)

            if offset:
                exercise = exercise.offset(offset)

            exercise = exercise.all()

            return marshal({
                'count': len(exercise),
                'exercises': [marshal(t, exercise_fields) for t in exercise]
            }, exercise_list_fields)

    @marshal_with(exercise_fields)
    def post(self):
        args = exercise_post_parser.parse_args()

        exercise = Exercise(**args)
        db.session.add(exercise)
        db.session.commit()

        return exercise

    @marshal_with(exercise_fields)
    def put(self, exercise_id=None):
        exercise = Exercise.query.get(exercise_id)

        if 'url' in request.json:
            exercise.url = request.json['url']

        if 'duration' in request.json:
            exercise.duration = request.json['duration']

        if 'category' in request.json:
            exercise.category = request.json['category']

        db.session.commit()
        return exercise

    @marshal_with(exercise_fields)
    def delete(self, exercise_id=None):
        exercise = Exercise.query.get(exercise_id)

        db.session.delete(exercise)
        db.session.commit()

        return exercise
