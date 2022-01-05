import datetime
import uuid

from django.db import models


def my_upload_to(instance, filename):
    uid = uuid.uuid4().hex
    ext = filename.split('.')[-1]
    return datetime.datetime.now().strftime(f'uploads/%Y/%m/%d/{uid}.{ext}')


class FileDemo(models.Model):
    file = models.FileField(
        '文件', upload_to=my_upload_to, null=True, blank=True)
    img = models.ImageField(
        '图片', upload_to=my_upload_to, width_field='image_width', height_field='image_height', null=True, blank=True)
    image_height = models.PositiveSmallIntegerField(
        null=True, blank=True, editable=False, default=100)
    image_width = models.PositiveSmallIntegerField(
        null=True, blank=True, editable=False, default=100)
