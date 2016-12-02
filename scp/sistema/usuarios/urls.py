from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'usuarios'

urlpatterns = [

	url(r'^$', views.users_view, name='users'),
	url(r'^novo/cadastro/$', views.novo_cadastro_view, name='novo-cadastro'),

	url(r'^editar/cadastro/(?P<id>[0-9]+)$', views.editar_cadastro_view, name='editar-cadastro'),

	url(r'^excluir/tarefa/(?P<id>[0-9]+)$', views.excluir_tarefa_view, name='excluir-tarefa'),

	url(r'^lista/$', views.lista_view, name='lista'),
	url(r'^inicio/$', views.inicio_view, name='inicio'),
	url(r'^(?P<cadastro_id>[0-9]+)/alterar/$', views.cadastro_alterar, name='alterar'),
    url(r'^(?P<cadastro_id>[0-9]+)/delete/$', views.cadastro_deletar, name='deletar'),
	url(r'^cadastro/$', views.cadastro_view, name='cadastro'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),

	url(r'^erro/$', views.erro_view, name='erro'),

]
