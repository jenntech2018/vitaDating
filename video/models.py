from django.db import models
from django.utils import timezone

PRIVACY_SETTINGS = [
    ("F", "Friends"),
    ("PRV", "Private"),
    ("PUB", "Public")
]

def default_replies():
    return dict(replies=[])

def user_dir_path(instance, filename):
    return f"user_{instance.user.id}/{filename}"

class Video(models.Model):
    video = models.FileField(upload_to=user_dir_path)
    privacy = models.CharField(max_length=3,choices=PRIVACY_SETTINGS)
    comments = models.ManyToManyField("Comment")
    likes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=70)

class Comment(models.Model):
    # user = models.ForeignKey("vibe_user.Viber", on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    replies = models.JSONField(default=default_replies)
    timestamp = models.DateTimeField(default=timezone.now)