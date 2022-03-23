from rest_framework import serializers

from .models import *


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
        fields = ('id','name','num_books', 'books')
