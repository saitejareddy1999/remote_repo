from django.db import models

# Create your models here.
class Connectfour(models.Model):
    name=models.CharField(max_length=256)
    # id=models.CharField(max_length=256)
