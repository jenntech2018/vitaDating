from django.shortcuts import render, HttpResponseRedirect, reverse, redirect

from django.contrib.auth.models import AbstractUser
from vibe_user.models import Viber
from video.models import Video
from vibe_user.forms import EditProfileForm
# Create your views here.

def vibe_user_profile_view(request, username):
    vibe_user = Viber.objects.get(username=username)

    following = Viber.objects.filter(username=request.user, following=vibe_user)
    is_following = "true" if bool(following) else "false"

    vibe_followers = vibe_user.followers.all().count
    vibe_following = vibe_user.following.all().count

    vibe_user_videos = Video.objects.filter(creator=vibe_user).all()

    suggested_creators = Viber.objects.all().filter(verified=True).order_by('-followers')[:10]
    return render(request, "user/vibe_profile.html", {
        "vibe_user": vibe_user, 
        "vibe_followers": vibe_followers,
        "vibe_following": vibe_following,
        "vibe_user_videos": vibe_user_videos,
        "suggested": suggested_creators,
        "is_following": is_following,
        })

def vibe_user_follower_view(request, user_id):
    follow = Viber.objects.get(id=user_id)
    request.user.followers.add(follow)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def vibe_user_unfollow_view(request, user_id):
    follow = Viber.objects.get(id=user_id)
    request.user.followers.remove(follow)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def edit_profile_view(request, username):
    editable = Viber.objects.get(id=request.user.id)

    if request.method == "POST":
        form = EditProfileForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            editable.display_name = data['display_name']
            editable.bio = data['bio']
            editable.profile_photo = data['profile_photo']
            editable.first_name = data['first_name']
            editable.last_name = data['last_name']
            editable.username = data['username']
            editable.save()
        return HttpResponseRedirect(request.GET.get('next', reverse('profile', args=[editable.username])))

    form = EditProfileForm(
        initial={
            "display_name": editable.display_name,
            "bio": editable.bio,
            "profile_photo": editable.profile_photo,
            "first_name": editable.first_name,
            "last_name": editable.last_name,
            "username": editable.username,
        }
    )
    return render(request, "user/edit_profile.html", {'form': form})

def settings_page(request):
    return render(request, 'settings/settings.html', {})

def delete_account(request):
    Viber.objects.get(id=request.user.id).delete()
    return redirect(reverse("main"))
