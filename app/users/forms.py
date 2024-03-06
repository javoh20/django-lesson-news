from typing import Any
from django import forms
from django.contrib.auth.models import User
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 100)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.ModelForm):
    password_1 = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name')

    def clean_password(self):
        data = self.cleaned_data
        if data['password_1'] != data['password_2']:
            raise forms.ValidationError('Different passwords')
        return data['password_2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo','date_of_birth')