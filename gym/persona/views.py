from django.shortcuts import render

def regPage(request):
    return render(request, 'persona/reg.html')

def calendarPage(request):
    return render(request, 'persona/calendar.html')


