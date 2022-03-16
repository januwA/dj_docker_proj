# 使用的Debian linux和apt包管理器
FROM python:3.10.1-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /proj

COPY ./proj/* /proj/

# 创建镜像时执行
RUN python -m pip install --upgrade pip
RUN pip install -r /proj/requirements.txt

COPY ./scripts /scripts
RUN chmod 777 /scripts/*