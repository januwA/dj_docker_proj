from rest_framework import serializers

from .models import FileDemo


class FileDemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileDemo
        fields = "__all__"
