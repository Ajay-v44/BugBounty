from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profilepicture = models.ImageField(
        upload_to='images', height_field=None, width_field=None, max_length=None)
    banner = models.ImageField(
        upload_to='images', height_field=None, width_field=None, max_length=None, blank=True)
    about = models.TextField()
    collabs = models.IntegerField(default=0, null=True, blank=True)
    bugcrowd = models.CharField(max_length=150, blank=True)
    twitter = models.CharField(max_length=150, blank=True)
    fb = models.CharField(max_length=150, blank=True)
    insta = models.CharField(max_length=150, blank=True)
    phone = models.BigIntegerField(blank=True)
