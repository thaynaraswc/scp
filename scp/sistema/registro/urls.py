from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'registro'

urlpatterns = [

	url(r'^novo/item/$', views.novo_item_view, name='novo-item'),
	url(r'^novo/tipo/$', views.novo_tipo_view, name='novo-tipo'),
	url(r'^novo/movimentacao/$', views.novo_movimentacao_view, name='novo-movimentacao'),

	url(r'^editar/item/(?P<id>[0-9]+)$', views.editar_item_view, name='editar-item'),
	url(r'^editar/movimentacao/(?P<id>[0-9]+)$', views.editar_movimentacao_view, name='editar-movimentacao'),
	url(r'^editar/tipo/(?P<id>[0-9]+)$', views.editar_tipo_view, name='editar-tipo'),

	url(r'^excluir/item/(?P<id>[0-9]+)$', views.excluir_item_view, name='excluir-item'),
	url(r'^excluir/movimentacao/(?P<id>[0-9]+)$', views.excluir_movimentacao_view, name='excluir-movimentacao'),
	url(r'^excluir/tipo/(?P<id>[0-9]+)$', views.excluir_tipo_view, name='excluir-tipo'),

	url(r'^lista/$', views.lista_itens_view, name='lista-itens'),

	url(r'^itens/$', views.itens_view, name='itens'),
]
