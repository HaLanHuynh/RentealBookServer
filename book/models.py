from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=30)
    topic = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    imageUrl = models.CharField(max_length=500)