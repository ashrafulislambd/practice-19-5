from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = "music"

urlpatterns = [
    path("", views.AlbumListView.as_view(), name="index"),
    path("create_musician/", login_required(views.MusicianCreateView.as_view()), name="create_musician"),
    path("create_album/", login_required(views.AlbumCreateView.as_view()), name="create_album"),
    path("edit_musician/<int:pk>", login_required(views.MusicianUpdateView.as_view()), name="edit_musician"),
    path("edit_album/<int:pk>", login_required(views.AlbumUpdateView.as_view()), name="edit_album"),
    path("delete_musician/<int:pk>", login_required(views.MusicianDeleteView.as_view()), name="delete_musician"),
    path("delete_album/<int:pk>", login_required(views.AlbumDeleteView.as_view()), name="delete_album"),
]
