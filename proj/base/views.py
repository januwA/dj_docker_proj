import logging
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import update_last_login
from proj.tasks import add
from asgiref.sync import async_to_sync
from django.shortcuts import render, HttpResponse
from channels.layers import get_channel_layer

from rest_framework import viewsets
from rest_framework import exceptions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.settings import api_settings as sjwt_settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import FileDemo
from .serializers import FileDemoSerializer

# 指定记录器发送日志消息
logger = logging.getLogger('django')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # 在token中添加数据
        # token["username"] = user.username
        return token

    def validate(self, attrs, *args, **kwargs):
        """验证通过后返回token"""
        data = super().validate(attrs)

        # 登录时对用户信息做验证
        # if not self.user.is_email_verified:
        #     raise exceptions.APIException("邮箱未验证")

        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        # 从 SIMPLE_JWT 判断是否更新最后登录时间
        if sjwt_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    """自定义Token声明
    https://django-rest-framework-simplejwt.readthedocs.io/en/latest/customizing_token_claims.html
    """

    serializer_class = MyTokenObtainPairSerializer

    def post(self, request: Request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


def celery_task_demo(request):
    logger.info('发送异步消息')
    add.apply_async(args=(1, 2), ignore_result=False)
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
