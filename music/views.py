from django.shortcuts import render
from django.urls import reverse

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages

from .models import Album, Musician
from .forms import MusicianForm, AlbumForm

class AlbumListView(ListView):
    model = Album
    template_name = "music/index.html"

class MusicianCreateView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = "music/create_musician.html"

    def get_success_url(self):
        messages.success(self.request, message="Successfully Created Musician")
        return reverse("music:index")
    
class MusicianUpdateView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = "music/create_musician.html"

    def get_success_url(self):
        messages.success(self.request, message="Successfully Modified Musician")
        return reverse("music:index")
    
class MusicianDeleteView(DeleteView):
    model = Musician
    template_name = "music/delete.html"

    def get_success_url(self):
        messages.success(self.request, message="Successfully Deleted Musician")
        return reverse("music:index")
    
class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = "music/create_musician.html"

    def get_success_url(self):
        messages.success(self.request, message="Successfully Created Album")
        return reverse("music:index")

class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = "music/create_musician.html"

    def get_success_url(self):
        messages.success(self.request, message="Successfully Modified Album")
        return reverse("music:index")
    
class AlbumDeleteView(DeleteView):
    model = Album
    template_name = "music/delete.html"

    def get_success_url(self):
        messages.success(self.request, message="Successfully Deleted Album")
        return reverse("music:index")


