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
    path('createpost/', createPost, name='createpost'),
    path('sentcollabs/<int:id>/', sentCollabarationMessage, name='sentcollabs'),
    path('viewcollabs/', viewCollabs, name='viewcollabs'),
    path('publicprofile/<str:username>/',
         viewPublicProfile, name='publicprofile'),
    path('viewposts/', viewPosts, name='viewposts'),
    path('deletepost/<int:id>/', deletePost, name='deletepost'),
    path('updateposts/<int:id>/', updatePost, name='updateposts'),
    path('mycollabs', myCollabs, name='mycollabs'),
    path('deleetcollabs/<int:id>/', deleteCollabs, name='deleetcollabs'),
    path('updatecollabstatus/<str:status>/<int:id>/',
         updateCollabStatus, name="updatecollabstatus"),
    path('contactus', contactUs, name='contactus'),
    path('page404',page404,name='page404')
]
