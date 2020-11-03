from flask import Flask, jsonify, request
from application import create_app, db
from application.models.exercise import Exercise
from application.models.timer import Timer
from application.models.rest import Rest
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, create_engine
import os
from sqlalchemy.orm import sessionmaker

app = create_app("development")
db = SQLAlchemy(app)

@app.cli.command('db_reset')
def db_reset():
    exercises = Exercise.query.all()
    for exercise in exercises:
        Exercise.delete(exercise)

    timers = Timer.query.all()
    for timer in timers:
        Timer.delete(timer)

    rests = Rest.query.all()
    for rest in rests:
        Rest.delete(rest)

@app.cli.command('db_seed')
def db_seed():

    #Seed Array
    Seeds = []

    #MEDITATION
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=W5wqniA4MMc&ab_channel=EssentialSomatics', duration='10:00', category='MEDITATION'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=O-6f5wQXSu8&ab_channel=Goodful', duration='10:00', category='MEDITATION'))
    Seeds.append(Exercise(url='https://soundcloud.com/ucsdmindfulness/allowing-emotions?in=ucsdmindfulness/sets/mpeak', duration='10:00', category='MEDITATION'))
    Seeds.append(Exercise(url='https://soundcloud.com/ucsdmindfulness/mpeak-10-min-awareness-of-breath-meditation-by-corrie-falcon?in=ucsdmindfulness/sets/mpeak', duration='10:00', category='MEDITATION'))
    Seeds.append(Exercise(url='https://soundcloud.com/ucsdmindfulness/mpeak-10-min-awareness-of-breath-by-pete-kirchmer', duration='10:00', category='MEDITATION'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=ZLWmNgy7VaM&ab_channel=ChiropractorByronBayAndrewBadmanWaveofLife', duration='7:00', category='MEDITATION'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=0oz5aEmScms&ab_channel=KristenMartin', duration='7:00', category='MEDITATION'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=1MGgK8eulKo', duration='7:00', category='MEDITATION'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=cFeCUfw657g', duration='7:00', category='MEDITATION'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=inpok4MKVLM&ab_channel=Goodful', duration='5:00', category='MEDITATION'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=L1QOh-n-eus&ab_channel=TheHonestGuys-Meditations-Relaxation', duration='5:00', category='MEDITATION'))
    Seeds.append(Exercise(url='https://soundcloud.com/ucsdmindfulness/mpeak-5-min-open-awareness-meditation-by-pete-kirchmer', duration='5:00', category='MEDITATION'))
    Seeds.append(Exercise(url='https://soundcloud.com/ucsdmindfulness/5-min-checkin-by-christy-cassisa', duration='5:00', category='MEDITATION'))
    Seeds.append(Exercise(url='https://soundcloud.com/ucsdmindfulness/five-minute-mindful-moment', duration='5:00', category='MEDITATION'))

    #MOVEMENT
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=A0pkEgZiRG4&ab_channel=YogaWithBird', duration='10:00', category='MOVEMENT'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=KJaWIBg15n0&ab_channel=ExtremeFitnessPro', duration='10:00', category='MOVEMENT'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=_0xZ3iOswYM', duration='10:00', category='MOVEMENT'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=VaoV1PrYft4', duration='10:00', category='MOVEMENT'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=3Ql411IIpJM&ab_channel=YogaWithAdriene', duration='7:00', category='MOVEMENT'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=BO2YOk4817s&ab_channel=PilatesByLisa', duration='7:00', category='MOVEMENT'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=4C-gxOE0j7s', duration='7:00', category='MOVEMENT'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=LI9upn4t9n8', duration='7:00', category='MOVEMENT'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=jOfshreyu4w', duration='7:00', category='MOVEMENT'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=d8QqXLV3tWM&ab_channel=RosalieYoga', duration='5:00', category='MOVEMENT'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=BsxBfhs0Qjc&ab_channel=JennyFord', duration='5:00', category='MOVEMENT'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=3wjuDki_zos', duration='5:00', category='MOVEMENT'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=CVzshj3GKLg', duration='5:00', category='MOVEMENT'))

    #SOMATIC
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=dsmfIAyiois', duration='5:00', category='SOMATIC'))
    Seeds.append(Exercise(url='https://soundcloud.com/ucsdmindfulness/mpeak-5-min-body-scan-by-pete-kirchmer', duration='5:00', category='SOMATIC'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=Eum8DTvsRkI', duration='7:00', category='SOMATIC'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=1saZqSr2zGM', duration='7:00', category='SOMATIC'))
    Seeds.append(Exercise(url='https://soundcloud.com/ucsdmindfulness/10-min-body-scan-by-christy-cassisa?in=ucsdmindfulness/sets/short-meditation-sessions', duration='10:00', category='SOMATIC'))
    Seeds.append(Exercise(url='https://www.youtube.com/watch?v=zsCVqFr6j1g&feature=emb_logo', duration='10:00', category='SOMATIC'))

    #Default Timer
    Seeds.append(Timer(work_interval='25:00', rest_interval='5:00', sound='chordCliff'))

    for x in Seeds:
        db.session.add(x)

    db.session.commit()
    print('Database Seeded!')
