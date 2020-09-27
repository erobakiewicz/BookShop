from django import forms
from django.contrib.auth.models import User


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', ]
