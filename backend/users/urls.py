from django.urls import path
from . import views



urlpatterns = [

    path("editprofile/", views.EditProfile, name='edit_profile'),

]
