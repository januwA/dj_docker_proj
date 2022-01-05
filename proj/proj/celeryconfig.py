import datetime
import os
from pathlib import Path

main_name = Path(__file__).parent.name

# 使用 RabbitMQ 作为消息代理人
broker_url = f"amqp://{os.environ.get('RABBITMQ_USER')}:{os.environ.get('RABBITMQ_PASS')}@somerabbitmq:{os.environ.get('RABBITMQ_PORT')}//"

# 使用 Redis 作为结果后端
result_backend = f'redis://someredis:{os.environ.get("REDIS_PORT")}/0'


# 工作线程启动时要导入的模块序列
# 调用了 celery_app.autodiscover_tasks() 可以忽略这个配置
# imports = (f"{main_name}.tasks",)

# 此设置可用于重写配置中的任何任务属性
# task_annotations = {
#   "tasks.add": {"rate_limit": "10/s"}
# }

# 定期删除储存的结果
result_expires = datetime.timedelta(hours=6)

timezone = "Asia/Shanghai"
