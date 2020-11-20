import unittest
import json
from application import create_app, db
from application.models.user import User


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
        user1 = User(user_name="Princess.Kopf", token="token1")
        user2 = User(user_name="ABD", token="token2")
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
        self.assertEquals(payload['users'][0]['user_name'], "Princess.Kopf")
        self.assertEquals(payload['users'][0]['token'], "token1")
        self.assertEquals(payload['users'][1]['user_name'], "ABD")
        self.assertEquals(payload['users'][1]['token'], "token2")

    def test_get_user_by_id(self):
        user1 = User(user_name="Princess.Kopf", token="token1")
        user2 = User(user_name="ABD", token="token2")
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
        self.assertEquals(payload['user_name'], "Princess.Kopf")
        self.assertEquals(payload['token'], "token1")

    def test_create_user(self):

        response = self.test_app.post(
            '/api/users',
            json={
                "user_name": "Rachel Williams",
                "token": "token3",
            },
            follow_redirects=True
        )

        self.assertEquals(response.status, "200 OK")
        payload = json.loads(response.data)
        self.assertEquals(payload['user_name'], "Rachel Williams")
        self.assertEquals(payload['token'], "token3")

if __name__ == "__main__":
    unittest.main()
