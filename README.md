## Django 开发环境

## 启动
```sh
> docker-compose up
> docker-compose up -d
```

启动时会自动加载 `.env` 文件

## 生产
```sh
$ docker-compose -f docker-compose.yml -f docker-compose.prod.yml up
```

## 在容器内运行脚本
```sh
docker-compose run dj python manage.py startapp base
docker-compose run dj python manage.py makemigrations
docker-compose run dj python manage.py migrate
docker-compose run dj python manage.py createsuperuser
docker-compose run dj python manage.py collectstatic --noinput
docker-compose run nginx nginx -s reload
```

## 查看容器内的logs信息
```sh
$ docker-compose logs
```

使用时去掉`.gitignore`中的`proj/djstatic`配置

## 文件
```
|-- .env                        docker compose 环境变量
|-- .git
|-- .gitignore
|-- app 前端静态文件
|   |-- .gitkeep
|   `-- index.html
|-- docker-compose.override.yml 开发配置
|-- docker-compose.prod.yml     线上配置
|-- docker-compose.yml          基础配置
|-- Dockerfile
|-- nginx                       nginx配置
|   `-- conf.d
|       `-- django.conf        
|-- pgdb                        pgdb配置
|   |-- .gitkeep
|   `-- data
|-- proj                        django项目文件
|-- rabbitmq                    rabbitmq配置
|   |-- .gitkeep
|   |-- conf
|   |   |-- enabled_plugins
|   |   `-- rabbitmq.conf
|   `-- data
|-- README.md
|-- redis                       redis配置
|   |-- .gitkeep
|   |-- conf
|   |   `-- redis.conf
|   `-- data
`-- requirements.txt            django项目依赖
```

## 查看正在运行的容器
```sh
docker-compose ps
```

## 容器关闭和重启
```sh
docker-compose start 
docker-compose stop 
docker-compose restart 

# 停止并删除容器，-v删除卷
docker-compose down -v 
```

## 进入容器
```sh
docker-compose exec dj bash
```

## 将容器文件拷贝到主机
```sh
docker cp 容器id:容器路径 本机路径

docker cp d27a5a75ae54:/var/a.txt ./
```