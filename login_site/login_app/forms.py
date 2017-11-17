from django import forms
from django.contrib.auth.models import User
from login_app.models import UserInfo

class UserBasicForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password','email')

class AdditionalForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('social_site', 'profile_pic')
