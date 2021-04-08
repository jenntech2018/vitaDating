from django.db import models
from django.utils import timezone
from django.conf import settings

import os
from urllib.parse import urlparse

from vibetube.helpers import user_vid_path, gen_uuid

base_dir = settings.BASE_DIR
PRIVACY_SETTINGS = [
    ("F", "Friends"),
    ("PRV", "Private"),
    ("PUB", "Public")
]

def default_replies():
    return dict(replies=[])

class Video(models.Model):
    creator = models.ForeignKey('vibe_user.Viber', null=True, blank=True, on_delete=models.CASCADE, related_name="video_creator")
    video = models.FileField(upload_to=user_vid_path)
    uuid = models.IntegerField(default=gen_uuid, unique=True)
    privacy = models.CharField(max_length=3,choices=PRIVACY_SETTINGS)
    comments = models.ManyToManyField("Comment", blank=True)
    likes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now)
    caption = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.caption} | {self.timestamp}"

class Comment(models.Model):
    user = models.ForeignKey('vibe_user.Viber', null=True, blank=True, on_delete=models.CASCADE, related_name="commenter")
    comment = models.CharField(max_length=60, null=True, blank=True)
    likes = models.IntegerField(default=0)
    replies = models.JSONField(default=default_replies)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.comment} | {self.user} | {self.timestamp}"