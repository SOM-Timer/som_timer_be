import unittest
import json
from application import create_app, db
from application.models.rest import Rest


class TestRests(unittest.TestCase):
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

    def test_get_all_rests(self):
        rest1 = Rest(mood_rating_1 = 2, mood_rating_2 = 4, rest_interval='5:00', focus_interval='30:00', content_selected='SOMATIC')
        rest2 = Rest(mood_rating_1 = 4, mood_rating_2 = 5, rest_interval='7:00', focus_interval = '25:00', content_selected='MOVEMENT')
        with self.app.app_context():
            db.session.add(rest1)
            db.session.add(rest2)
            db.session.commit()

        response = self.test_app.get(
            '/api/rests',
            follow_redirects=True
        )

        # Assert response is 200 OK.
        self.assertEquals(response.status, "200 OK")
        payload = json.loads(response.data)
        self.assertEquals(payload['count'], 2)
        self.assertEquals(payload['rests'][0]['mood_rating_1'], 2)
        self.assertEquals(payload['rests'][0]['mood_rating_2'], 4)
        self.assertEquals(payload['rests'][0]['content_selected'], 'SOMATIC')
        self.assertEquals(payload['rests'][0]['focus_interval'], '30:00')
        self.assertEquals(payload['rests'][0]['rest_interval'], '5:00')
        self.assertEquals(payload['rests'][1]['mood_rating_1'], 4)
        self.assertEquals(payload['rests'][1]['mood_rating_2'], 5)
        self.assertEquals(payload['rests'][1]['content_selected'], 'MOVEMENT')
        self.assertEquals(payload['rests'][1]['focus_interval'], '25:00')
        self.assertEquals(payload['rests'][1]['rest_interval'], '7:00')



if __name__ == "__main__":
    unittest.main()
