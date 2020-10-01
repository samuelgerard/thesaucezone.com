from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#class that inherits form djangos user creation form
#adds things like requiring an email in the email field and sets up meta data from the user
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #default bool requires there to be an email

    class Meta:
        model = User #whenever this form validates, creates a new user
        fields = ['username','email','password1','password2']

#allows to update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() #default bool requires there to be an email

    class Meta:
        model = User #whenever this form validates, creates a new user
        fields = ['username','email']

#allows to update profile picture
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']