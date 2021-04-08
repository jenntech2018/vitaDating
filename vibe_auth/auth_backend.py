from django.conf import settings

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

from vibe_user.models import Viber

class SettingsBackend(BaseBackend):
    def authenticate(self, request, username=None, email=None, display_name=None, password=None):
        if email: user = Viber.objects.get(username=email)
        elif display_name: user = Viber.objects.get(display_name=display_name)
        
        if password:
            try:
                user = Viber.objects.get(username=email)
                password_valid = check_password(password, user.password)
                if password_valid:
                    return user
            except Viber.DoesNotExist:
                return None
        return None

    def get_user(self, user_id):
        try:
            return Viber.objects.get(pk=user_id)
        except Viber.DoesNotExist:
            return None