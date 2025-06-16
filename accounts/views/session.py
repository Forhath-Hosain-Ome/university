from django.shortcuts import redirect, render
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User


from .forms import registerForm,login_Auth



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


def logout_view(request):
    logout(request)
    return redirect('home:home')