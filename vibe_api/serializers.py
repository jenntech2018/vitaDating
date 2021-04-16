from video.models import Video, Comment, Sound
from vibe_api.models import EmailAuth
from vibe_user.models import Viber
from notifications.models import Notifications
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


class NotificationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notifications
        fields = ["id", "time_created", "n_type", "video", "comment", "sender", "to"]


class EmailAuthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmailAuth
        fields = ["id"]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "user", "comment", "likes", "replies", "timestamp"]

