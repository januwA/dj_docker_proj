import datetime
import uuid
import os

from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.contrib import admin
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


def my_upload_to(instance, filename):
    uid = uuid.uuid4().hex

    # a.txt => '.txt'
    # a     => ''
    # .txt  => ''
    ext = os.path.splitext(filename)
    return datetime.datetime.now().strftime(f'uploads/%Y/%m/%d/{uid}{ext}')


class FileDemo(models.Model):
    file = models.FileField(
        '文件', upload_to=my_upload_to, null=True, blank=True)
    img = models.ImageField(
        '图片', upload_to=my_upload_to, width_field='image_width', height_field='image_height', null=True, blank=True)
    image_height = models.PositiveSmallIntegerField(
        null=True, blank=True, editable=False, default=100)
    image_width = models.PositiveSmallIntegerField(
        null=True, blank=True, editable=False, default=100)

    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)


class MyUserManager(UserManager):

    def _create_user(self, username, email, password, **extra_fields):

        # 在这里判断必填字段
        if not username:
            raise ValueError("The given username must be set")

        email = self.normalize_email(email)

        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)

        # 创建时必须初始化 REQUIRED_FIELDS 中的字段
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    phone = models.CharField('手机号', max_length=11, validators=[],
                             null=True, blank=True, unique=True)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    # 创建时的必选字段
    REQUIRED_FIELDS = []

    # 如果将邮箱设置为登录名，必须添加唯一限制
    # email = models.EmailField(
    #     verbose_name="账号",
    #     max_length=255,
    #     unique=True,
    # )

    # 如果不在需要 username 字段
    # username = None

    # 修改了必填选项 REQUIRED_FIELDS，必须重写管理器
    objects = MyUserManager()

    @admin.display(description="全名")
    def full_name(self):
        return self.get_full_name()

    class Meta(AbstractUser.Meta):
        verbose_name = "用户"
        verbose_name_plural = "用户列表"
        ordering = ["id"]

    def __str__(self) -> str:
        return self.get_username()
