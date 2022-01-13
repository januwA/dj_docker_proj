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