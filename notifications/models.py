from django.db import models
from django.utils import timezone
from vibe_user.models import Viber
from video.models import Video
# Create your models here.

'''
selfications:
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
    to = models.ForeignKey(to=Viber, on_delete=models.CASCADE, null=True, blank=True, related_name="related_reciever")

    @property
    def msg(self):
        if self.n_type == "L":
            return "liked your video."
        elif self.n_type == "C":
            return "commented on your video."
        elif self.n_type ==  "F":
            return "followed you."
        elif self.n_type == "M":
            if self.sender == self.video.creator:
                return f"mentioned you in their video."
            else:
                return f"mentioned you in {video.creator.username}'s video."
        elif self.n_type == "CR":
            if self.sender == self.video.creator:
                return f"replied to your comment on their video."
            else:
                return f"replied to your comment on {video.creator.username}'s video."
        elif self.n_type == "CL":
            if self.sender == self.video.creator:
                return f"liked your comment on their video."
            else:
                return f"liked your comment on {video.creator.username}'s video."
