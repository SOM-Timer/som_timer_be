from application import db
from enum import Enum, auto

class SomaticCategory(Enum):
    MOVEMENT = auto()
    MEDITATION = auto()
    SOMATIC = auto()

class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    duration = db.Column(db.String())
    category = db.Column(db.Enum(SomaticCategory))

    def __init__(self, url, duration, category):
        self.url = url
        self.duration = duration
        self.category = category

    def __repr__(self):
        return f"<Exercise {self.id}>"
