from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import *
# from .views import ArtViewSet



# router = DefaultRouter()
# router.register(r'', ArtViewSet, base_name='livros')

# livros_urls = router.urls


urlpatterns = [
    path("newart/", views.artcreate, name='createart'),
    path("artup/", views.art_update, name='art_update'),
    path('bb/', views.Art_api_view),
    path('arts/<int:idart>/', views.artAccess, name='art_url'),
    path('popo/<int:pk>/', views.teste, name='Art-list'),
    path('teste/', views.teste_api_art, name='teste'),
    path('testee/', Art_api_view)
]
