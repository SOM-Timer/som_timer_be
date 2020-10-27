from flask import Flask, jsonify, request
from application import create_app, db
from application.models.exercise import Exercise
from application.models.timer import Timer
from flask_sqlalchemy import SQLAlchemy
import os

app = create_app("development")
db = SQLAlchemy(app)

@app.cli.command('db_seed')
def db_seed():
    exercise1 = Exercise(url='https://www.youtube.com/watch?v=W5wqniA4MMc&ab_channel=EssentialSomatics', duration='10:00', category='MEDITATION')
    exercise2 = Exercise(url='https://www.youtube.com/watch?v=_0xZ3iOswYM', duration='10:00', category='MOVEMENT')

    timer1 = Timer(work_interval='25:00', rest_interval='5:00')

    db.session.add(exercise1)
    db.session.add(exercise2)
    db.session.add(timer1)
    db.session.commit()
    print('Database Seeded!')
