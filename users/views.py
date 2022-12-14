from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisteration, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(response):
    if response.method == "POST":
        form = UserRegisteration(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, f'ACCOUNT CREATED SUCCESSFULLY')
            return redirect('login')
    else:
        form = UserRegisteration()
    return render(response, 'users/register.html', {'form': form})


@login_required()
def profile(response):
    if response.method == 'POST':
        u_form = UserUpdateForm(response.POST, instance=response.user)
        p_form = ProfileUpdateForm(response.POST, response.FILES, instance=response.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save() and p_form.save()
            messages.success(response, f'ACCOUNT UPDATED SUCCESSFULLY')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=response.user)
        p_form = ProfileUpdateForm(instance=response.user.profile)
    context = {
        'title': 'Profile',
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(response, 'users/profile.html', context)
