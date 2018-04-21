from django.contrib import admin
from .models import Album, Songs, Person


admin.site.register(Album)
admin.site.register(Songs)
admin.site.register(Person)