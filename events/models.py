from django.db import models


# Design what we want our models to look like. 
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    venue = models.TextField(max_length=50)
    ticket = models.TextField(max_length=50)
    signature = models.CharField(max_length=200, default='Loud musiq no silence')


def __str__(self):
    return self.title
