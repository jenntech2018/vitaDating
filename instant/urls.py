from django.urls import path
from .views import MessagesView

urlpatterns = [
    path('messages/<int:chat_id>/', MessagesView.as_view(), name='msg')
]

