from django.urls import re_path, include
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from . import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"files/?", views.FileDemoViewSet)

urlpatterns = [
    re_path(r"token/?", views.MyTokenObtainPairView.as_view(),
            name="token_obtain_pair"),
    re_path(r"token/refresh/?", TokenRefreshView.as_view(), name="token_refresh"),


    re_path(r'celery_task_demo/?', views.celery_task_demo,
            name='celery_task_demo'),
    re_path(r'prod_errorlog/?', views.prod_errorlog, name='prod_errorlog'),
    re_path(r'chat/?', include([
        re_path(r'global_send/?', views.chat_global_send,
                name='chat_global_send'),
        re_path('', views.chat_index, name='chat_index'),
        re_path(r'<str:room_name>/?', views.chat_room, name='chat_room'),
    ])),
    re_path("", include(router.urls)),

]
