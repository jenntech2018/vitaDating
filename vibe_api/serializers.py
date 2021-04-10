from video.models import Video, Comment, Sound
from vibe_user.models import Viber
from rest_framework import serializers


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ["id", "video", "likes", "comments", "creator", "privacy", "sound"]


class ViberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Viber
        fields = ["id", "display_name", "username", "email", "verified", "followers", "following"]


class SoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sound
        fields = ["id", "original_video", "creator", "audio_file"]