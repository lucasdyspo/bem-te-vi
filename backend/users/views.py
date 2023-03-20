from django.shortcuts import render  # noqa
from django import forms
from django.http import HttpRequest, HttpResponse




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
        set_profile = ProfileForm
        form_profile = set_profile(request.POST)
        # print(dir(form_profile))
        print(dir(form_profile.data))
        print(dir(form_profile.visible_fields()))
    return render(request, 'account/edit_profile.html', context=dic)
