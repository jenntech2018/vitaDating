from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.conf import settings
base_dir = settings.BASE_DIR

from video.forms import UploadForm
from video.models import Video, Sound

import moviepy.editor as mp

class UploadView(View):
    def post(self, request):
        form = UploadForm(request.POST or None, request.FILES or None, user=request.user)
        if form.is_valid():
            data = form.cleaned_data
            video = mp.VideoFileClip(data["video"].temporary_file_path())
            
            instance = form.save()
            video.audio.write_audiofile(f"media/@{request.user.username}/video/{instance.uuid}_sound.mp3")
            sound = Sound.objects.create(
                original_video = instance,
                creator = request.user,
                audio_file = f"@{request.user.username}/video/{instance.uuid}_sound.mp3"
            )
            return redirect(reverse("main"))

    def get(self, request):
        form = UploadForm(initial={'creator':request.user}, user=request.user)
        return render(request, "video/upload.html", {"form": form})