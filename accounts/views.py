from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import registerForm,login_Auth
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def login_form(request):
    if request.method == 'POST':
        form = login_Auth(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data.get('identifier')
            password = form.cleaned_data.get('password')

            if identifier is not None and '@' in identifier:
                try:
                    user_obj = User.objects.get(email=identifier)
                    username = user_obj.username
                except User.DoesNotExist:
                    username = None
            else:
                username = identifier


            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:home')
            else:
                form.add_error(None, "Invalid email or password")
    else:
        form = login_Auth()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
        else:
            messages.error(request,"Please enter valid data")
    else:
        form = registerForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/register.html', context)

def profile(request):
    return render(request, 'accounts/profile.html')

def logout_view(request):
    logout(request)
    return redirect('home:home')