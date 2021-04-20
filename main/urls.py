from django.urls import path
from main.views import MainView
from vibe_auth.views import login_page, register_page
from django.views.static import serve

urlpatterns = [
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path("", MainView.as_view(), name="main"),
]