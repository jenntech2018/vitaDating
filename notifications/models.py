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

class Notifications(models.Model):
    time_created = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Video, on_delete=models.CASCADE)
    mentions = models.ManyToManyField(Viber, symmetrical=False, related_name='mentions')
    # user = models.ManyToManyField(Viber, symmetrical=False, related_name='mentions')

    def __str__(self):
        return self.mentions

class LikedNotifications(models.Model):
    time_created = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Video, on_delete=models.CASCADE)
    liked = models.ManyToManyField(Viber, symmetrical=False, related_name='liked')

class CommentedNotifications(models.Model):
    time_created = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Video, on_delete=models.CASCADE)
    Commented = models.ManyToManyField(Viber, symmetrical=False, related_name='commented')

class FollowedNotifications(models.Model):
    followed = models.ManyToManyField(Viber, symmetrical=False, related_name='followed')