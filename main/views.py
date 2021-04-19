from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.urls import reverse

import datetime

from video.models import Video
from vibe_auth.forms import LoginForm, RegistrationForm
from vibe_user.models import Viber
from vibetube.helpers import auth_user, check_for_name, check_for_username

class MainView(View):
    def post(self, request):
        if 'email' in request.POST: form = RegistrationForm(request.POST, request.FILES)
        else: form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if 'email' in data:
                display_name = check_for_name(data["display_name"])
                username = check_for_username(data['username'], display_name)
                dob = datetime.date(int(data["year"]), int(data["month"]), int(data["day"]))
                data["username"] = username

                Viber.objects.create_user(
                    username=username,
                    email=data["email"],
                    password=data["password"],
                    dob=dob,
                    display_name=display_name,
                    profile_photo=data["profile_photo"])
            is_authed = auth_user(request, data)
            if is_authed:
                return redirect(reverse("main"))

    def get(self, request):
        following_vids = []
        videos = Video.objects.all().order_by('-timestamp')
        user = Viber.objects.get(id=request.user.id)
        # following = user.following.all()
        # for viber in following:
        #     vid = Video.objects.filter(creator=viber)
        #     following_vids.append(vid)
        print(following_vids)
        # for vid in following_vids[:len(following_vids)-1]:
        #     print(vid.creator)
        suggested_creators = Viber.objects.all().filter(verified=True).order_by('-followers')[:10]
        return render(request, "main/main.html", {"videos": videos, "suggested": suggested_creators, 'vids': following_vids})


'''
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

class Viber(AbstractUser):
    display_name = models.CharField(max_length=120, null=True, blank=True)
    bio = models.TextField()
    dob = models.DateField(blank=True,null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='viber_followers')
    following = models.ManyToManyField('self', symmetrical=False, related_name='viber_following')
    videos = models.ManyToManyField(Video, related_name='viber_videos')
    verified = models.BooleanField(default=False)
    sounds = models.ManyToManyField(Sound, related_name='viber_sounds')
    profile_photo = models.ImageField(upload_to=user_photo_path, blank=True, null=True)
    liked_videos = models.ManyToManyField(Video, related_name="liked_videos_list")

'''
