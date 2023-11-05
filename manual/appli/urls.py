from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path("about/", views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('chat/', views.chat, name='chat'),
]