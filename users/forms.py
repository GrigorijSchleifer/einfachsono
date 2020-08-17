from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# this class is a form that inherits from UserCreationForm
# this way we can update and change the UserCreationForm
class UserRegisterForm(UserCreationForm):
    # here we adding an email field
    email = forms.EmailField() # 'required' argument is set here to true, so that the user is providing his/her email

    # class meta is giving us a nested name space and keeps the configurations in one place
    # this will add additional fields to the form
    class Meta:
        # here we specify the model the form will iteract with
        # every time the model is validated it is creating a new user
        # everytime something is happening it will happen to the User
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# creating a "ModelForm" that will allow us to work with a specific database model
# this will allow us to update users username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# this form will allow us to update the update image of the user
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile # Profile IS the model we work with
        fields = ['image']
