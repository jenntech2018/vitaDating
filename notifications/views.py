from django.shortcuts import render, reverse, HttpResponseRedirect
# from notifications.models import Notifications, LikedNotifications, CommentedNotifications, FollowedNotifications
from notifications.models import Notifications

from vibe_user.models import Viber
from video.models import Video

# Create your views here.
'''
// call this function when like button is pressed
def like_notification(request, post_id):

// call this function when comment is made
def comment_notification(request, post_id):

// call this functions when follow button is pressed
def follow_notifcation(request, user_id):

// call this function when comment is made to check for mentions
def mention_notifcation(requst, post_id):
    latest_post = Video.objects.latest('timestamp')
    mentions = re.findall(r'@([A-Za-z0-9_]+)', latest_post.comments.body)

testing:

from video.models import Video
from vibe_user.models import Viber
from notifications.models import Notifications, LikedNotifications, CommentedNotifications, FollowedNotifications

from vibe_user.models import Viber:
    display_name = models.CharField(max_length=120, null=True, blank=True)
    bio = models.TextField()
    dob = models.DateField(blank=True,null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='viber_followers')
    following = models.ManyToManyField('self', symmetrical=False, related_name='viber_following')
    videos = models.ManyToManyField(Video, related_name='viber_videos')
    # sound = models.ManyToManyField('self', symmetrical=False, related_name='viber_sound')
    profile_photo = models.ImageField(upload_to=user_photo_path, blank=True, null=True)

from notifications.models import Notifications:
    time_created = models.DateTimeField(default=timezone.now)
    mentions = models.ManyToManyField(Viber, symmetrical=False, related_name='mentions')
    post = models.ForeignKey(Video, on_delete=models.CASCADE)
    liked = models.ManyToManyField(Viber, symmetrical=False, related_name='liked')
    Commented = models.ManyToManyField(Viber, symmetrical=False, related_name='commented')
    followed = models.ManyToManyField(Viber, symmetrical=False, related_name='followed')


from video.models import Video:
    creator = models.ForeignKey('vibe_user.Viber', null=True, blank=True, on_delete=models.CASCADE, related_name="video_creator")
    video = models.FileField(upload_to=user_vid_path)
    uuid = models.IntegerField(default=gen_uuid, unique=True)
    privacy = models.CharField(max_length=3,choices=PRIVACY_SETTINGS)
    comments = models.ManyToManyField("Comment", blank=True)
    likes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now)
    caption = models.CharField(max_length=70)

notification creation:
- create an object that has a foreign key relationship to a post
  ex: n = MentionNotifications.objects.create(post=video1)

- add a user to the mention propery who is being mentioned
  ex: n.mentions.add(user1) // user1 is being mentioned @user1

- add the user doing the mentioning to another property
  ex: n.user.add(request.user) // person typeing the @user1

  n.mentions.all()
<QuerySet [<Viber: vibetubez@gmail.com>]>

  n.mentions.filter(id=1)
<QuerySet [<Viber: vibetubez@gmail.com>]>
'''


def notification_view(request):
    notifs = Notifications.objects.filter(id=request.user.id)

    blips = 'notifications/blips.html'
    return render(request, blips, {
        'notifs': notifs,
    })


def like_notification(request):

    return HttpResponseRedirect(request.GET.get('next', reverse('blips')))
