from django.shortcuts import render

def AboutView(request):
    return render(request, 'home/about.html')