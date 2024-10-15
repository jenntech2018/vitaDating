from django.contrib import admin

from activity.models import Activity, Comment, Sound
# Register your models here.
admin.site.register(Activity)
admin.site.register(Comment)
admin.site.register(Sound)
