# Som Timer Backend 

See [Som Timer Frontend](https://github.com/SOM-Timer/som_timer_fe) for more information on general functionality. 

## Overview
Tech stack: [Python3.9](https://www.python.org/downloads/) on [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/)
Testing: UnitTest 

Endpoints built out to deliver timer and exercise content to a user in order to deliver a guided interval work/rest experience. 

## Setup 
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

## Endpoints

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

#### GET  '/api/rand_exercises'

```
#REQUEST BODY
duration options are 5:00, 7:00, 10:00
category options are SOMATIC, MOVEMENT, MEDITATION
{
    "duration": "5:00",
    "category": "SOMATIC"
}

#RESPONSE BODY
{
    "id": 21,
    "url": "http://www.youtube.com/superrelaxinvibes",
    "duration": "5:00",
    "category": "SOMATIC"
}
```
