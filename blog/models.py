from django.db import models

# Design what we want our models to look like 
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    signature = models.CharField(max_length=200, default='Loud musiq no silence')
    date = models.DateTimeField()


def __str__(self):
    return self.title
