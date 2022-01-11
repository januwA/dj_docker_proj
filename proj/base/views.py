import logging
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from proj.tasks import add
from asgiref.sync import async_to_sync
from django.shortcuts import render, HttpResponse
from channels.layers import get_channel_layer

from rest_framework import viewsets
from .models import FileDemo
from .serializers import FileDemoSerializer

# 指定记录器发送日志消息
logger = logging.getLogger('django')


def celery_task_demo(request):
    logger.info('发送异步消息')
    add.apply_async(args=(1, 2))
    return HttpResponse('ok')


def chat_index(request):
    return render(request, 'base/index.html')


def chat_room(request, room_name):
    return render(request, 'base/room.html', {
        'room_name': room_name
    })


def chat_global_send(request):
    logger.info('发送全局socket消息')
    channel_layer = get_channel_layer()
    # 如果要向所有房间发送消息，则创建房间时需要存入数据库
    async_to_sync(channel_layer.group_send)("chat_a", {
        'type': 'chat_message',
        'message': 'chat_a 房间所有用户将会收到消息'
    })
    return HttpResponse('已发送全局消息')


def prod_errorlog(request):
    logger.error('记录错误消息')
    return HttpResponse('ok')


class FileDemoViewSet(viewsets.ModelViewSet):
    queryset = FileDemo.objects.all()
    serializer_class = FileDemoSerializer
