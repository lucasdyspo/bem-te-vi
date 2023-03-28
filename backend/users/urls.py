from django.urls import path
from . import views



urlpatterns = [

    path("editprofile/", views.EditProfile, name='edit_profile'),
    path("profile/<str:username>/", views.Profileview.as_view(), name='profile')

]
