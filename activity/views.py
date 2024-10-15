from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
base_dir = settings.BASE_DIR
import requests

from activity.forms import UploadForm
from activity.models import Activity, Sound
from vitaDatinguser.models import vitaDatinguser
from VitaDating.helpers import upload_file

import moviepy.editor as mp

class UploadView(LoginRequiredMixin, View):
    def post(self, request):
        form = UploadForm(request.POST or None, request.FILES or None, user=request.user)
        if form.is_valid():
            data = form.cleaned_data
            if not data['sound']:
                activity = mp.activityFileClip(data["activity"].temporary_file_path())
                instance = form.save()
                activity.audio.write_audiofile(f'{instance.uuid}_sound.mp3')

                upload_file(f'{instance.uuid}_sound.mp3', "VitaDatingbucket", f'media/@{request.user.username}/activity/{instance.uuid}_sound.mp3')
                sound = Sound.objects.create(
                    original_activity = instance,
                    creator = request.user,
                    audio_file = f"@{request.user.username}/activity/{instance.uuid}_sound.mp3"
                )
                instance.sound = sound
                instance.save()
            else:
                activity = mp.activityFileClip(data["activity"].temporary_file_path())
                res = requests.get(data['sound'].audio_file.url)
                open(data['sound'].audio_file.url.split('activity/')[-1], 'wb').write(res.content)

                audio_clip = mp.AudioFileClip(data['sound'].audio_file.url.split('activity/')[-1])
                if activity.duration < audio_clip.duration:
                    audio_clip = audio_clip.subclip(activity.duration)
                activity_clip = activity.set_audio(audio_clip)

                instance = form.save(commit=False)
                activity_clip.write_activityfile(f"{instance.uuid}.{activity_clip.filename.split('.')[-1]}")
                upload_file(
                    f"{instance.uuid}.{activity_clip.filename.split('.')[-1]}",
                    "VitaDatingbucket",
                    f"media/@{request.user.username}/activity/{instance.uuid}.{activity_clip.filename.split('.')[-1]}"
                    )

                instance.activity = f"@{request.user.username}/activity/{instance.uuid}.{activity_clip.filename.split('.')[-1]}"
                instance.save()
            return redirect(reverse("main"))

    def get(self, request):
        sound_options = Sound.objects.all()
        form = UploadForm(initial={'creator':request.user, 'sound': sound_options}, user=request.user)
        return render(request, "activity/upload.html", {"form": form})


def sound_view(request, sound_uuid):
    original_activity = Activity.objects.get(uuid=sound_uuid)
    sound = Sound.objects.get(original_activity=original_activity)
    suggested = vitaDatinguser.objects.filter(verified=True).order_by('followers')[:10]

    used_by = Activity.objects.filter(sound=sound)
    return render(request, 'activity/sound.html', {"sound": sound, "suggested": suggested, "used_by": used_by})