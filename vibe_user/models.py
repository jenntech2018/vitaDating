from django.db import models
from django.contrib.auth.models import AbstractUser

import random

from video.models import Video, Sound
from vibetube.helpers import user_photo_path


class Viber(AbstractUser):
    display_name = models.CharField(max_length=120, null=True, blank=True)
    bio = models.TextField()
    dob = models.DateField(blank=True,null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='viber_followers')
    following = models.ManyToManyField('self', symmetrical=False, related_name='viber_following')
    videos = models.ManyToManyField(Video, related_name='viber_videos')
    verified = models.BooleanField(default=False)
    sounds = models.ManyToManyField(Sound, related_name='viber_sounds')
    profile_photo = models.ImageField(upload_to=user_photo_path, blank=True, null=True)
    liked_videos = models.ManyToManyField(Video, related_name="liked_videos_list")

    @property
    def video_likes(self):
        user_videos = Video.objects.filter(creator=self).all()
        count = 0
        for vid in user_videos:
            count += vid.likes
        return count

    def __str__(self):
        return self.username