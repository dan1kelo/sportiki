from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
urlpatterns  = [
    path('', views.regPage, name='reg'),
    path('calendar/', views.calendarPage, name='calendar'),
    
    
]