from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Usuario

# Create your views here.
def login(request):
    return render(request, 'login_page.html')


def validar_cadastro(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')    
    vulgo = request.POST.get('vulgo')
    usuario = Usuario(nome=nome, senha=senha, email=email, vulgo=vulgo)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/login/cadastro/?status=1')

    if len(senha) < 1:
        return redirect('/login/cadastro/?status=2')


    
    
    #usuario = Usuario.objects.filter()
    
    
    usuario.save()
    return HttpResponse('oila')