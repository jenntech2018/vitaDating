from django.contrib.auth import authenticate, login
import random


def handle_create_user(data):
    display_name = check_for_name(data["display_name"])
    username = check_for_username(data['username'], display_name)
    dob = datetime.date(int(data["year"]), int(data["month"]), int(data["day"]))

    Viber.objects.create_user(
        username=username,
        email=data["email"],
        password=data["password"],
        dob=dob,
        display_name=display_name,
        profile_photo=data["profile_photo"])
    return

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
    return f"@{instance.creator.display_name}/video/{random.randint(690000000, 699999999)}.{ext}"

def user_photo_path(instance, filename):
    ext = filename.split(".")[-1]
    return f"@{instance.display_name}/profile-photos/{random.randint(101010101, 999999999)}.{ext}"

def gen_uuid():
    return random.randint(690000000, 699999999)
