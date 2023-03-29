from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField
from django.forms import NumberInput

from .models import User

class LoginForm(forms.Form):
    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'birth_date',
        ]
        # widgets = {
        #     'birth_date': forms.DateField(widget=NumberInput(attrs={'type': 'date'})),
        # }


class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'username',
            'image',
            'email',
            'address',
            'birth_date',
        ]

