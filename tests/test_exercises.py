import unittest
import json
from application import create_app, db
from application.models.exercise import Exercise


class TestExercises(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.test_app = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

    def test_get_all_exercises(self):
        exercise1 = Exercise(url='https://youtube.com', duration='5:00', category='SOMATIC')
        exercise2 = Exercise(url='https://vimeo.com', duration='15:00', category='MOVEMENT')
        with self.app.app_context():
            db.session.add(exercise1)
            db.session.add(exercise2)
            db.session.commit()

        # create a user
        response = self.test_app.get(
            '/api/exercises',
            follow_redirects=True
        )

        # Assert response is 200 OK.
        self.assertEquals(response.status, "200 OK")
        payload = json.loads(response.data)
        self.assertEquals(payload['count'], 2)
        self.assertEquals(payload['exercises'][0]['url'], 'https://youtube.com')
        self.assertEquals(payload['exercises'][0]['duration'], '5:00')
        self.assertEquals(payload['exercises'][0]['category'], 'SomaticCategory.SOMATIC')
        self.assertEquals(payload['exercises'][1]['url'], 'https://vimeo.com')
        self.assertEquals(payload['exercises'][1]['duration'], '15:00')
        self.assertEquals(payload['exercises'][1]['category'], 'SomaticCategory.MOVEMENT')

    def test_create_exercise(self):
        response = self.test_app.post(
            '/api/exercises',
            json={
                'url': 'https://youtube.com/somatic',
                'duration': '10:00',
                'category': 'MEDITATION'
            },
            follow_redirects=True
        )

        # Assert response is 200 OK.
        self.assertEquals(response.status, "200 OK")
        payload = json.loads(response.data)
        self.assertEquals(payload['url'], "https://youtube.com/somatic")
        self.assertEquals(payload['duration'], '10:00')
        self.assertEquals(payload['category'], 'SomaticCategory.MEDITATION')


if __name__ == "__main__":
    unittest.main()
