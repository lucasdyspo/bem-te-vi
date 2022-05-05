from django.db import models

# Create your models here.

#user: caio12
#email: caio@gmail.com
#senha: teste1234

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    vulgo = models.CharField(max_length=20)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
    
