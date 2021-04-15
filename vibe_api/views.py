from django.db.models import F
from django.utils import timezone
from vibe_api.models import EmailAuth
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from video.models import Video, Comment, Sound
from vibe_user.models import Viber
from notifications.models import Notifications
from vibetube.helpers import generate_html

from vibe_api.serializers import ViberSerializer, CommentSerializer, VideoSerializer, SoundSerializer, NotificationsSerializer, EmailAuthSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('-timestamp')
    serializer_class = VideoSerializer

    @action(detail=True, methods=["post"])
    def like_video(self, request, pk=None):
        Video.objects.filter(id=pk).update(likes=F("likes") + 1)
        data = Video.objects.get(id=pk)

        sender = Viber.objects.get(id=request.data["viber_id"])
        sender.liked_videos.add(data)

        creator = Viber.objects.get(id=request.data["creator_id"])

        Notifications.objects.create(
                                     n_type="L",
                                     video=data,
                                     sender=sender,
                                     to=creator)
        serialized_data = self.get_serializer(data)
        return Response(data=serialized_data.data,status=status.HTTP_201_CREATED)

    
    @action(detail=True, methods=["post"])
    def unlike_video(self, request, pk=None):
        Video.objects.filter(id=pk).update(likes=F("likes") - 1)
        data = Video.objects.get(id=pk)
        serialized_data = self.get_serializer(data)
        return Response(data=serialized_data.data,status=status.HTTP_201_CREATED)


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

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSerializer

    @action(detail=False, methods=["post"])
    def add_comment(self, request):
        comment = request.data["comment"]
        video_id = request.data["video_id"]
        user_id = request.data["user_id"]

        user = Viber.objects.get(id=user_id)
        new_comment = Comment.objects.create(user=user, comment=comment)

        vid = Video.objects.get(id=video_id)
        vid.comments.add(new_comment)
        vid.save()

        comment_count = vid.comments.all().count()

        return Response({"comment_count": comment_count},status=status.HTTP_201_CREATED)

    
    @action(detail=True, methods=["post"])
    def add_reply(self, request, pk=None):
        comment = Comment.objects.get(id=pk)
        user = Viber.objects.get(id=request.data["user_id"])

        photo_url = user.profile_photo if user.profile_photo else ""
        verified = user.verified if user.verified else ""
        timestamp = str(timezone.now())

        if comment.replies["replies"]:
            reply_id = max(comment.replies["replies"], key=lambda x: x["id"])["id"] + 1
        else:
            reply_id = 1
        
        comment.replies["replies"].append(dict(user_id=request.data["user_id"], liked_by={"user_ids": []},id=reply_id, likes="0", verified=verified, username=user.username, photo_url=photo_url, reply=request.data["reply"], timestamp=timestamp))
        comment.save()
        reply_count = len(comment.replies["replies"])
        return Response({"reply_count": reply_count, "timestamp": timestamp, "reply_id": reply_id}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["post"])
    def like_reply(self, request, pk=None):
        comment = Comment.objects.get(id=pk)
        user = Viber.objects.get(id=request.data["user_id"])
        for reply in comment.replies["replies"]:
            if reply.get('id', 0) == request.data["reply_id"]:
                if not request.data["user_id"] in reply["liked_by"]["user_ids"]:
                    reply["likes"] = int(reply["likes"]) + 1
                    reply["liked_by"]["user_ids"].append(request.data["user_id"])
                likes_count = reply["likes"]
        comment.save()
        return Response({"likes_count": likes_count}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def unlike_reply(self, request, pk=None):
        comment = Comment.objects.get(id=pk)
        user = Viber.objects.get(id=request.data["user_id"])
        for reply in comment.replies["replies"]:
            if reply.get('id', 0) == request.data["reply_id"]:
                reply["likes"] = int(reply["likes"]) - 1
                reply["liked_by"]["user_ids"].remove(request.data["user_id"])
                likes_count = reply["likes"]
        comment.save()
        return Response({"likes_count": likes_count}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def like_comment(self, request, pk=None):
        comment = Comment.objects.get(id=pk)
        user = Viber.objects.get(id=request.data["user_id"])
        
        comment.likes += 1
        comment.liked_by.add(user)
        comment.save()

        likes_count = comment.likes
        return Response({"likes_count": likes_count}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def unlike_comment(self, request, pk=None):
        comment = Comment.objects.get(id=pk)
        user = Viber.objects.get(id=request.data["user_id"])

        comment.likes -= 1
        comment.liked_by.remove(user)
        comment.save()

        likes_count = comment.likes
        return Response({"likes_count": likes_count}, status=status.HTTP_200_OK)



class AuthViewSet(viewsets.ModelViewSet):
    queryset = EmailAuth.objects.all()
    serializer_class = EmailAuthSerializer

    @action(detail=False, methods=["post"])
    def send_token(self, request):
        import random
        import os
        import environ
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail

        token = random.randint(101010, 909090)
        user_email = request.data["email"]
        token_instance = EmailAuth.objects.create(token=token)
        environ.Env.read_env()
        key = os.environ["SENDGRID_API_KEY"]

        message = Mail(
            from_email="vibetubez@gmail.com",
            to_emails=user_email,
            subject=f"{token} is your verification code",
            html_content=generate_html(user_email, token))

        try:
            sg = SendGridAPIClient(key)
            resp = sg.send(message)
            print(resp.status_code)
            print(resp.body)
            print(resp.headers)
            return Response(status=status.HTTP_201_CREATED)
        except Exception as err:
            print(err.message)

    
    @action(detail=False, methods=["post"])
    def verify_token(self, request):
        token = int(request.data["token"])
        token_instance = EmailAuth.objects.get(token=token)
        if token_instance:
            token_instance.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
