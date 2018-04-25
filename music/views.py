from django.http import Http404
from django.http import HttpResponse
from .models import Album, Songs
from login.models import Person
from django.shortcuts import render
import numpy as np
from django.shortcuts import redirect

key_session = 0

def index(request, key, p_id):
    all_albums = Album.objects.all()
    global key_session

    try:
        person = Person.objects.get(id=p_id)
    except Person.DoesNotExist:
        print("sdgs")

    back_url = '/back_details/' + p_id

    if person.key == key:

        context = {
            'all_albums': all_albums,
            'back_url': back_url
        }

        person.key = np.random.randint(50000)
        key_session = person.key
        person.save()

        return render(request, 'music/test/index.html', context)

    else:
        return redirect('/login/')


def back_details(request, p_id):
    global key_session

    url = '/music/' + str(key_session) + '/' + str(p_id)

    return redirect(url)




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
    