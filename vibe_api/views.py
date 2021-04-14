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
        sender = Viber.objects.get(id=request.data["viber_id"])
        creator = Viber.objects.get(id=request.data["creator_id"])

        Notifications.objects.create(
                                     n_type="L",
                                     video=data,
                                     sender=sender,
                                     to=creator)
        
        serialized_data = self.get_serializer(data)
        return Response(data=serialized_data.data,status=status.HTTP_201_OK)

    
    @action(detail=True, methods=["post"])
    def unlike_video(self, request, pk=None):
        Video.objects.filter(id=pk).update(likes=F("likes") - 1)
        data = Video.objects.get(id=pk)
        serialized_data = self.get_serializer(data)
        return Response(data=serialized_data.data,status=status.HTTP_201_OK)


class ViberViewSet(viewsets.ModelViewSet):
    queryset = Viber.objects.all().order_by('-username')
    serializer_class = ViberSerializer

    @action(detail=True, methods=["post"])
    def follow(self, request, pk=None):
        user = Viber.objects.get(id=pk)
        follower = Viber.objects.get(id=request.data["from_id"])
        
        user.followers.add(follower)
        follower.following.add(user)

        user.save()
        follower.save()

        Notifications.objects.create(
            n_type="F",
            sender=follower,
            to=user
        )

        followers_count = user.followers.all().count()
        return Response(data={"followers_count": followers_count}, status=status.HTTP_201_CREATED)


    @action(detail=True, methods=["post"])
    def unfollow(self, request, pk=None):
        user = Viber.objects.get(id=pk)
        unfollower = Viber.objects.get(id=request.data["from_id"])
        user.followers.remove(unfollower)
        unfollower.following.remove(user)
        user.save()
        unfollower.save()

        Notifications.objects.create(
            n_type="F",
            sender=unfollower,
            to=user
        )
        followers_count = user.followers.all().count()
        return Response(data={"followers_count": followers_count}, status=status.HTTP_201_CREATED)




class SoundViewSet(viewsets.ModelViewSet):
    queryset = Sound.objects.all().order_by('-id')
    serializer_class = SoundSerializer


class NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Notifications.objects.all().order_by('-id')
    serializer_class = NotificationsSerializer