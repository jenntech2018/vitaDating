from django.db.models import F
from django.utils import timezone
from vitaDatingapi.models import EmailAuth
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from instant.models import Message
from notifications.models import Notifications
from activity.models import Activity, Comment, Sound
from vitaDatinguser.models import vitaDatinguser
from VitaDating.helpers import generate_html

from vitaDatingapi.serializers import vitaDatinguserSerializer, MessageSerializer, CommentSerializer, activitySerializer, SoundSerializer, NotificationsSerializer, EmailAuthSerializer


class activityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('-timestamp')
    serializer_class = activitySerializer

    @action(detail=True, methods=["post"])
    def like_activity(self, request, pk=None):
        Activity.objects.filter(id=pk).update(likes=F("likes") + 1)
        data = Activity.objects.get(id=pk)

        sender = vitaDatinguser.objects.get(id=request.data["vitaDatinguser_id"])
        sender.liked_activities.add(data)

        creator = vitaDatinguser.objects.get(id=request.data["creator_id"])

        Notifications.objects.create(
                                     n_type="L",
                                     activity=data,
                                     sender=sender,
                                     to=creator)
        serialized_data = self.get_serializer(data)
        return Response(data=serialized_data.data,status=status.HTTP_201_CREATED)

    
    @action(detail=True, methods=["post"])
    def unlike_activity(self, request, pk=None):
        sender = vitaDatinguser.objects.get(username=request.data["username"])

        Activity.objects.filter(id=pk).update(likes=F("likes") - 1)
        data = Activity.objects.get(id=pk)
        sender.liked_activities.remove(data)
        serialized_data = self.get_serializer(data)
        return Response(data=serialized_data.data,status=status.HTTP_201_CREATED)


class vitaDatinguserViewSet(viewsets.ModelViewSet):
    queryset = vitaDatinguser.objects.all().order_by('-username')
    serializer_class = vitaDatinguserSerializer
        
    @action(detail=False, methods=["post"])
    def follow(self, request):
        user = vitaDatinguser.objects.get(id=request.data["to_id"])
        follower = vitaDatinguser.objects.get(id=request.data["from_id"])
        
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


    @action(detail=False, methods=["post"])
    def unfollow(self, request):
        user = vitaDatinguser.objects.get(id=request.data["to_id"])
        unfollower = vitaDatinguser.objects.get(id=request.data["from_id"])
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
        activity_id = request.data["activity_id"]
        user_id = request.data["user_id"]

        user = vitaDatinguser.objects.get(id=user_id)
        new_comment = Comment.objects.create(user=user, comment=comment)

        vid = Activity.objects.get(id=activity_id)
        vid.comments.add(new_comment)
        vid.save()

        comment_count = vid.comments.all().count()

        return Response({"comment_count": comment_count},status=status.HTTP_201_CREATED)

    
    @action(detail=True, methods=["post"])
    def add_reply(self, request, pk=None):
        comment = Comment.objects.get(id=pk)
        user = vitaDatinguser.objects.get(id=request.data["user_id"])

        photo_url = user.profile_photo.url if user.profile_photo else ""
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
        user = vitaDatinguser.objects.get(id=request.data["user_id"])
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
        user = vitaDatinguser.objects.get(id=request.data["user_id"])
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
        user = vitaDatinguser.objects.get(id=request.data["user_id"])
        
        comment.likes += 1
        comment.liked_by.add(user)
        comment.save()

        likes_count = comment.likes
        return Response({"likes_count": likes_count}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def unlike_comment(self, request, pk=None):
        comment = Comment.objects.get(id=pk)
        user = vitaDatinguser.objects.get(id=request.data["user_id"])

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
            from_email="VitaDatingz@gmail.com",
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


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @action(detail=False, methods=["post"])
    def send_message(self, request):
        recipient_id = request.data["recipient"]
        if recipient_id.isdigit():
            recip = vitaDatinguser.objects.get(id=int(recipient_id))
        else:
            recip = vitaDatinguser.objects.get(username=recipient_id)

        sender_id = request.data["sender"]
        sender = vitaDatinguser.objects.get(id=int(sender_id))
        
        message_body = request.data["content"]
        new_message = Message.objects.create(
                                             author=sender,
                                             recipient=recip,
                                             message=message_body)
        return Response({"message": new_message.message, "pub_date": new_message.pub_date})
