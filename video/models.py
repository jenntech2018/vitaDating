from django.db import models
from django.utils import timezone
from django.conf import settings

import os
from urllib.parse import urlparse

import random

base_dir = settings.BASE_DIR
PRIVACY_SETTINGS = [
    ("F", "Friends"),
    ("PRV", "Private"),
    ("PUB", "Public")
]

def default_replies():
    return dict(replies=[])



def user_dir_path(instance, filename):
    # once we have the user model, file upload naming will be:
    # /@<user.display_name>/video/<video id>
    return f"@test/{instance.uuid}.mp4"

def gen_uuid():
    return random.randint(690000000, 699999999)

class Video(models.Model):

        
    uuid = models.IntegerField(default=gen_uuid, unique=True)
    video = models.FileField(upload_to=user_dir_path)
    privacy = models.CharField(max_length=3,choices=PRIVACY_SETTINGS)
    comments = models.ManyToManyField("Comment", blank=True)
    likes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.description} | {self.timestamp}"


    def get_absolute_url(self):
        return f"{base_dir}/media/@test/{self.uuid}.mp4"


class Comment(models.Model):
    # user = models.ForeignKey("vibe_user.Viber", on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    replies = models.JSONField(default=default_replies)
    timestamp = models.DateTimeField(default=timezone.now)