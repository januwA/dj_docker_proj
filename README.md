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