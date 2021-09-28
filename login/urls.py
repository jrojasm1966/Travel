from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('validainicio', views.validainicio, name='validainicio'),
    path('registro', views.registro, name='registro'),
    path('logout', views.logout, name='logout'),
    path('recuperar_pass', views.recuperar_pass, name='recuperar_pass'),
    path('cambiar_pass', views.cambiar_pass, name='cambiar_pass'),
]