from django.shortcuts import render

def ContactView(request):
    return render(request, 'home/contact.html')