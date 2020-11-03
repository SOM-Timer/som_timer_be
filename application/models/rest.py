from application import db

class Rest(db.Model):
    __tablename__ = 'rests'

    id = db.Column(db.Integer, primary_key=True)
    mood_rating_1 = db.Column(db.Integer)
    mood_rating_2 = db.Column(db.Integer)
    content_selected = db.Column(db.String())
    focus_interval = db.Column(db.String())
    rest_interval = db.Column(db.String())

    def __init__(self, mood_rating_1, mood_rating_2, content_selected, focus_interval, rest_interval):
        self.mood_rating_1 = mood_rating_1
        self.mood_rating_2 = mood_rating_2
        self.content_selected = content_selected
        self.focus_interval = focus_interval
        self.rest_interval = rest_interval

    def __repr__(self):
        return f"<Rest {self.id}>"

    def delete(self):
        db.session.delete(self)
        db.session.commit()
