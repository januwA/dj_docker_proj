from .celery import celery_app

@celery_app.task(bind=True)
def add(self, x, y):
    return x + y