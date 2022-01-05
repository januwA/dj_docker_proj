# 使用的Debian linux和apt包管理器
FROM python:3.10.1-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /proj

COPY ./requirements.txt /

# 创建镜像时执行
RUN pip install -r /requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY ./proj/* /proj/

COPY ./scripts /scripts
RUN chmod 777 /scripts/*