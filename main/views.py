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
        videos = Video.objects.all().order_by('-timestamp')
        suggested_creators = Viber.objects.all().filter(verified=True).order_by('followers')[:10]
        return render(request, "main/main.html", {"videos": videos, "suggested": suggested_creators})