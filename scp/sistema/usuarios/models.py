from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# MVC MODEL VIEW CONTROLLER

# class Grupo(models.Model):
#     nome = models.CharField(max_length=120, default="Defaul")
#     cadastrar = models.BooleanField(default=False)

#     def __str__(self):
#         return self.nome


class Cadastro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=120, blank=True)
    cpf = models.CharField(max_length=15, blank=True)
    dataN = models.DateField()
    cidade = models.CharField(max_length=120, blank=True)
    estado = models.CharField(max_length=120, blank=True)
    bairro = models.CharField(max_length=120, blank=True)
    endereco = models.CharField(max_length=120, blank=True)
    cep = models.CharField(max_length=12, blank=True)
    complemento = models.CharField(max_length=120, blank=True)
    lotado =  models.CharField(max_length=120, blank=True)
    setor = models.CharField(max_length=120, blank=True)
    cargo = models.CharField(max_length=120, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    whatsapp = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    nfuncional = models.CharField(max_length=15, blank=True)
    # grupo = models.CharField(max_length=26, blank=True)
    # codigo = models.IntegerField()
    # publish = models.DateField(auto_now=False, auto_now_add=False)
    # updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    # timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome


class Tarefas(models.Model):
    tarefa = models.CharField(max_length=120, blank=False)

    def __str__(self):
        return self.tarefa
