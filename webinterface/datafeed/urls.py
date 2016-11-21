from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^datafeed$', views.datafeed, name='datafeed'),
]
