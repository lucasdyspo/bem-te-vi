from django.urls import path
from . import views


urlpatterns = [
    path("", views.login, name='login'),
    path('validar_cadastro/', views.validar_cadastro, name='validar_cadastro'),
    path('sologin/', views.sologin, name='sologin'),
    path('loginfeito/', views.validar_login, name="validar_login"),
    path('home/', views.myhome, name="home"),
    path('alter_profile2/', views.alter_profile2, name="alter_profile2")
    
]