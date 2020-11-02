from application import db

class Rest(db.Model):
    __tablename__ = 'rests'

    id = db.Column(db.Integer, primary_key=True)
    init_mood = db.Column(db.Integer)
    end_mood = db.Column(db.Integer)
    content_selected = db.Column(db.String())
    focus_interval = db.Column(db.String())
    rest_interval = db.Column(db.String())

    def __init__(self, init_mood, end_mood, content_selected, focus_interval, rest_interval):
        self.init_mood = init_mood
        self.end_mood = end_mood
        self.content_selected = content_selected
        self.focus_interval = focus_interval
        self.rest_interval = rest_interval

    def __repr__(self):
        return f"<Rest {self.id}>"

    def delete(self):
        db.session.delete(self)
        db.session.commit()
