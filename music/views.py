from django.http import Http404
from django.http import HttpResponse
from .models import Album, Songs
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
    return render(request, 'music/test/details.html', {'album': album})

def favorite(request, album_id):
    album = Album.objects.get(id=album_id)
    try:
        selected_song = album.songs_set.get(id=request.POST['song'])
    except (KeyError, Songs.DoesNotExist):
        return render(request, 'music/test/details.html', {'album': album})
    else:
        selected_song.is_favorite = not selected_song.is_favorite
        selected_song.save()
        return render(request, 'music/test/details.html', {'album': album})
    