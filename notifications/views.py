# from django.shortcuts import render, reverse, HttpResponseRedirect
# from notifications.models import Notifications

# from vitaDatinguser.models import vitaDatinguser
# from activity.models import activity

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
    latest_post = activity.objects.latest('timestamp')
    mentions = re.findall(r'@([A-Za-z0-9_]+)', latest_post.comments.body)

testing:

from activity.models import activity
from vitaDatinguser.models import vitaDatinguser
from notifications.models import Notifications

from vitaDatinguser.models import vitaDatinguser:
    display_name = models.CharField(max_length=120, null=True, blank=True)
    bio = models.TextField()
    dob = models.DateField(blank=True,null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='vitaDatinguser_followers')
    following = models.ManyToManyField('self', symmetrical=False, related_name='vitaDatinguser_following')
    activities = models.ManyToManyField(activity, related_name='vitaDatinguser_activitys')
    # sound = models.ManyToManyField('self', symmetrical=False, related_name='vitaDatinguser_sound')
    profile_photo = models.ImageField(upload_to=user_photo_path, blank=True, null=True)

from activity.models import activity:
    creator = models.ForeignKey('vitaDatinguser.vitaDatinguser', null=True, blank=True, on_delete=models.CASCADE, related_name="activity_creator")
    activity = models.FileField(upload_to=user_vid_path)
    uuid = models.IntegerField(default=gen_uuid, unique=True)
    privacy = models.CharField(max_length=3,choices=PRIVACY_SETTINGS)
    comments = models.ManyToManyField("Comment", blank=True)
    likes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now)
    caption = models.CharField(max_length=70)

notification creation:
- create an object that has a foreign key relationship to a post
  ex: n = MentionNotifications.objects.create(post=activity1)

- add a user to the sender property who is being mentioned
  ex: n.sender = user1 // user1 is being mentioned @user1

- add the user doing the mentioning to another property
  ex: n.reciever = user2 // person typeing the @user1

  n.mentions.all()
<QuerySet [<vitaDatinguser: VitaDatingz@gmail.com>]>

  n.mentions.filter(id=1)
<QuerySet [<vitaDatinguser: VitaDatingz@gmail.com>]>
'''


# def notification_view(request):
#     notifs = Notifications.objects.all()

#     blips = 'notifications/blips.html'
#     return render(request, blips, {
#         'notifs': notifs,
#     })


# def like_notification(request):
#     vid = activity.objects.get(id=1)
#     Notifications.objects.create(
#       n_type='L',
#       activity=vid,
#       sender=request.user.id,
#       reciever=request.user.id
#     )
#     return HttpResponseRedirect(request.GET.get('next', reverse('blips')))
