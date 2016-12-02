from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'relatorio'

urlpatterns = [

	url(r'^$', views.relatorio_view, name='relatorio'),

]
