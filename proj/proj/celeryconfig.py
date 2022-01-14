# Celery 配置: https://docs.celeryproject.org/en/stable/userguide/configuration.html
# Task 配置: https://docs.celeryproject.org/en/stable/reference/celery.app.task.html
#
# 通常以 `task_` 开始的配置，都可以在`app.task`中重写，假如配置文件中`task_serializer = 'json'`，
# 在创建任务时可以重写成`@app.task(serializer = 'json')`
#
# 配置选项优先级:
# 执行配置 > 任务配置 > 全局配置

import datetime
import os
from pathlib import Path

main_name = Path(__file__).parent.name

# 使用 RabbitMQ 作为消息代理人
broker_url = f"amqp://{os.environ.get('RABBITMQ_USER')}:{os.environ.get('RABBITMQ_PASS')}@rabbitmq:{os.environ.get('RABBITMQ_PORT')}//"

# 使用 Redis 作为结果后端
result_backend = f'redis://redis:{os.environ.get("REDIS_PORT")}/15'


# 工作线程启动时要导入的模块序列
# 调用了 celery_app.autodiscover_tasks() 可以忽略这个配置
# imports = (f"{main_name}.tasks",)

# 此设置可用于重写配置中的任何任务属性
# task_annotations = {
#   "tasks.add": {"rate_limit": "10/s"}
# }

# 定期删除储存的结果
result_expires = datetime.timedelta(hours=6)

# 配置 Celery 以使用自定义时区
timezone = "Asia/Shanghai"
enable_utc = False

# 应许哪些类型序列化的白名单配置
accept_content = ['json']

# 消息序列化
task_serializer = 'json'

# 结果序列化
result_serializer = 'json'

# 全局禁用结果,如果要忽略可以为task单独配置
task_ignore_result = False

# 以秒为单位的任务硬时间限制,超过此值时，处理任务的工作人员将被杀死并用新的工作人员替换
# 硬超时不可捕获，强制终止任务
# task_time_limit = 3

# 以秒为单位的任务软时间限制 超过此值时将引发 SoftTimeLimitExceeded 异常
# 软时间限制允许任务捕获异常，以便在终止之前进行清理
# task_soft_time_limit = 3
