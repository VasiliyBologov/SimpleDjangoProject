from django.db import models

# Create your models here.

class One(models.Model):
    name = models.CharField(max_length=50)
    other_field = models.IntegerField()
