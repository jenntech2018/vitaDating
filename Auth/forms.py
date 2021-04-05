from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


NONPROFIT_CHOICES = [
    ('HRC', 'www.humanrightswatch.com'),
    ('MoMA', 'www.moma.org'),
    ('UNICEF', 'www.unicef.org'),
    ('Doctors without borders', 'https://donate.doctorswithoutborders.org/medicalcare/donatenow'),
    ('Rotary International', 'www.rotary.org'),
    ('ACLU', 'www.aclu.org'),
]
class AddUser(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    display_name = forms.CharField(max_length=60)
    bio = forms.CharField(max_length=180)
    nonprofit = forms.ChoiceField(choices=NONPROFIT_CHOICES, required=False)
    instagram_link = forms.URLField(max_length=180)
    youtube_link = forms.URLField(max_length=180)
    profile_photo = forms.ImageField(upload_to='/photos/')