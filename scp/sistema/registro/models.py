from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tipo(models.Model):
    # item = models.ForeignKey(Item, on_delete=models.CASCADE)
    nome = models.CharField(max_length=120, blank=False)
    codigo = models.CharField(max_length=120, blank=True)
    descricao = models.TextField(max_length=300, blank=True)
    marca = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.nome

class Item(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, null=True)
    patrimonio = models.CharField(max_length=120, blank=False)
    origem = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.patrimonio


class Movimentacao(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    # tipo = models.CharField(max_length=120, blank=True)
    modelo = models.CharField(max_length=120, blank=False)
    marca = models.CharField(max_length=120, blank=True)
    tombo = models.CharField(max_length=300, blank=True)
    situacao = models.CharField(max_length=120, blank=True)
    servidor = models.CharField(max_length=120, blank=True)
    proprietario = models.CharField(max_length=120, blank=True)
    local = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.tipo
