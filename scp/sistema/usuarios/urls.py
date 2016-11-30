from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'usuarios'

urlpatterns = [

	url(r'^$', views.users_view, name='users'),
	url(r'^novo/registro/$', views.novo_registro_view, name='novo-registro'),
	url(r'^novo/tarefa/$', views.novo_tarefa_view, name='novo-tarefa'),
	url(r'^novo/item/$', views.novo_item_view, name='novo-item'),
	url(r'^novo/tipo/$', views.novo_tipo_view, name='novo-tipo'),
	url(r'^novo/movimentacao/$', views.novo_movimentacao_view, name='novo-movimentacao'),
	url(r'^new/(?P<id>[0-9]+)$', views.new_view, name='new'),
	url(r'^editar/item/(?P<id>[0-9]+)$', views.editar_item_view, name='editar-item'),
	url(r'^editar/movimentacao/(?P<id>[0-9]+)$', views.editar_movimentacao_view, name='editar-movimentacao'),
	url(r'^editar/tipo/(?P<id>[0-9]+)$', views.editar_tipo_view, name='editar-tipo'),
	url(r'^editar/registro/(?P<id>[0-9]+)$', views.editar_registro_view, name='editar-registro'),
	url(r'^excluir/item/(?P<id>[0-9]+)$', views.excluir_item_view, name='excluir-item'),
	url(r'^excluir/movimentacao/(?P<id>[0-9]+)$', views.excluir_movimentacao_view, name='excluir-movimentacao'),
	url(r'^excluir/tipo/(?P<id>[0-9]+)$', views.excluir_tipo_view, name='excluir-tipo'),
	url(r'^excluir/tarefa/(?P<id>[0-9]+)$', views.excluir_tarefa_view, name='excluir-tarefa'),
	url(r'^lista/$', views.lista_view, name='lista'),
	url(r'^itens/$', views.itens_view, name='itens'),
	url(r'^inicio/$', views.inicio_view, name='inicio'),
	url(r'^(?P<registro_id>[0-9]+)/alterar/$', views.registro_alterar, name='alterar'),
    url(r'^(?P<registro_id>[0-9]+)/delete/$', views.registro_deletar, name='deletar'),
	url(r'^registro/$', views.registro_view, name='registro'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
