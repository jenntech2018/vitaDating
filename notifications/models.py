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

CHOICES = [
    (
        "M", "MENTION"
    ),
    (
        "L", "LIKE"
    ),
    (
        "C", "COMMENT"
    ),
    (
        "F", "FOLLOW"
    ),
    (
        "CR", "COMMENT_REPLY"
    ),
    (
        "CL", "COMMENT_LIKE"
    )
]

class Notifications(models.Model):
    time_created = models.DateTimeField(default=timezone.now)
    n_type = models.CharField(choices=CHOICES, max_length=2)
    video = models.ForeignKey(to=Video, on_delete=models.CASCADE, null=True, blank=True, related_name="related_video")
    comment = models.ForeignKey(to=Video, on_delete=models.CASCADE, null=True, blank=True, related_name="related_comment")
    sender = models.ForeignKey(to=Viber, on_delete=models.CASCADE, null=True, blank=True, related_name="related_sender")
    to = models.ForeignKey(to=Viber, on_delete=models.CASCADE, null=True, blank=True, related_name="related_to")
