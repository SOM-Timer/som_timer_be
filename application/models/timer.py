from application import db

class Timer(db.Model):
    __tablename__ = 'timers'

    id = db.Column(db.Integer, primary_key=True)
    work_interval = db.Column(db.String())
    rest_interval = db.Column(db.String())
    sound = db.Column(db.String())

    def __init__(self, work_interval, rest_interval, sound):
        self.work_interval = work_interval
        self.rest_interval = rest_interval
        self.sound = sound 

    def __repr__(self):
        return f"<Timer {self.id}>"
