from django.shortcuts import render,redirect
from .forms import registerForm


# Create your views here.
def login(request):
    
    return render(request, 'accounts/login.html')

def register(request):
    form = registerForm()
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = registerForm()
    return render(request, 'accounts/register.html', {'form' : form})

def profile(request):
    return render(request, 'accounts/profile.html')

def profile(request):
    return render(request, 'accounts/profile.html')