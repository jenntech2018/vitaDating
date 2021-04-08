def base_login_form(request):
    from vibe_auth.forms import LoginForm
    form = LoginForm()
    return {"login_form": form}


def base_register_form(request):
    from vibe_auth.forms import RegistrationForm
    form = RegistrationForm()
    return {"registration_form": form}