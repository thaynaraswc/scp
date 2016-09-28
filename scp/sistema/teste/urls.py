from django.conf.urls import url
from django.contrib import admin

from .views import (
	users_view,
	)

urlpatterns = [
	url(r'^$', users_view, name='users'),
]
