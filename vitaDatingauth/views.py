from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from vitaDatingauth.forms import LoginForm, RegistrationForm
from vitaDatinguser.models import vitaDatinguser
from VitaDating.helpers import auth_user

# Create your views here.
def register_page(request):
    form = AddUser()
    if request.method == 'POST':
        form = AddUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = vitaDatinguser.objects.create_user(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name'],
            )
            user.follow_users.add(user)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('register'))
    form = AddUser()
    return render(request, 'auth/register.html', {'form': form} )


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            is_authed = auth_user(request, data)
            if is_authed:
                return redirect(reverse("main"))
    form = LoginForm()
    return render(request, "auth/login.html", {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('main'))

def error_404(request, exception):
    return render(request, 'auth/404.html')

def error_500(request):
    return render(request, 'auth/500.html')
