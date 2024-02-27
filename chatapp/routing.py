from django.urls import path
from .consumers import MychatApp

websocket_urlpatterns =[

    path('chat/msg/ws/wsc/',MychatApp.as_asgi())
]