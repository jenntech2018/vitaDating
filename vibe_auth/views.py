from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from vibe_auth.forms import LoginForm, AddUser

# Create your views here.
def register_page(request):
    form = AddUser()
    if request.method == 'POST':
        form = AddUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = <usermodel>.objects.create_user(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name'],
            )
            user.follow_users.add(user)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    context = {'form': form}
    return render(request, 'register.html', context)


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse(request.GET.get('next', reverse("home")))))
    form = LoginForm()
    return render(request, "login.html", {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
