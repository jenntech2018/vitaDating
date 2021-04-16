from django import forms
from vibe_user.models import Viber
# from vibetube.helpers import user_photo_path

class EditProfileForm(forms.Form):
    display_name = forms.CharField(max_length=120, required=False)
    bio =  forms.CharField(widget=forms.Textarea)
    # profile_photo = forms.ImageField(upload_to=user_photo_path, null=True, blank=True, required=False)
    first_name = forms.CharField(max_length=40, required=False)
    last_name = forms.CharField(max_length=40, required=False)
    username = forms.CharField(max_length=20, required=False)