from django.contrib import admin

# Register your models here.
from .forms import RegistroForm
from .models import Registro, Item, Movimentacao, Tipo, Tarefas

class RegistroAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "cpf", "dataN"]
    #class Meta:
    #    model = SignUp

admin.site.register(Registro, RegistroAdmin)
admin.site.register(Item)
admin.site.register(Tipo)
admin.site.register(Movimentacao)
admin.site.register(Tarefas)