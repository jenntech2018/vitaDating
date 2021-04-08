from django.urls import path
from vibe_user import views

urlpatterns = [
    path('profile/<int:user_id>', views.vibe_user_profile_view, name='profile'),
]