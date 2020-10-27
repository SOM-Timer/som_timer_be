# som_timer_be

## Endpoints

#### GET '/api/timers/{timer_id}

```
{
    "id": 1,
    "work_interval": "25:00",
    "rest_interval": "5:00"
}
```

#### PUT '/api/timers/{timer_id}

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
