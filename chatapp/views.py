from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


@login_required(login_url='/login')
def chat(request):
    frnd_name = request.GET.get('user')
    mychats_data = None
    user_value = request.GET.get('user')
    if frnd_name:
        try:
            frnd_ = User.objects.get(username=frnd_name)
            mychats_data = Mychats.objects.get(me=request.user, frnd=frnd_)
        except (User.DoesNotExist, Mychats.DoesNotExist):
            pass
    
    frnds = User.objects.filter(id__in=Mychats.objects.filter(
        me=request.user).values_list('frnd', flat=True))

    return render(request, 'message.html', {'my': mychats_data, 'chats': mychats_data.chats if mychats_data else None, 'frnds': frnds, "allchat": mychats_data, "user_value": user_value})
