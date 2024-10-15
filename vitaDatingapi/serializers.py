from instant.models import Message
from notifications.models import Notifications
from activity.models import Activity, Comment, Sound
from vitaDatingapi.models import EmailAuth
from vitaDatinguser.models import vitaDatinguser
from rest_framework import serializers


class activitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ["id", "activity", "likes", "comments", "creator", "privacy", "sound"]


class vitaDatinguserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vitaDatinguser
        fields = ["id", "display_name", "username", "email", "verified", "followers", "following"]


class SoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sound
        fields = ["id", "original_activity", "creator", "audio_file"]


class NotificationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notifications
        fields = ["id", "time_created", "n_type", "activity", "comment", "sender", "to"]


class EmailAuthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmailAuth
        fields = ["id"]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "user", "comment", "likes", "replies", "timestamp"]


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        # we aint tryna have people see mf messages
        fields = ["id", "recipient", "author", "message"]
