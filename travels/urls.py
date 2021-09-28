from django.urls import path, include
from . import views

urlpatterns = [
    path('travels', views.travels, name='travels'),
    path('despliegatravels', views.despliegatravels, name='despliegatravels'),
    path('travels/createtravel', views.createtravel, name='createtravel'),
    path('travels/destination', views.capturatravel, name='capturatravel'),
    path('travels/add', views.ingresatravel, name='ingresatravel'),
    path('updatetravel', views.updatetravel, name='updatetravel'),
]
