# urls.py -- profiles
from django.urls import path
from . import views

urlpatterns = [
    path('profile/<slug:username>/', views.user_profile_page, name='user_profile_page'),
    path('profile/<slug:username>/edit/', views.user_profile_edit_page, name='user_profile_edit_page'),
    ]