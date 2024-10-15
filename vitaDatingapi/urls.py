from django.urls import include, path
from rest_framework import routers
from vitaDatingapi import views

router = routers.DefaultRouter()
router.register(r"vitaDatingusers", views.vitaDatinguserViewSet)
router.register(r"activities", views.activityViewSet)
router.register(r"sounds", views.SoundViewSet)
router.register(r"auth", views.AuthViewSet)
router.register(r"comments", views.CommentViewSet)
router.register(r"messages", views.MessageViewSet)


urlpatterns = [
    path('api-vibes/', include(router.urls)),
]