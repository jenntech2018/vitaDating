from django.db import models

# Create your models here.
class EmailAuth(models.Model):
    token = models.IntegerField()