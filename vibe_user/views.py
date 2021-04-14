from django.shortcuts import render, HttpResponseRedirect, reverse

from django.contrib.auth.models import AbstractUser
from vibe_user.models import Viber
from video.models import Video
# Create your views here.

def vibe_user_profile_view(request, username):
    vibe_user = Viber.objects.get(username=username)
    
    following = Viber.objects.filter(username=request.user, following=vibe_user)
    is_following = "true" if bool(following) else "false"

    vibe_followers = vibe_user.followers.all().count
    vibe_following = vibe_user.following.all().count
    vibe_user_profile_photo = vibe_user.profile_photo
    # vibe_user_videos = Video.objects.get(id=user_id)
    # vibe_likes = vibe_user.likes.all().count
    suggested_creators = Viber.objects.all().filter(verified=True).order_by('-followers')[:10]
    return render(request, "user/vibe_profile.html", {
        "vibe_user": vibe_user, 
        "vibe_followers": vibe_followers,
        "vibe_following": vibe_following,
        "vibe_user_profile_photo":vibe_user_profile_photo,
        # "vibe_user_videos": vibe_user_videos,
        # 'vibe_likes': vibe_likes,
        "suggested": suggested_creators,
        "is_following": is_following
        })

def vibe_user_follower_view(request, user_id):
    follow = Viber.objects.get(id=user_id)
    request.user.followers.add(follow)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def vibe_user_unfollow_view(request, user_id):
    follow = Viber.objects.get(id=user_id)
    request.user.followers.remove(follow)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
