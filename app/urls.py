from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login', login_user, name='login'),
    path('userprofile/',userprofile,name='userprofile'),
    path('logout/',logout_user,name='logout')

]
