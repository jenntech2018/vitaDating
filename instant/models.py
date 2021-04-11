from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from vibe_user.models import Viber


class Chat(models.Model):
    DIALOG = 'D'
    CHAT = 'C'
    CHAT_TYPE_CHOICES = (
        (DIALOG, 'Dialog'),
        (CHAT, 'Chat')
    )

    type = models.CharField(
        max_length=1,
        choices=CHAT_TYPE_CHOICES,
        default=DIALOG
    )
    members = models.ManyToManyField(Viber, verbose_name="Member")
 
    def get_absolute_url(self):
        return 'users:messages', (), {'chat_id': self.pk }
 
 
class Message(models.Model):
    author = models.ForeignKey(Viber, verbose_name='viber', on_delete=models.CASCADE)
    message = models.TextField(max_length=280)
    pub_date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering=['pub_date']

    def __str__(self):
        return self.message

