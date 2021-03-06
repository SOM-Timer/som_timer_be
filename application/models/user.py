from application import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self, user_name, email):
        self.user_name = user_name
        self.email = email

    def __repr__(self):
        return f"<User {self.id}>"

    def delete(self):
        ### A chain delete like this is best practice and should work but will take more research
        # db.session.delete(db.session.query(Timer).filter_by(user_id=self.id))
        # db.session.delete(db.session.query(Rest).filter_by(user_id=self.id))
        db.session.delete(self)
        db.session.commit()
