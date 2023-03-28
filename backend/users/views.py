from django.shortcuts import render, redirect
from django import forms
from django.http import HttpRequest, HttpResponse
from rest_framework.generics import *
from .models import User

from .serializers import ProfileSerializer




# Create your views here.

class ProfileForm(forms.Form):
    username = forms.CharField(max_length=80)
    username = forms.CharField(max_length=80)
    bio = forms.TextInput()
    country = forms.CharField(max_length=40)
    birth = forms.DateField()
    twitter = forms.URLField(max_length=200)
    linkedin = forms.URLField(max_length=200)
    instagram = forms.URLField(max_length=200)
    # behance = forms.URLField(max_length=200)





def EditProfile(request):


    lista = []
    # def __valid_form(obj):



    set_profile = ProfileForm()
    # print(user)
    user = request.user
    dic = {'user': user, 'form': set_profile}
    if request.method == 'GET':




        # po = dict(user)

        print(dir(request.user))
        print(dir(request))
        return render(request, 'account/edit_profile.html', context=dic)


    else:

        username = request.POST.get('username')
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        country = request.POST.get('country')
        birth = request.POST.get('birth')
        linkedin = request.POST.get('linkedin')
        instagram = request.POST.get('instagram')
        twitter = request.POST.get('twitter')
        behance = request.POST.get('behance')


        # validate_and_execute = lambda x: None if x else pass




    return render(request, 'account/edit_profile.html', context=dic)







class Profileview(ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        nick = self.kwargs.get('username')
        queryset = User.objects.filter(username=nick)
        print((self.request.user.username))
        if nick == (self.request.user.username):
            redirect('myuser/')
        else:

            return queryset






