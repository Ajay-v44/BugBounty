from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login', login_user, name='login'),
    path('userprofile/', user_profile, name='userprofile'),
    path('logout/', logout_user, name='logout'),
    path('addprofile/', addUserProfile, name='addprofile'),
    path('updateprofile/', updateUserProfile, name='updateprofile'),
    path('createpost/',createPost,name='createpost'),
    path('sentcollabs/<int:id>/',sentCollabarationMessage,name='sentcollabs'),
    path('viewcollabs/',viewCollabs,name='viewcollabs')

]
