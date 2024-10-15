from django import forms
from vitaDatinguser.models import vitaDatinguser
# from VitaDating.helpers import user_photo_path

class EditProfileForm(forms.ModelForm):
    username = forms.CharField(required=False, max_length=32, help_text=None, widget=forms.TextInput(attrs={"type":"text", "class":"box-right-inner-general-inputs"}))
    display_name = forms.CharField(required=False, max_length=64, widget=forms.TextInput(attrs={"type":"text", "class":"box-right-inner-general-inputs"}))
    bio = forms.CharField(required=False, max_length=80, widget=forms.Textarea(attrs={"rows": "3", "cols": "22","type":"text", "class":"box-right-inner-general-inputs"}))
    email = forms.CharField(required=False, max_length=80, widget=forms.TextInput(attrs={"type":"email", "class":"box-right-inner-general-inputs"}))
    profile_photo = forms.ImageField(label="", required=False, widget=forms.FileInput(attrs={"id":"edit-pfp", "type":"file", "style":"font-size: 0; opacity: 0; top: 3.95rem; right: 19rem;", "class":"opacity-100 absolute w-8 h-8 cursor-pointer", "accept":"image/png,image/jpeg,image/jpg"}))
    website = forms.CharField(required=False, max_length=64, widget=forms.TextInput(attrs={"type":"url", "class":"box-right-inner-general-inputs"}))

    class Meta:
        model = vitaDatinguser
        fields = ("username", "display_name", "bio", "email", "profile_photo", "website")