# import unittest
# import json
# from application import create_app, db
# from application.models.timer import Timer
# from application.models.user import User
#
# class TestTimers(unittest.TestCase):
#     def setUp(self):
#         self.app = create_app('testing')
#
#         self.test_app = self.app.test_client()
#         with self.app.app_context():
#             db.create_all()
#
#     def tearDown(self):
#         with self.app.app_context():
#             # drop all tables
#             db.session.remove()
#             db.drop_all()
#
#     def test_get_one_timer(self):
#         timer1 = Timer(work_interval='25:00', rest_interval='5:00', sound='chordCliff', mood=True, user_id=1)
#         with self.app.app_context():
#                 db.session.add(timer1)
#                 db.session.commit()
#
#         response = self.test_app.get(
#             '/api/timers/1',
#             follow_redirects=True
#         )
#
#         self.assertEquals(response.status, "200 OK")
#         payload = json.loads(response.data)
#         self.assertEquals(payload['work_interval'], "25:00")
#         self.assertEquals(payload['rest_interval'], '5:00')
#         self.assertEquals(payload['sound'], 'chordCliff')
#         self.assertEquals(payload['mood'], True)
#         self.assertEquals(payload['user_id'], 1)
#
#     def test_update_timer(self):
#         timer1 = Timer(work_interval='25:00', rest_interval='5:00', sound='chordCliff', mood=False, user_id=1)
#         with self.app.app_context():
#                 db.session.add(timer1)
#                 db.session.commit()
#
#         response = self.test_app.put(
#             '/api/timers/1',
#             json={
#                 "work_interval": "30:00",
#                 "rest_interval": "7:00",
#                 "sound": "chordCliff",
#                 "mood": False,
#                 "user_id": 2
#             },
#             follow_redirects=True
#         )
#
#         self.assertEquals(response.status, "200 OK")
#         payload = json.loads(response.data)
#         self.assertEquals(payload['work_interval'], "30:00")
#         self.assertEquals(payload['rest_interval'], '7:00')
#         self.assertEquals(payload['sound'], 'chordCliff')
#         self.assertEquals(payload['mood'], False)
#         self.assertEquals(payload['user_id'], 2)
#
# if __name__ == "__main__":
#     unittest.main()
