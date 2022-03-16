# 使用的Debian linux和apt包管理器
# slim-bullseye 相对于 bullseye 镜像大小小了不少
# 但是可能缺少一些系统依赖包需要手动安装
# FROM python:3.10.1-bullseye
FROM python:3.10.2-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 安装需要的依赖包
RUN apt update -y
RUN apt install libpq-dev gcc python3-dev musl-dev -y

WORKDIR /proj

COPY ./proj/* /proj/

# 创建镜像时执行
RUN python -m pip install --upgrade pip
RUN pip install -r /proj/requirements.txt

COPY ./scripts /scripts
RUN chmod 777 /scripts/*