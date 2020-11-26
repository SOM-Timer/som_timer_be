import unittest
import json
from application import create_app, db
from application.models.user import User
from application.models.timer import Timer
from application.models.rest import Rest


class TestUsers(unittest.TestCase):
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

    def test_get_all_users(self):
        user1 = User(uid=123456, user_name="Princess.Kopf", token="token1")
        user2 = User(uid=654321, user_name="ABD", token="token2")
        with self.app.app_context():
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()

        response = self.test_app.get(
            '/api/users',
            follow_redirects=True
        )

        # Assert response is 200 OK.
        self.assertEquals(response.status, "200 OK")
        payload = json.loads(response.data)
        self.assertEquals(payload['count'], 2)
        self.assertEquals(payload['users'][0]['uid'], 123456)
        self.assertEquals(payload['users'][0]['user_name'], "Princess.Kopf")
        self.assertEquals(payload['users'][0]['token'], "token1")
        self.assertEquals(payload['users'][1]['uid'], 654321)
        self.assertEquals(payload['users'][1]['user_name'], "ABD")
        self.assertEquals(payload['users'][1]['token'], "token2")

    def test_get_user_by_id(self):
        user1 = User(uid=123456, user_name="Princess.Kopf", token="token1")
        user2 = User(uid=654321, user_name="ABD", token="token2")
        with self.app.app_context():
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()

        response = self.test_app.get(
            '/api/users/1',
            follow_redirects=True
        )

        # Assert response is 200 OK.
        self.assertEquals(response.status, "200 OK")
        payload = json.loads(response.data)
        self.assertEquals(payload['uid'], 123456)
        self.assertEquals(payload['user_name'], "Princess.Kopf")
        self.assertEquals(payload['token'], "token1")

    def test_create_user(self):

        response = self.test_app.post(
            '/api/users',
            json={
                "uid": 987654,
                "user_name": "Rachel Williams",
                "token": "token3",
            },
            follow_redirects=True
        )

        self.assertEquals(response.status, "200 OK")
        payload = json.loads(response.data)
        self.assertEquals(payload['uid'], 987654)
        self.assertEquals(payload['user_name'], "Rachel Williams")
        self.assertEquals(payload['token'], "token3")

    def test_creating_a_user_creates_associated_default_timer(self):

        self.test_app.post(
            '/api/users',
            json={
                "uid": 123456,
                "user_name": "Sienna Kopf",
                "token": "token5",
            },
            follow_redirects=True
        )

        response = self.test_app.get(
            '/api/users/1/timer',
            json={
                "id": 1,
                "work_interval": "25:00",
                "rest_interval": "5:00",
                "sound": "reverbSplash",
                "mood": True,
                "user_id": 1
            }
        )

        self.assertEquals(response.status, "200 OK")
        payload = json.loads(response.data)
        self.assertEquals(payload['id'], 1)
        self.assertEquals(payload['work_interval'], "25:00")
        self.assertEquals(payload['rest_interval'], '5:00')
        self.assertEquals(payload['sound'], 'reverbSplash')
        self.assertEquals(payload['mood'], True)
        self.assertEquals(payload['user_id'], 1)

    def test_no_user_creation_on_uid_match(self):

        self.test_app.post(
            '/api/users',
            json={
                "uid": 987654,
                "user_name": "Rachel Williams",
                "token": "token3",
            },
            follow_redirects=True
        )

        response = self.test_app.post(
            '/api/users',
            json={
                "uid": 987654,
                "user_name": "RW",
                "token": "token4",
            },
            follow_redirects=True
        )

        self.assertEquals(response.status, "200 OK")
        payload = json.loads(response.data)
        self.assertEquals(payload['uid'], 987654)
        self.assertEquals(payload['user_name'], "Rachel Williams")
        self.assertEquals(payload['token'], "token3")

    # def test_get_timer_for_user(self): ## WORKS IN POSTMAN
    #     user1 = User(uid=123456, user_name="Princess.Kopf", token="token1")
    #     timer1 = Timer(work_interval='25:00', rest_interval='5:00', sound='chordCliff', mood=False, user_id=user1.id)
    #     with self.app.app_context():
    #             db.session.add(user1)
    #             db.session.commit()
    #
    #     response = self.test_app.get(
    #         '/api/users/1/timer',
    #         follow_redirects=True
    #     )
    #
    #     self.assertEquals(response.status, "200 OK")
    #     payload = json.loads(response.data)
    #     self.assertEquals(payload['id'], 1)
    #     self.assertEquals(payload['work_interval'], "25:00")
    #     self.assertEquals(payload['rest_interval'], "5:00")
    #     self.assertEquals(payload['sound'], "chordCliff")
    #     self.assertEquals(payload['mood'], False)
    #     self.assertEquals(payload['user_id'], 1)

    # def test_get_rests_for_user(self): ## WORKS IN POSTMAN
    #     user1 = User(uid=123456, user_name="Princess.Kopf", token="token1")
    #     rest1 = Rest(mood_rating_1 = 2, mood_rating_2 = 4, rest_interval='5:00', focus_interval='30:00', content_selected='SOMATIC', user_id=user1.id)
    #     rest2 = Rest(mood_rating_1 = 4, mood_rating_2 = 5, rest_interval='7:00', focus_interval = '25:00', content_selected='MOVEMENT', user_id=user1.id)
    #     with self.app.app_context():
    #             db.session.add(user1)
    #             db.session.commit()
    #
    #     response = self.test_app.get(
    #         '/api/users/1/rests',
    #         follow_redirects=True
    #     )
    #
    #     self.assertEquals(response.status, "200 OK")
    #     payload = json.loads(response.data)
    #     self.assertEquals(payload['count'], 2)
    #     self.assertEquals(payload['rests'][0]['mood_rating_1'], 2)
    #     self.assertEquals(payload['rests'][0]['mood_rating_2'], 4)
    #     self.assertEquals(payload['rests'][0]['content_selected'], 'SOMATIC')
    #     self.assertEquals(payload['rests'][0]['focus_interval'], '30:00')
    #     self.assertEquals(payload['rests'][0]['rest_interval'], '5:00')
    #     self.assertEquals(payload['rests'][0]['user_id'], 1)
    #     self.assertEquals(payload['rests'][1]['mood_rating_1'], 4)
    #     self.assertEquals(payload['rests'][1]['mood_rating_2'], 5)
    #     self.assertEquals(payload['rests'][1]['content_selected'], 'MOVEMENT')
    #     self.assertEquals(payload['rests'][1]['focus_interval'], '25:00')
    #     self.assertEquals(payload['rests'][1]['rest_interval'], '7:00')
    #     self.assertEquals(payload['rests'][1]['user_id'], 1)

if __name__ == "__main__":
    unittest.main()
