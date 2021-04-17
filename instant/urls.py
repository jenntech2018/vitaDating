from django.urls import path
from .views import MessagesView

urlpatterns = [
    path('messages/<int:recipient>/', MessagesView.as_view(), name='main'),
    path('messages/new/', MessagesView.new_message, name='new'),
    path('messages/message/<int:author>/', MessagesView.user_messages_view, name='usrs'),
]

