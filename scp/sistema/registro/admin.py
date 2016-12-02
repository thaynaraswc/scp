from django.contrib import admin

from .models import Item, Movimentacao, Tipo
# Register your models here.

# class RegistroAdmin(admin.ModelAdmin):
#     list_display = ["__unicode__", "cpf", "dataN"]

admin.site.register(Item)
admin.site.register(Tipo)
admin.site.register(Movimentacao)
