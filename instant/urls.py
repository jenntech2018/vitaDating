from django.urls import path
from .views import MessagesView

urlpatterns = [
    path('messages/new/', MessagesView.new_message, name='new'),
    path('messages/<int:recipient>/', MessagesView.as_view(), name='msg')
]

