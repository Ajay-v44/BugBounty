from django.shortcuts import render
from .models import *
from app.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


@login_required(login_url='/login')
def chat(request):
    frnd_name = request.GET.get('user')
    mychats_data = None
    user_value = request.GET.get('user')
    usrquery = UserProfile.objects.get(user=request.user)
    if frnd_name:
        try:
            frndquery = UserProfile.objects.get(username=frnd_name)
            frnd_ = User.objects.get(username=frnd_name)
            mychats_data = Mychats.objects.get(me=request.user, frnd=frnd_)
            chatq1=Mychats.objects.get(me=request.user, frnd=frnd_)
            romqM=Rooms.objects.get(chat=chatq1.id)
            chatq2=Mychats.objects.get(me=frnd_, frnd=request.user)
            romqF=Rooms.objects.get(chat=chatq2.id)
        except (User.DoesNotExist, Mychats.DoesNotExist):
            
            pass
    else:
        romqM=romqF=None
        frndquery = None
    
    
    frnds = User.objects.filter(id__in=Mychats.objects.filter(
        me=request.user).values_list('frnd', flat=True))
    return render(request, 'message.html', {'my': mychats_data, 'chats': mychats_data.chats if mychats_data else None, 'frnds': frnds, "allchat": mychats_data, "user_value": user_value, "usrquery": usrquery, "frndquery": frndquery,"romqM":romqM,"romqF":romqF})
