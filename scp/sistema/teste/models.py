from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.
# MVC MODEL VIEW CONTROLLER

# class Grupo(models.Model):
#     nome = models.CharField(max_length=120, default="Defaul")
#     cadastrar = models.BooleanField(default=False)

#     def __str__(self):
#         return self.nome


class Registro(models.Model):
    nome = models.CharField(max_length=120, blank=True)
    cpf = models.CharField(max_length=15, blank=True)
    dataN = models.DateField()
    cidade = models.CharField(max_length=120, blank=True)
    estado = models.CharField(max_length=120, blank=True)
    bairro = models.CharField(max_length=120, blank=True)
    adress = models.CharField(max_length=120, blank=True)
    cep = models.CharField(max_length=12, blank=True)
    complemento = models.CharField(max_length=120, blank=True)
    lotado =  models.CharField(max_length=120, blank=True)
    setor = models.CharField(max_length=120, blank=True)
    cargo = models.CharField(max_length=120, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    whatsapp = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    # codigo = models.IntegerField()
    # publish = models.DateField(auto_now=False, auto_now_add=False)
    # updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    # timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    nome = models.CharField(max_length=120, blank=False)
    codigo = models.CharField(max_length=120, blank=True)
    descricao = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.nome


class Item(models.Model):
    # chave do tipo
    tipo = models.CharField(max_length=120, blank=True)
    patrimonio = models.CharField(max_length=120, blank=False)
    origem = models.CharField(max_length=120, blank=True)
    descricao = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.tipo


class Movimentacao(models.Model):
    tipo = models.CharField(max_length=120, blank=True)
    modelo = models.CharField(max_length=120, blank=False)
    marca = models.CharField(max_length=120, blank=True)
    tombo = models.CharField(max_length=300, blank=True)
    situacao = models.CharField(max_length=120, blank=True)
    servidor = models.CharField(max_length=120, blank=True)
    proprietario = models.CharField(max_length=120, blank=True)
    local = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.tipo