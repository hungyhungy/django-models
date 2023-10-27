from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name