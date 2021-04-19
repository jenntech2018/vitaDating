from django.urls import path
from .views import MessagesView

urlpatterns = [
    path('messages/', MessagesView.messages_main, name='messages'),
    path('messages/new/', MessagesView.new_message, name='new'),
    path('messages/message/<int:author>/', MessagesView.user_messages_view, name='usrs'),
]

