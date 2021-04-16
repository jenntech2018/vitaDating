from django.urls import path
from .views import MessagesView

urlpatterns = [
    path('messages/<str:recipient>/', MessagesView.as_view(), name='msg')
]

