# som_timer_be

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
