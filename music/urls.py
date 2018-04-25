from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [

	# /music
	url(r'^(?P<key>[0-9]+)/(?P<p_id>[0-9]+)$', views.index, name='index'),

	# /music/13
	url(r'^(?P<album_id>[0-9]+)/$', views.details, name='details'),

	# /music/<album_id>/favorite/
	url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

    url(r'^back_details/(?P<p_id>[0-9]+)$', views.back_details, name='back_details'),
]