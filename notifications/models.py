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
    mentions = models.ManyToManyField(Viber, symmetrical=False)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.mentions


class LikedNotifications(models.Model):
    time_created = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Video, on_delete=models.CASCADE)
    liked = models.ManyToManyField(Viber, symmetrical=False)
    user = models.CharField(max_length=100)


class CommentedNotifications(models.Model):
    time_created = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Video, on_delete=models.CASCADE)
    Commented = models.ManyToManyField(Viber, symmetrical=False)
    user = models.CharField(max_length=100)


class FollowedNotifications(models.Model):
    followed = models.ManyToManyField(Viber, symmetrical=False)
    user = models.CharField(max_length=100)
