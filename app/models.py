from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username=models.CharField( max_length=150)
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


class Posts(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    tags = models.CharField(max_length=150, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'tags', 'user', 'date')
    search_fields = ['title']
    list_filter = ['title']


class collaborate(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()


@admin.register(collaborate)
class collaborateAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'description')
