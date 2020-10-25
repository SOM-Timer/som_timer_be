from application import db

class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    duration = db.Column(db.String())
    category = db.Column(db.Enum("Movement", "Meditation", "Somatic", name="exercise_category"), nullable=False, server_default="Somatic")

    def __init__(self, url, duration, category):
        self.url = url
        self.duration = duration
        self.category = category
        
    def __repr__(self):
        return f"<Exercise {self.id}>"
