from django.contrib import admin
from vitaDatinguser.models import vitaDatinguser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# Register your models here.

class vitaDatinguserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = vitaDatinguser
    list_display = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'bio', 'website', 'display_name', 'verified', 'profile_photo']
    fieldsets = [
        (None, {'fields': ('username',  'password', 'email', 'first_name', 'last_name', 'bio', 'website', 'display_name', 'verified', 'profile_photo')})
    ]

admin.site.register(vitaDatinguser, vitaDatinguserAdmin)