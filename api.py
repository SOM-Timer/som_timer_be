import flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/som_timer"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class TimersModel(db.Model):
    __tablename__ = 'timers'

    id = db.Column(db.Integer, primary_key=True)
    work_interval = db.Column(db.String())
    rest_interval = db.Column(db.String())

    def __init__(self, work_interval, rest_interval):
        self.work_interval = work_interval
        self.rest_interval = rest_interval

    def __repr__(self):
        return f"<Timer {self.id}>"

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/jsonify/', methods=['GET'])
def jsonify():
    return flask.jsonify({'username': 'yxr'})

app.run()
