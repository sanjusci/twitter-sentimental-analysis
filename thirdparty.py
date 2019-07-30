from flask_sqlalchemy import SQLAlchemy
from celery import Celery

db = SQLAlchemy()
cel = None


def make_celery():
    from settings import app, config
    global cel
    CELERY = config.get("CELERY")
    celery = Celery("twitter", **CELERY)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    if cel is None:
        cel = celery
    return cel

make_celery()