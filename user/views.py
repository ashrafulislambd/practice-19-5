from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from .forms import SignupForm

def index(request):
    return render(request, "users/index.html")

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, message="Successfully created user")
            return redirect(reverse("music:index"))
    else:
        form = SignupForm()
    return render(request, "users/signup.html", {"form": form})

@login_required
def profile(request):
    return render(request, "users/profile.html")

def LogOut(request):
    logout(request)
    messages.success(request, message="Logged out successfully")
    return redirect(reverse("music:index"))

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('users:profile')
    
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'users/change_password.html', {'form' : form})

@login_required
def set_password(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('users:profile')
    
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'users/change_password.html', {'form' : form})
    

class UserLoginView(LoginView):
    def get_success_url(self):
        messages.success(self.request, message="Logged in Successfully")
        return reverse("music:index")
    
    template_name = "users/login.html"