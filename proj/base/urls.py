from django.urls import path, include
from . import views

urlpatterns = [
    path('celery_task_demo', views.celery_task_demo, name='celery_task_demo'),
    path('prod_errorlog', views.prod_errorlog, name='prod_errorlog'),
    path('chat/', include([
        path('global_send', views.chat_global_send, name='chat_global_send'),
        path('', views.chat_index, name='chat_index'),
        path('<str:room_name>', views.chat_room, name='chat_room'),
    ])),
]
