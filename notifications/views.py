from django.shortcuts import render
from notifications.models import Notifications
# Create your views here.
'''
def like_notification(request, post_id):

def comment_notification(request, post_id):

def follow_notifcation(request, user_id):

def mention_notifcation(requst, post_id):
'''


def notification_view(request, user_id):
    user = Model.objects.get(id=user_id)
    mention_notifications = Notifications.objects.filter(mentions=user_id).all()
    like_notifications = Notifications.objects.filter(mentions=user_id).all()
    comment_notifications = Notifications.objects.filter(mentions=user_id).all()
    followed_notifications = Notifications.objects.filter(mentions=user_id).all()
    return render(request, 'notifications.html',{
        'comments': comment_notifications,
        'likes': like_notifications,
        'mentions': mention_notifications,
        'followed': followed_notifications
    })