from django.shortcuts import render

def Privacy_PolicyView(request):
    return render(request, 'home/privacy_policy.html')