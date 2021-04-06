from django.db import models
from django.utils import timezone
# Create your models here.

'''
notifications:
time
mentions
post
liked
commented
follow
'''

class Notifications(models.model):
    time_created = models.DateTimeField(default=timezone.now)
    mentions = models.ManyToManyField()
    