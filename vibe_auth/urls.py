from django.urls import path
from vibe_auth.views import logout_view

urlpatterns = [
    path('logout', logout_view, name='logout'),
]