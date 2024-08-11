from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from user.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'u-clearfix', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'u-clearfix', 'placeholder': 'Пароль'}))

    class Meta:
        model = User
        field = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'u-clearfix', 'placeholder': 'Имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'u-clearfix', 'placeholder': 'Почта'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'u-clearfix', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'u-clearfix', 'placeholder': 'Подтвердить пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserCabinetForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'u-clearfix', 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'u-clearfix'}), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'u-align-center u-text u-text-1'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image')