from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.conf import settings
base_dir = settings.BASE_DIR

from video.forms import UploadForm
from video.models import Video, Sound
from vibe_user.models import Viber
from vibetube.helpers import upload_file

import moviepy.editor as mp

class UploadView(View):
    def post(self, request):
        form = UploadForm(request.POST or None, request.FILES or None, user=request.user)
        if form.is_valid():
            data = form.cleaned_data
            if not data['sound']:
                video = mp.VideoFileClip(data["video"].temporary_file_path())
                instance = form.save()
                video.audio.write_audiofile(f'{instance.uuid}_sound.mp3')

                upload_file(f'{instance.uuid}_sound.mp3', "vibetubebucket", f'media/@{request.user.username}/video/{instance.uuid}_sound.mp3')
                sound = Sound.objects.create(
                    original_video = instance,
                    creator = request.user,
                    audio_file = f"@{request.user.username}/video/{instance.uuid}_sound.mp3"
                )
                instance.sound = sound
                instance.save()
            else:
                video = mp.VideoFileClip(data["video"].temporary_file_path())
                audio_clip = mp.AudioFileClip(f"media/{data['sound'].audio_file.url.replace('/media/%40', '@')}")
                if video.duration < audio_clip.duration:
                    audio_clip = audio_clip.subclip(video.duration)
                video_clip = video.set_audio(audio_clip)

                instance = form.save(commit=False)
                video_clip.write_videofile(f"{instance.uuid}.{video_clip.filename.split('.')[-1]}")
                upload_file(
                    f"{instance.uuid}.{video_clip.filename.split('.')[-1]}",
                    "vibetubebucket",
                    f"media/@{request.user.username}/video/{instance.uuid}.{video_clip.filename.split('.')[-1]}"
                    )

                instance.video = f"@{request.user.username}/video/{instance.uuid}.{video_clip.filename.split('.')[-1]}"
                instance.save()
            return redirect(reverse("main"))

    def get(self, request):
        sound_options = Sound.objects.all()
        form = UploadForm(initial={'creator':request.user, 'sound': sound_options}, user=request.user)
        return render(request, "video/upload.html", {"form": form})


def sound_view(request, sound_uuid):
    original_video = Video.objects.get(uuid=sound_uuid)
    sound = Sound.objects.get(original_video=original_video)
    suggested = Viber.objects.filter(verified=True).order_by('followers')[:10]

    used_by = Video.objects.filter(sound=sound)
    return render(request, 'video/sound.html', {"sound": sound, "suggested": suggested, "used_by": used_by})