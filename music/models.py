from django.db import models
from django.core.urlresolvers import reverse


# here are going to create tables for artists, albums, songs, etc
# example: the album Hysteria will have the PrimaryKey of 1

class Album(models.Model):
    artist = models.CharField(max_length=250, null=False, blank=False)
    album_title = models.CharField(max_length=400)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    # this is were we specify what gets printed out
    def __str__(self):
        return self.album_title + ' - ' + self.artist


# (Album, on_delete=models.CASCADE) means that if the Album is deleted, all songs related to it will be deleted too

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
