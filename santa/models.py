from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=150)
    creator = models.ForeignKey(User)
    is_fixed = models.BooleanField()
    date_to_public = models.DateTimeField()


class Member(models.Model):
    name = models.CharField(max_length=150)
    room = models.ForeignKey(Room)
    number = models.IntegerField()
    gift_to = models.IntegerField()
