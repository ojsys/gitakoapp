from django.contrib import admin
from django.urls import path
from authentication import views

urlpatterns = [
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
]
