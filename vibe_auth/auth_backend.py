from django.conf import settings

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

from vibe_user.models import Viber

class SettingsBackend(BaseBackend):
    def authenticate(self, request, username=None, email=None, password=None):
        username = username
        if email: user = Viber.objects.get(email__iexact=email)
        else: user = Viber.objects.filter(username__iexact=username).first()
        
        if password:
            try:
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