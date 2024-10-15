from django.conf import settings

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

from vitaDatinguser.models import vitaDatinguser

class SettingsBackend(BaseBackend):
    def authenticate(self, request, username=None, email=None, password=None):
        username = username
        if email: user = vitaDatinguser.objects.get(email__iexact=email)
        else: user = vitaDatinguser.objects.filter(username__iexact=username).first()
        
        if password:
            try:
                password_valid = check_password(password, user.password)
                if password_valid:
                    return user
            except vitaDatinguser.DoesNotExist:
                return None
        return None

    def get_user(self, user_id):
        try:
            return vitaDatinguser.objects.get(pk=user_id)
        except vitaDatinguser.DoesNotExist:
            return None