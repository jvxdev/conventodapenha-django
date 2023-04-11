from django.contrib import admin
from django.urls import path
from conventodapenha.views import home, conhecaumpoucomais

urlpatterns = [
    path('', home),
    path('conventodapenha/', conhecaumpoucomais)
]
