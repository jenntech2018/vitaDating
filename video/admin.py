from django.contrib import admin

from video.models import Video, Comment, Sound
# Register your models here.
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Sound)
