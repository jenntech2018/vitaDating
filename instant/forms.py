from django import forms
from vibe_user.models import Viber

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    recipient = forms.ModelChoiceField(queryset=Viber.objects.all())
 