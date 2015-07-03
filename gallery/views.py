from django.shortcuts import render
from .models import Album

# Create your views here.

def gallery(request):
    albums = Album.objects.all()
    selected_album = Album.objects.first()
    if request.GET.get('album_id'):
        selected_album = Album.objects.get(pk=request.GET['album_id'])
    return render(request, "gallery.html", {"albums": albums, "selected_album": selected_album})
