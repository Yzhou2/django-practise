# from django.shortcuts import render, get_object_or_404
# from django.views import generic
# from django.http import Http404
# from .models import Album, Song
# from django.views.generic.edit import CreateView
# # import logging
# #
# # logr = logging.getLogger(__name__)
#
# # Create your views here.
#
# def index(request):
#     all_albums = Album.objects.all()
#     context = {'all_albums': all_albums}
#     return render(request, 'homepage/home.html', context)
#
# def detail(request, id):
#     # try:
#     #     album = Album.objects.get(id=id)
#     # except Album.DoesNotExist:
#     #     raise Http404("Album does not exist")
#
#     album = get_object_or_404(Album, pk=id)
#     return render(request, 'homepage/detail.html', {'album': album})
#
# def fav(request, id):
#     album = get_object_or_404(Album, pk=id)
#     try:
#         selected_song = album.song_set.get(id=request.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         return render(request, 'homepage/detail.html', {'album': album, 'error_message': 'select a song',
#     })
#     else:
#         selected_song.is_fav = True
#         selected_song.save()
#         return render(request, 'homepage/detail.html', {'album': album})

from django.views import generic
from .models import Album, Song
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class HomeView(generic.ListView):
    template_name = "homepage/home.html"
    context_object_name = "all_albums"

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'homepage/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'title', 'album_logo']

class AlbumUpdate(UpdateView):
        model = Album
        fields = ['artist', 'title', 'album_logo']

class AlbumDelete(DeleteView):
                model = Album
                success_url = reverse_lazy('homepage')
                # template_name = 'homepage/home.html'
