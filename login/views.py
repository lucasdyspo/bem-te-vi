from django import views
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Usuario, Img_test
from django import forms
from img import *
from rest_framework.views import APIView, Response


class teste:
    num = 1
    string = 'rooolaaaa'
        


class profileChanges(forms.Form):
    vulgo = forms.CharField(max_length=80)
    bio = forms.TextInput()
    # photo

class form_login(forms.Form):
    vulgo = forms.CharField(max_length=80)
    password = forms.PasswordInput()
    senha = forms.CharField(max_length=80)
    
class form_register(forms.Form):
    remail = forms.CharField(max_length=80) #change for type as email
    rname = forms.CharField(max_length=120)
    rvulgo = forms.CharField(max_length=80)
    rpassword = forms.CharField(max_length=80)
    # sexo = forms.BooleanField(required=True)
    
    
    
    
# Create your views here.
def login(request):
    i = Usuario.objects.filter(nome__contains='o')
    print(i)
    if request.method == 'GET':
        register = form_register()
        login = form_login()
        
        form1 = {'formreg': register, 'formlog': login}
        
        
        print("esse metodo foi GET\n\n\n\n\n")               
        
    
        return render(request, 'login_page.html', context=form1)
    
    
    
    
    else:
        print("esse metodo foi POST \n\n\n\n\n")
        login = form_login(request.POST)
        resgister = form_register(request.POST)
        form1 = {}
        print(login.is_valid())
        
        
        return HttpResponse('certin')
        
        
        
        
def sologin(request):
    return render(request, 'tela_login.html')


def validar_cadastro(request): 
    email = request.POST.get('email')    
    nome = request.POST.get('nome')
    vulgo = request.POST.get('vulgo')
    senha = request.POST.get('senha')
  
    
    try:
        usuario = Usuario(nome=nome, senha=senha, email=email, vulgo=vulgo)
        usuario.save()
        return HttpResponse('deu')
    except:
        return HttpResponse('nem deu')


def validar_login(request):
    vulgo = request.POST.get('vulgo')
    senha = request.POST.get('senha')
 
    usuario = Usuario.objects.filter(vulgo = vulgo).filter(senha = senha)
    l = "\n\n\n\n\n"
    print(len(usuario), l)

    if len(usuario) == 0:
        return HttpResponse('deu nao')
    elif len(usuario) > 0:
        return redirect("/login/alter_profile/")


def myhome(request):
    return render(request, 'home.html')



def alter_profile2(request):
    test = teste
    p = {'adra': 'pppppppooooooii'}
    y = {"P" : test}
    g = {"Y" : y}
    
    
    return render(request, 'profile.html', context={'django': 'the web framework for perfectionists with deadlines'})
        
        
        
# def save_thumbs(photo):
#     l = Usuario.objects.get(pk=11)
#     p = Usuario.objects.get(pk=5)
#     print(bool(l.photo))
#     l = ((p.photo))
#     o = (str(l))
#     print(o)
#     y = Optimize_Images(('media/' + o))
#     y.save()