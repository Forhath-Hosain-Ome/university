from django.shortcuts import render,redirect
from .forms import registerForm,login_Auth
from django.contrib import messages

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