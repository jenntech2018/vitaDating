from django.shortcuts import render
from notifications.models import Notifications
from video.models import Video
# Create your views here.
'''
def like_notification(request, post_id):


def comment_notification(request, post_id):

def follow_notifcation(request, user_id):

def mention_notifcation(requst, post_id):
    latest_post = Video.objects.latest('timestamp')
    mentions = re.findall(r'@([A-Za-z0-9_]+)', latest_post.comments.body)


'''


def notification_view(request, user_id):
    user = Model.objects.get(id=user_id)
    mention_notifications = Notifications.objects.filter(id=request.user.id).all()
    like_notifications = Notifications.objects.filter(id=request.user.id).all()
    comment_notifications = Notifications.objects.filter(id=request.user.id).all()
    followed_notifications = Notifications.objects.filter(id=request.user.id).all()

    return render(request, 'notifications.html',{
        'comments': comment_notifications,
        'likes': like_notifications,
        'mentions': mention_notifications,
        'followed': followed_notifications
    })

def like_notification(request, post_id):
    user = request.user
    notification_object = notifications.objects.create(
        post = post_id,
        liked = post_id,

    ).mentions.add(post_id.user)
    notification_object.save()