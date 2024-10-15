from django.db import models
from django.contrib.auth.models import AbstractUser

import random

from activity.models import Activity, Sound
from VitaDating.helpers import user_photo_path


class vitaDatinguser(AbstractUser):
    display_name = models.CharField(max_length=64, null=True, blank=True)
    bio = models.TextField(blank=True, null=True, max_length=80)
    dob = models.DateField(blank=True,null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='vitaDatinguser_followers')
    following = models.ManyToManyField('self', symmetrical=False, related_name='vitaDatinguser_following')
    activities = models.ManyToManyField(Activity, related_name='vitaDatinguser_activities')
    verified = models.BooleanField(default=False)
    sounds = models.ManyToManyField(Sound, related_name='vitaDatinguser_sounds')
    profile_photo = models.ImageField(upload_to=user_photo_path, blank=True, null=True)
    liked_activities = models.ManyToManyField(Activity, related_name="liked_activitys_list")
    website = models.URLField(blank=True, null=True)

    @property
    def activity_likes(self):
        user_activities = Activity.objects.filter(creator=self).all()
        count = 0
        for vid in user_activities:
            count += vid.likes
        return count

    def __str__(self):
        return self.username