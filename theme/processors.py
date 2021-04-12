def base_login_form(request):
    from vibe_auth.forms import LoginForm
    form = LoginForm()
    return {"login_form": form}


def base_register_form(request):
    from vibe_auth.forms import RegistrationForm
    form = RegistrationForm()
    return {"registration_form": form}


def notifications_all(request):
    if request.user.is_authenticated:
        from notifications.models import Notifications
        notifs = Notifications.objects.filter(to=request.user)
        return {"notifs_all": notifs}
    return {}


def notifications_likes(request):
    if request.user.is_authenticated:
        from notifications.models import Notifications
        notifs = Notifications.objects.filter(to=request.user, n_type="L")
        return {"notifs_likes": notifs}
    return {}


def notifications_comments(request):
    if request.user.is_authenticated:
        from notifications.models import Notifications
        from django.db.models import Q
        notifs = Notifications.objects.filter(Q(n_type="C") | Q(n_type="CL") | Q(n_type="CR"), to=request.user)
        return {"notifs_comments": notifs}
    return {}


def notifications_mentions(request):
    if request.user.is_authenticated:
        from notifications.models import Notifications
        notifs = Notifications.objects.filter(to=request.user, n_type="M")
        return {"notifs_mentions": notifs}
    return {}


def notifications_followers(request):
    if request.user.is_authenticated:
        from notifications.models import Notifications
        notifs = Notifications.objects.filter(to=request.user, n_type="F")
        return {"notifs_followers": notifs}
    return {}