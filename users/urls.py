from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.ViewProfile, name='profile'),
    path('edit-profile/', views.EditProfile, name='edit-profile'),
    path('change-password/', views.ChangePassword, name='change-password'),
]