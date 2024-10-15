from django.db import models
from django.utils import timezone
from vitaDatinguser.models import vitaDatinguser
from activity.models import Activity
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
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True, blank=True, related_name="related_activity")
    comment = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True, blank=True, related_name="related_comment")
    sender = models.ForeignKey(vitaDatinguser, on_delete=models.CASCADE, null=True, blank=True, related_name="related_sender")
    to = models.ForeignKey(to=vitaDatinguser, on_delete=models.CASCADE, null=True, blank=True, related_name="related_reciever")

    @property
    def msg(self):
        if self.n_type == "L":
            return "liked your activity."
        elif self.n_type == "C":
            return "commented on your activity."
        elif self.n_type ==  "F":
            return "followed you."
        elif self.n_type == "M":
            if self.sender == self.activity.creator:
                return f"mentioned you in their activity."
            else:
                return f"mentioned you in {activity.creator.username}'s activity."
        elif self.n_type == "CR":
            if self.sender == self.activity.creator:
                return f"replied to your comment on their activity."
            else:
                return f"replied to your comment on {activity.creator.username}'s activity."
        elif self.n_type == "CL":
            if self.sender == self.activity.creator:
                return f"liked your comment on their activity."
            else:
                return f"liked your comment on {activity.creator.username}'s activity."
