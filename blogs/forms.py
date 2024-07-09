from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User
from .models import Blog, Review

from django import forms

from django.forms. widgets import PasswordInput, TextInput


# create a new user (modelForm)
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]


class LogUserForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)


class BlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'


class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['blog']


