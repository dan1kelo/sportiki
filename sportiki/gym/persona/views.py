from django.shortcuts import render

def profilePage(request):
    return render(request, 'persona/profile.html')
# Create your views here.
