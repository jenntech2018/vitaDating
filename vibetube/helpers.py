from django.contrib.auth import authenticate, login

import random

def auth_user(request, data):
        if '@' in data['username']:
            user = authenticate(request, email=data['username'], password=data["password"])
        else: 
            user = authenticate(request, username=data['username'], password=data["password"])

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

def check_for_username(name, display_name):
    if not name: return display_name
    else: return name

def user_vid_path(instance, filename):
    ext = filename.split(".")[-1]
    return f"@{instance.creator.username}/video/{instance.uuid}.{ext}"

def user_sound_path(instance, filename):
    ext = filename.split(".")[-1]
    return f"@{instance.creator.username}/sound/{instance.original_video.uuid}.{ext}"

def user_photo_path(instance, filename):
    ext = filename.split(".")[-1]
    return f"@{instance.username}/profile-photos/{random.randint(101010101, 999999999)}.{ext}"

def gen_uuid():
    return random.randint(690000000, 699999999)
