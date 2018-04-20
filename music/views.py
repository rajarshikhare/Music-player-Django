from django.http import Http404
from django.http import HttpResponse
from .models import Album
from django.shortcuts import render

def index(request):
	all_albums = Album.objects.all()

	context = {
		'all_albums': all_albums,
	}

	return render(request, 'music/test/index.html', context)


def details(request, album_id):
	try:
		album = Album.objects.get(id=album_id)
	except Album.DoesNotExist:
		raise Http404("Album not found")
	return render(request, 'music/details.html', {'album': album})
	