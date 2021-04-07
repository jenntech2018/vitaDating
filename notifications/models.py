from django.db import models
from django.utils import timezone
from vibe_user.models import Viber
from video.models import Video
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
    mentions = models.ManyToManyField(Viber, symmetrical=False, related_name='mentions')
    post = models.ForeignKey(Video, on_delete=models.CASCADE)
    liked = models.ManyToManyField(Viber, symmetrical=False, related_name='liked')
    Commented = models.ManyToManyField(Viber, symmetrical=False, related_name='commented')
    followed = models.ManyToManyField(Viber, symmetrical=False, related_name='followed')
