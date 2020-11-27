import unittest
import json
from application import create_app, db


class TestDocumentation(unittest.TestCase):
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

    def test_documentation_page(self):

        response = self.test_app.get(
            '/',
            follow_redirects=True
        )

        self.assertEquals(response.status, "200 OK")

        html = response.data.decode()
        assert "Som Timer Endpoints" in html
        assert "GET  '/api/users/:user_id/timer'" in html
        assert "PUT  '/api/users/:user_id/timer'" in html
        assert "GET  '/api/rand_exercise'" in html
        assert "GET  '/api/users/:user_id/rests'" in html
        assert "POST  '/api/users/:user_id/rests'" in html
        assert "GET  '/api/users'" in html
        assert "GET  '/api/users/:user_id'" in html
        assert "POST  '/api/users'" in html

if __name__ == "__main__":
    unittest.main()
