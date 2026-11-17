
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta

from time import sleep

app = Celery(
    main='tasks',
    broker='pyamqp://guest@localhost//',
    backend='db+sqlite:///celery.sqlite',
)

app.conf.beat_schedule = {
    'get-stock-price-every-minute': {
        'task': 'tasks.get_value',
        'schedule': crontab(minute='*'),        
    },
    'get-stock-price-every-minute2': {
        'task': 'tasks.get_value_2',
        'schedule': timedelta(seconds=10),        
    },
}

app.conf.timezone = 'America/Sao_Paulo'


@app.task
def get_value():

    sleep(5)  

    return 'Tarefa executada com sucesso'

@app.task
def get_value_2():

    sleep(5)  

    return 'Tarefa 2 executada com sucesso'