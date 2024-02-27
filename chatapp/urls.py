from django.urls import path
from .views import *
from .consumers import MychatApp

urlpatterns = [
path('msg/',chat,name='msg'),
path('msg/ws/wsc/', MychatApp.as_asgi()), 

]
