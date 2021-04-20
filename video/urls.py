from django.urls import path
from video.views import UploadView, sound_view

urlpatterns = [
    path("upload", UploadView.as_view(), name="upload"),
    path("music/original-sound-<int:sound_uuid>", sound_view, name="view_sound")
]