from django import forms
from activity.models import Activity, Sound
from vitaDatinguser.models import vitaDatinguser


CHOICES = [
    ("F", "Friends"),
    ("PRV", "Private"),
    ("PUB", "Public")
]

class UploadForm(forms.ModelForm):
    activity = forms.FileField(widget=forms.FileInput(attrs={"type": "file", "id": "upload-input", "accept": "activity/mp4,activity/webm", "class":"relative block opacity-0 w-full h-full p-20 z-50"}))
    caption = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"type":"text", "id":"caption", "class":"rounded-md h-12 border-gray-200 mt-2 border-2 w-full"}))
    privacy = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={"type":"radio", "class":"form-radio rounded-full h-6 w-6 text-gray-600"}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields["creator"] = forms.ModelChoiceField(queryset=vitaDatinguser.objects.filter(username=self.user.username), required=False)
        self.fields["sound"] = forms.ModelChoiceField(queryset=Sound.objects.all(),widget=forms.Select(attrs={"class": "bg-white border-2 border-gray-400 w-96 h-10"}), required=False)

    class Meta:
        model = Activity
        fields = ("activity", "caption", "privacy", "creator", "sound")
