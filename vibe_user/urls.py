from django.urls import path
from vibe_user import views

urlpatterns = [
    path('@<str:username>', views.vibe_user_profile_view, name='profile'),
    path('settings', views.settings_page, name='settings')
]