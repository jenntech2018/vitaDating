from django import forms
from vitaDatinguser.models import vitaDatinguser

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    recipient = forms.ModelChoiceField(queryset=vitaDatinguser.objects.all())
 