from django import forms
from video.models import Video

CHOICES = [
    ("F", "Friends"),
    ("PRV", "Private"),
    ("PUB", "Public")
]

class UploadForm(forms.ModelForm):
    video = forms.FileField(widget=forms.FileInput(attrs={"type": "file", "id": "upload-input", "accept": "video/mp4,video/webm", "class":"relative block opacity-0 w-full h-full p-20 z-50"}))
    caption = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"type":"text", "id":"caption", "class":"rounded-md h-12 border-gray-200 mt-2 border-2 w-full"}))
    privacy_settings = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={"type":"radio", "class":"form-radio rounded-full h-6 w-6 text-gray-600"}))

    class Meta:
        model = Video
        fields = ("video", "caption", "privacy_settings")