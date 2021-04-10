from django.db.models import F
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from video.models import Video, Comment, Sound
from vibe_user.models import Viber

from vibe_api.serializers import ViberSerializer, VideoSerializer, SoundSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('-timestamp')
    serializer_class = VideoSerializer

    @action(detail=True, methods=["post"])
    def like_video(self, request, pk=None):
        Video.objects.filter(id=pk).update(likes=F("likes") + 1)
        data = Video.objects.get(id=pk)
        serialized_data = self.get_serializer(data)
        return Response(data=serialized_data.data,status=status.HTTP_200_OK)

    
    @action(detail=True, methods=["post"])
    def unlike_video(self, request, pk=None):
        Video.objects.filter(id=pk).update(likes=F("likes") - 1)
        data = Video.objects.get(id=pk)
        serialized_data = self.get_serializer(data)
        return Response(data=serialized_data.data,status=status.HTTP_200_OK)

    
    @action(detail=True, methods=["get"])
    def video_info(self, request, pk=None):
        x = Video.objects.filter(id=pk).all()
        serializer = self.get_serializer(x, many=True)
        return Response(serializer.data)


class ViberViewSet(viewsets.ModelViewSet):
    queryset = Viber.objects.all().order_by('-username')
    serializer_class = ViberSerializer


class SoundViewSet(viewsets.ModelViewSet):
    queryset = Sound.objects.all().order_by('-id')
    serializer_class = SoundSerializer