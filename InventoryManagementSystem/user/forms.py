from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#form for the new registration of the staff
class CreateUserForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']

#form for the updation of the staff profile ( their username and email )
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model= User
        fields=['username','email']

#form for the profile updation of staff ( their address, phone and profile picture )
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address', 'phone','image']