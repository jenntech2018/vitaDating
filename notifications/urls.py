from django.urls import path
from notifications.views import notification_view

url_patterns = [
    path('blips', notification_view, name='blips')
 ]

#  somethingsdfsdf