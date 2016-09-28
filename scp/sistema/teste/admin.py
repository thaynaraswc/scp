from django.contrib import admin

# Register your models here.
from .forms import RegistroForm
from .models import Registro

class RegistroAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "cpf", "dataN"]
    form = RegistroForm
    #class Meta:
    #    model = SignUp

admin.site.register(Registro, RegistroAdmin)
