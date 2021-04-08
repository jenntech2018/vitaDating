from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.urls import reverse

import datetime

from video.models import Video
from vibe_auth.forms import LoginForm, RegistrationForm
from vibe_user.models import Viber
from vibetube.helpers import auth_user, check_for_name

class MainView(View):
    def post(self, request):
        if request.POST['email']: form = RegistrationForm(request.POST, request.FILES)
        else: form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['email']:
                display_name = check_for_name(data["display_name"])
                dob = datetime.date(int(data["year"]), int(data["month"]), int(data["day"]))
                Viber.objects.create_user(
                    username=data["email"],
                    password=data["password"],
                    dob=dob,
                    display_name=display_name,
                    profile_photo=data["profile_photo"])
            is_authed = auth_user(request, data)
            if is_authed:
                return redirect(reverse("main"))

    def get(self, request):
        stuff = Video.objects.all()
        return render(request, "main/main.html", {"vids": stuff})

        #     if request.method == 'POST':
        # form = LoginForm(request.POST)
        # if form.is_valid():
        #     from django.contrib.auth import authenticate, login
        #     if "@" in data["name"]:
        #         user = authenticate(request, username=data["name"], password=data["password"])
        #     else:
        #         user = authenticate(request, display_name=data["name"], password=data["password"])
            
        #     if user:
        #         login(request, user)
        #     return redirect(reverse("main"))