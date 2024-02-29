from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import uuid
import datetime


class Mychats(models.Model):
    me = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='it_me')
    frnd = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='my_frnd')
    chats = models.JSONField(default=dict)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now_add=True)


class Rooms(models.Model):
    chat = models.ForeignKey(Mychats, on_delete=models.CASCADE)
    uniqueid = models.CharField(max_length=150, unique=True)
    username=models.CharField( max_length=150)

    def save(self, *args, **kwargs):
        unique_id = uuid.uuid4()
        current_time = datetime.datetime.now()
        time_str = current_time.strftime("%Y%m%d%H%M%S%f")
        combined_id = str(unique_id) + time_str
        self.uniqueid = combined_id
        super(Rooms, self).save(*args, **kwargs)
