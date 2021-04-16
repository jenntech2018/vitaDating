from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from vibe_user.models import Viber
from vibetube import settings


class Message(models.Model):
    author = models.ForeignKey(Viber, verbose_name='sender', on_delete=models.CASCADE)
    message = models.TextField(max_length=280)
    pub_date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    recipient = models.ForeignKey(Viber, related_name='recipient', on_delete=models.CASCADE)
    
    class Meta:
        ordering=['pub_date']

    def __str__(self):
        return self.message

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
    chat_id = models.ManyToManyField(Message, verbose_name="messages")
    def get_absolute_url(self):
        return 'users:messages', (), {'chat_id': self.pk }
 
 
