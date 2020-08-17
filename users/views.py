from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages # to get/send flash messages (messages.debug/messages.warning/messages.error/messages.info)
from .forms import (
    # removing "from django.contrib.auth.forms import UserCreationForm"
    # importing the updated User creation form with added email fields
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm
)

def register(request):
    # in order to store the data the POST request needs to be evaluated
    # a registration form is submitted as a POST request
    if request.method == 'POST':
        # to add fields to a form we need to create another separate
        # here we added an email field to the registration form
        # the instance of UserCreationForm will have POST request data incorporated
        # UserRegisterForm will inherit from UserCreationForm and contail additional fields
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # saving = creating the user, hashing passwords
            form.save()
            # gets username
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in')
            # this will redirect the user to another location after submission
            return redirect('login')
    else:
        # will create an instance of UserCreationForm that will be passed to a template so it can be rendered
        # if it is not a POST request, the instance will be just a blanc form
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        # creating instances of the forms
        u_form = UserUpdateForm(request.POST, instance=request.user) # instance will populate the fields with users information
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) # populate with the users prifile picture
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    # passing the instances to our template by creating a context dictionary
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
