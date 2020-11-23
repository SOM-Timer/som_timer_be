from application import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String())
    token = db.Column(db.String())

    def __init__(self, user_name, token):
        self.user_name = user_name
        self.token = token

    def __repr__(self):
        return f"<User {self.id}>"

    def delete(self):
        db.session.delete(self)
        db.session.delete(db.session.query(Timer).filter_by(user_id=self.id))
        db.session.delete(db.session.query(Rest).filter_by(user_id=self.id))
        db.session.commit()
