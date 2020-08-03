from django.db import models
from datetime import datetime

# Create your models here.

class Quote(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    description = models.TextField()
    deadline = models.CharField(max_length=1000)
    document = models.FileField(upload_to="quote/")