from django.urls import path
from . import views
ulrlpatterns = [
    path('profile/', views.profilePage, name='profile'),
    
    
]