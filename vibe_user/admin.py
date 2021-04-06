from django.contrib import admin
from vibe_user.models import Viber
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# Register your models here.

class ViberAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = Viber
    list_display = ['email', 'username', 'first_name', 'last_name', 'display_name']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name', 'display_name',)}),
    )
    fieldsets = UserAdmin.fieldsets

admin.site.register(Viber, ViberAdmin)