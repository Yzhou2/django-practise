from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    album_logo = models.CharField(max_length=1000 )

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title= models.CharField(max_length=150)
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
