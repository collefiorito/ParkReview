# filepath: c:\django\ParkReview\ParkReview\urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('mappa/', views.mappa, name='mappa'),
    path('recensioni/', views.recensioni, name='recensioni'),
    path('about/', views.about, name='about'),
]
