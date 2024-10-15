"""VitaDating URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

from main.urls import urlpatterns as main_urls
from activity.urls import urlpatterns as activity_urls
from vitaDatinguser.urls import urlpatterns as user_urls
from vitaDatingauth.urls import urlpatterns as auth_urls
from vitaDatingauth import views as auth_views
from vitaDatingapi.urls import urlpatterns as api_urls


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += main_urls
urlpatterns += activity_urls
urlpatterns += user_urls
urlpatterns += auth_urls
urlpatterns += api_urls
handler404 = auth_views.error_404
handler500 = auth_views.error_500

urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)

