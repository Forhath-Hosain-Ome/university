from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import registerForm,login_Auth


# Create your views here.
def login_form(request):
    if request.method == 'POST':
        form = login_Auth(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login_Auth(request, user)
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
    form = registerForm()
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = registerForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/register.html', context)

def profile(request):
    return render(request, 'accounts/profile.html')
