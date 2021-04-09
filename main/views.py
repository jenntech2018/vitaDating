from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.urls import reverse

import datetime

from video.models import Video
from vibe_auth.forms import LoginForm, RegistrationForm
from vibe_user.models import Viber
from vibetube.helpers import auth_user, check_for_name, check_for_username, handle_create_user

class MainView(View):
    def post(self, request):
        if 'email' in request.POST: form = RegistrationForm(request.POST, request.FILES)
        else: form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if 'email' in data:
                handle_create_user(data)
                
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