from django.contrib.auth.forms import AuthenticationForm

from django.forms import CharField, TextInput, PasswordInput


class UserLoginForm(AuthenticationForm):
    username = CharField(label='User Name', widget=TextInput(attrs={'class': 'form-control'}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control'}))
