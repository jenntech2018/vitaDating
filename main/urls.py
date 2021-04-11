from django.urls import path
from main.views import MainView
from vibe_auth.views import login_page, register_page
from instant.views import MessagesView
urlpatterns = [
    path('message/', MessagesView.as_view(), name='message'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path("", MainView.as_view(), name="main")
]