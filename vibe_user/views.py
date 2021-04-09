from django.shortcuts import render, HttpResponseRedirect, reverse

from django.contrib.auth.models import AbstractUser
from vibe_user.models import Viber
from video.models import Video
# Create your views here.

def vibe_user_profile_view(request, user_id):
    vibe_user = Viber.objects.get(id=user_id)
    vibe_followers = vibe_user.followers.all().count
    vibe_following = vibe_user.following.all().count
    vibe_user_profile_photo = vibe_user.profile_photo
    # vibe_user_videos = Video.objects.get(id=user_id)
    # vibe_likes = vibe_user.likes.all().count
    return render(request, "user/vibe_profile.html", {
        "vibe_user": vibe_user, 
        "vibe_followers": vibe_followers,
        "vibe_following": vibe_following,
        "vibe_user_profile_photo":vibe_user_profile_photo,
        # "vibe_user_videos": vibe_user_videos,
        # 'vibe_likes': vibe_likes,
        })

