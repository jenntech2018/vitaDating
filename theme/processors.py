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
        notifs = Notifications.objects.filter(to=request.user).order_by('-time_created')
        return {"notifs_all": notifs}
    return {}


def notifications_likes(request):
    if request.user.is_authenticated:
        from notifications.models import Notifications
        notifs = Notifications.objects.filter(to=request.user, n_type="L").order_by('-time_created')
        return {"notifs_likes": notifs}
    return {}


def notifications_comments(request):
    if request.user.is_authenticated:
        from notifications.models import Notifications
        from django.db.models import Q
        notifs = Notifications.objects.filter(Q(n_type="C") | Q(n_type="CL") | Q(n_type="CR"), to=request.user).order_by('-time_created')
        return {"notifs_comments": notifs}
    return {}


def notifications_mentions(request):
    if request.user.is_authenticated:
        from notifications.models import Notifications
        notifs = Notifications.objects.filter(to=request.user, n_type="M").order_by('-time_created')
        return {"notifs_mentions": notifs}
    return {}


def notifications_followers(request):
    if request.user.is_authenticated:
        from notifications.models import Notifications
        notifs = Notifications.objects.filter(to=request.user, n_type="F").order_by('-time_created')
        return {"notifs_followers": notifs}
    return {}


def users_list(request):
    if request.user.is_authenticated:
        from vibe_user.models import Viber
        from django.db.models import Q
        users = Viber.objects.filter(~Q(id=request.user.id)).all()
        return {"users_list": users}
    return {}


def inbox(request):
    if request.user.is_authenticated:
        from vibe_user.models import Viber
        from django.db.models import Q
        from instant.models import Message
        rev = Message.objects.filter(Q(recipient=request.user)|Q(author=request.user)).all().order_by('-pub_date')
        norm = Message.objects.filter(Q(recipient=request.user)|Q(author=request.user)).all().order_by('pub_date')
        authors = {}
        for msg in rev:
            if msg.author.username == request.user.username:
                if msg.recipient.username not in authors:
                    authors[msg.recipient.username] = msg
            elif msg.author.username not in authors:
                authors[msg.author.username] = msg

        sorted_authors = dict(sorted(authors.items(), key=lambda k: k[1].pub_date, reverse=True))

        print(sorted_authors)
        return {"inbox_msgs": norm, "authors": sorted_authors}
    return {}