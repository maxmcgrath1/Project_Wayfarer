from asyncio.proactor_events import _ProactorDuplexPipeTransport
from email.mime import image
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
###########################################################################################
###########################################################################################

class City(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    population = models.IntegerField(default=0)
    attractions = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

###########################################################################################
###########################################################################################

class Post(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']

###########################################################################################
###########################################################################################
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.CharField(max_length=250)
