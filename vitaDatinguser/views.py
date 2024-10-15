from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.db.models import Q
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import AbstractUser
from vitaDatinguser.models import vitaDatinguser
from activity.models import Activity
from vitaDatinguser.forms import EditProfileForm
# Create your views here.

def vitaDatinguser_profile_view(request, username):
    vitaDatinguser = vitaDatinguser.objects.get(username=username)

    if request.user.is_authenticated: 
        following = vitaDatinguser.objects.filter(username=request.user, following=vitaDatinguser)
        is_following = "true" if bool(following) else "false"
    else:
        is_following = "false"
        
    vitaDatingfollowers = vitaDatinguser.followers.all().count
    vitaDatingfollowing = vitaDatinguser.following.all().count

    vitaDatinguser_activitys = Activity.objects.filter(creator=vitaDatinguser).all()

    suggested_creators = vitaDatinguser.objects.all().filter(verified=True).order_by('followers')[:10]
    return render(request, "user/vitaDatingprofile.html", {
        "vitaDatinguser": vitaDatinguser, 
        "vitaDatingfollowers": vitaDatingfollowers,
        "vitaDatingfollowing": vitaDatingfollowing,
        "vitaDatinguser_activitys": vitaDatinguser_activitys,
        "suggested": suggested_creators,
        "is_following": is_following,
        })


@login_required
def vitaDatinguser_follower_view(request, user_id):
    follow = vitaDatinguser.objects.get(id=user_id)
    request.user.followers.add(follow)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    
@login_required
def vitaDatinguser_unfollow_view(request, user_id):
    follow = vitaDatinguser.objects.get(id=user_id)
    request.user.followers.remove(follow)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class EditProfileView(LoginRequiredMixin, View):
    def post(self, request, username):
        user = request.user
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            data = form.cleaned_data
            instance = form.save()
        return HttpResponseRedirect(request.GET.get('next', reverse('profile', args=[user.username])))

    def get(self, request, username):
        user = request.user

        form = EditProfileForm(instance=request.user)
        return render(request, "user/edit_profile.html", {'form': form})


@login_required
def settings_page(request):
    return render(request, 'settings/settings.html', {})

@login_required
def delete_account(request):
    vitaDatinguser.objects.get(id=request.user.id).delete()
    return redirect(reverse("main"))

def search_accounts(request):
    search_query = request.GET["q"]
    results = vitaDatinguser.objects.filter(Q(username__icontains=search_query) | Q(display_name__icontains=search_query))
    return render(request, 'user/search.html', {'query': search_query, 'results': results})