from django.urls import path
from . import views

urlpatterns = [
    path('', views.LogIn, name='log-in'),
    path('home/', views.Dashboard, name='dashboard'),
]
