from django.contrib.auth import authenticate, login
import random

def auth_user(request, data):
        user = authenticate(request, username=data["email"], password=data["password"])
        if user:
            login(request, user)
            return True
        return False

def check_for_name(name):
    if not name:
        display_name = f"User{random.randint(101010101, 999999999)}"
    else:
        display_name = name
    return display_name

def user_vid_path(instance, filename):
    ext = filename.split(".")[-1]
    return f"@{instance.creator.display_name}/video/{random.randint(690000000, 699999999)}.{ext}"

def user_photo_path(instance, filename):
    ext = filename.split(".")[-1]
    return f"@{instance.display_name}/profile-photos/{random.randint(101010101, 999999999)}.{ext}"

def gen_uuid():
    return random.randint(690000000, 699999999)
