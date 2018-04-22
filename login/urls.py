from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [

	url(r'^$', views.index, name='index'),

    url(r'^validate$', views.validate, name='validate'),
]