import os
from pathlib import Path
from celery import Celery

main_name = Path(__file__).parent.name

# 为 'celery' 程序设置默认的 Django 设置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{main_name}.settings')

celery_app = Celery(main_name)

# 加载配置文件
celery_app.config_from_object(f"{main_name}.celeryconfig")

# 从所有注册的 Django 应用程序加载任务模块
celery_app.autodiscover_tasks()