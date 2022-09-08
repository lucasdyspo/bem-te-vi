from django.urls import path, re_path
from . import views


urlpatterns = [

    path("", views.home, name='home'),
    path("search<str:search>", views.search, name='search'),
    path("?search=<str:search>", views.testezin, name='search'),
    path("settings/", views.settings, name='settings'),
    path("friends/", views.social, name='social'),
    path("favorites/", views.list_favorites, name='favorites'),
    path("myuser/", views.myuser, name='myuser'),
    path("insights/", views.myinsights, name='myinsights')
    
    
    
    ]
    

    # http://127.0.0.1:8000/home/?search=hhhh

    # http://127.0.0.1:8000/home/
    # home/?search=loiiiiiiiill
    # http://127.0.0.1:8000/home/?search=lucasgabriel400%40ymail.com
    # http://127.0.0.1:8000/home/search/pao
    
    
    # def home(request):
    #     return render(request, 'home.html')
