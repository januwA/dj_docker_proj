from .celery import celery_app


# 这将确保在 Django 启动时始终导入该应用程序，以便 shared_task 将使用该应用程序
__all__ = ('celery_app',)