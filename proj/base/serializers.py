from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        read_only_fields = ['is_superuser']
        extra_kwargs = {
            'password': {'write_only': True},  # 不返回密码
            'is_active': {'default': True},  # 创建的用户默认激活
        }


class BookSerializer(serializers.ModelSerializer):
    auther__username = serializers.CharField(read_only=True)
    auther_name = serializers.CharField(read_only=True)
    auther = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'auther', 'auther__username', 'auther_name')


class PublisherSerializer(serializers.ModelSerializer):

    # 明确声明 annotate 的聚合字段，然后再 fields 中添加
    num_books = serializers.IntegerField(read_only=True)

    class Meta:
        model = Publisher
        fields = ('id', 'name', 'num_books', 'books')
