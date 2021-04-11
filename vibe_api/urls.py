from django.urls import include, path
from rest_framework import routers
from vibe_api import views

router = routers.DefaultRouter()
router.register(r"vibers", views.ViberViewSet)
router.register(r"videos", views.VideoViewSet)
router.register(r"sounds", views.SoundViewSet)


urlpatterns = [
    path('api-vibes/', include(router.urls)),
]