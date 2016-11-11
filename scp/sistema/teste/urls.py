from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'teste'

urlpatterns = [
	url(r'^$', views.users_view, name='users'),
	url(r'^novo/$', views.novo_view, name='novo'),
	url(r'^lista/$', views.lista_view, name='lista'),
	url(r'^itens/$', views.itens_view, name='itens'),
	url(r'^(?P<registro_id>[0-9]+)/alterar/$', views.registro_alterar, name='alterar'),
    url(r'^(?P<registro_id>[0-9]+)/delete/$', views.registro_deletar, name='deletar'),
	url(r'^registro/$', views.registro_view, name='registro'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
