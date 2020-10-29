# Som Timer Backend 

See [Som Timer Frontend](https://github.com/SOM-Timer/som_timer_fe) for more information!

## Overview:
Tech stack: [Python3.9](https://www.python.org/downloads/) on [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/)</br>
Testing: UnitTest </br>
Functionality: timer and exercise endpoints built to deliver a guided interval work/rest experience.  </br>

## Learning Goals: 
- Ultimately, demonstrate knowledge you’ve gained throughout Turing
- Use an agile process to turn well defined requirements into deployed and production ready software
- Gain experience dividing applications into components and domains of responsibilities to facilitate multi-developer teams. Service oriented architecture concepts and patterns are highly encouraged.
- Explore and implement new concepts, patterns, or libraries that have not been explicitly taught while at Turing
- Practice an advanced, professional git workflow (see whole-team expectations)
- Gain more experience using continuous integration tools to build and automate the deployment of features in various environments
- Build applications that execute in development, test, CI, and production environments
- Focus on communication between front-end and back-end teams in order to complete and deploy features that have been outlined by the project spec
- At least 25% test coverage 
- Successfully implement a new framework (flask) and a new language (python) 

## Setup:
```
    clone and setup locally 
# enter the virtual enviroment 
    $ . venv/bin/activate 
# install requirements 
    $ pip install -r requirements.txt 
# create and configure database 
    $ createdb som_timer 
    $ export DATABASE_URL=postgresql://localhost:5432/som_timer
# migrate database 
    $ python manage.py db init
    $ python manage.py db migrate 
    $ python manage.py db upgrade 
# seed database 
    $ flask db_seed 
```

#### Running the app:
Command: 
``` 
$ python run.py 
```
Port: `http://localhost:5000` </br>

## Testing: 
To run tests: 
```
$ nosetests
```
To run tests and produce a coverage report: 
```
$ coverage run --omit 'venv/*' -m nose 
$ coverage report -m
```

## Endpoints:

#### GET  '/api/timers/{timer_id}

```
#RESPONSE
{
    "id": 1,
    "work_interval": "25:00",
    "rest_interval": "5:00"
}
```

#### PUT  '/api/timers/{timer_id}

```
#REQUEST BODY
{
    "work_interval": "30:00",
    "rest_interval": "7:00"
}

#RESPONSE
{
    "id": 1,
    "work_interval": "30:00",
    "rest_interval": "7:00"
}
```

#### GET  '/api/rand_exercise'

```
#QUERY PARAMS
* Required
EX: '<root_path>/api/rand_exercise?duration=10:00&category=SOMATIC'

* duration = 5:00, 7:00, 10:00
* category = SOMATIC, MOVEMENT, MEDITATION

#RESPONSE BODY
{
    "id": 21,
    "url": "http://www.youtube.com/superrelaxinvibes",
    "duration": "5:00",
    "category": "SOMATIC"
}
```

## Tools:
- Python3.9 
- Flask 
- Unittest 
- SQLAlchemy 
- Postgres

## Authors:
[Dorion](https://github.com/sciencefixion) </br>
[Chandler Hulstrom](https://github.com/Chulstro) </br>
[Sienna Kopf](https://github.com/sienna-kopf)
