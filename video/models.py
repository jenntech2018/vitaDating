from django.db import models
from django.utils import timezone
from django.conf import settings
import os
from urllib.parse import urlparse

from vibetube.helpers import user_vid_path, gen_uuid, user_sound_path

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
    uuid = models.IntegerField(default=gen_uuid, unique=True)
    video = models.FileField(upload_to=user_vid_path)
    privacy = models.CharField(max_length=3,choices=PRIVACY_SETTINGS)
    comments = models.ManyToManyField("Comment", blank=True)
    likes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now)
    caption = models.CharField(max_length=70)
    sound = models.ForeignKey("video.Sound", related_name="vid_sound", on_delete=models.CASCADE, null=True, blank=True,)

    def __str__(self):
        return f"{self.caption} | {self.timestamp}"


class Sound(models.Model):
    creator = models.ForeignKey("vibe_user.Viber", related_name="sound_creator", on_delete=models.CASCADE)
    original_video = models.ForeignKey("video.Video", related_name="og_sound", on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to=user_sound_path)


class Comment(models.Model):
    user = models.ForeignKey('vibe_user.Viber', null=True, blank=True, on_delete=models.CASCADE, related_name="commenter")
    comment = models.CharField(max_length=60, null=True, blank=True)
    likes = models.IntegerField(default=0)
    liked_by = models.ManyToManyField('vibe_user.Viber', blank=True, related_name="like_list")
    replies = models.JSONField(default=default_replies)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.comment} | {self.user} | {self.timestamp}"

    @property
    def fixed_date(self):
        current_date = timezone.now()
        value = self.timestamp
        if current_date.month == value.month and current_date.day == value.day and current_date.hour == value.hour and current_date.minute == value.minute:
            return f"{current_date.second - value.second} second(s) ago"
        elif current_date.month == value.month and current_date.day == value.day and current_date.hour == value.hour:
            return f"{current_date.minute - value.minute} minute(s) ago"
        elif current_date.day == value.day and current_date.month == value.month:
            return f"{current_date.hour - value.hour} hour(s) ago"
        else:
            return f"{(current_date.day - value.day)} day(s) ago"