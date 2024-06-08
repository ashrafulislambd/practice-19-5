from django.contrib import admin

from .models import Musician
from .models import Album

admin.site.register(Musician)
admin.site.register(Album)
