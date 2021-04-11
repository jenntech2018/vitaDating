from django.db.models import F
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from video.models import Video, Comment, Sound
from vibe_user.models import Viber
from notifications.models import Notifications

from vibe_api.serializers import ViberSerializer, VideoSerializer, SoundSerializer, NotificationsSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('-timestamp')
    serializer_class = VideoSerializer

    @action(detail=True, methods=["post"])
    def like_video(self, request, pk=None):
        Video.objects.filter(id=pk).update(likes=F("likes") + 1)
        data = Video.objects.get(id=pk)

        Notifications.objects.create(
                                     n_type="L",
                                     video=data,
                                     sender=request.data["viber_id"],
                                     to = request.data["creator_id"])
        
        serialized_data = self.get_serializer(data)
        return Response(data=serialized_data.data,status=status.HTTP_200_OK)

    
    @action(detail=True, methods=["post"])
    def unlike_video(self, request, pk=None):
        Video.objects.filter(id=pk).update(likes=F("likes") - 1)
        data = Video.objects.get(id=pk)
        serialized_data = self.get_serializer(data)
        return Response(data=serialized_data.data,status=status.HTTP_200_OK)


class ViberViewSet(viewsets.ModelViewSet):
    queryset = Viber.objects.all().order_by('-username')
    serializer_class = ViberSerializer


class SoundViewSet(viewsets.ModelViewSet):
    queryset = Sound.objects.all().order_by('-id')
    serializer_class = SoundSerializer


class NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Notifications.objects.all().order_by('-id')
    serializer_class = NotificationsSerializer