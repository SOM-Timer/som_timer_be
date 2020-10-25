import unittest
import json
from application import create_app, db
from application.models.timer import Timer


class TestTimers(unittest.TestCase):
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

    def test_get_all_timers(self):
        timer1 = Timer(work_interval='25:00', rest_interval='5:00')
        timer2 = Timer(work_interval='45:00', rest_interval='15:00')
        with self.app.app_context():
            db.session.add(timer1)
            db.session.add(timer2)
            db.session.commit()

        # create a user
        response = self.test_app.get(
            '/api/timers',
            follow_redirects=True
        )

        # Assert response is 200 OK.
        self.assertEquals(response.status, "200 OK")
        payload = json.loads(response.data)
        self.assertEquals(payload['count'], 2)
        self.assertEquals(payload['timers'][0]['work_interval'], '25:00')
        self.assertEquals(payload['timers'][0]['rest_interval'], '5:00')
        self.assertEquals(payload['timers'][1]['work_interval'], '45:00')
        self.assertEquals(payload['timers'][1]['rest_interval'], '15:00')

    def test_create_timer(self):
        response = self.test_app.post(
            '/api/timers',
            json={
                'work_interval': '30:00',
                'rest_interval': '10:00'
            },
            follow_redirects=True
        )

        # Assert response is 200 OK.
        self.assertEquals(response.status, "200 OK")
        payload = json.loads(response.data)
        self.assertEquals(payload['work_interval'], "30:00")
        self.assertEquals(payload['rest_interval'], '10:00')


if __name__ == "__main__":
    unittest.main()
