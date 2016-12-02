from django.contrib import admin

# Register your models here.
from .forms import CadastroForm
from .models import Cadastro, Tarefas

class CadastroAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "cpf", "dataN"]
    #class Meta:
    #    model = SignUp

admin.site.register(Cadastro, CadastroAdmin)
admin.site.register(Tarefas)
