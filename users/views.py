from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .forms import EditProfileForm


@login_required
def ViewProfile(request):
    user = request.user
    
    context = {
        'user': user,
        'title': 'Your Profile',
    }
    return render(request, 'profile.html', context)


@login_required
def EditProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/user/profile/')
    else:
        form = EditProfileForm(instance=request.user)

    context = {
        'form': form,
        'title': 'Edit Profile',
    }
    return render(request, 'editprofile.html', context)


@login_required
def ChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('/user/profile/')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {
        'form': form,
        'title': 'Change Password',
    }
    return render(request, 'changepassword.html', context)
