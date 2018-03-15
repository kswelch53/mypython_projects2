from django.db import models
from ..playlist1.models import *

class Song(models.Model):
    title=models.CharField(max_length=100)
    artist=models.CharField(max_length=100)
    # many songs, many users
    added_by=models.ManyToManyField(User, related_name="added")
    # total number of times a song has been added
    times_added = models.IntegerField(default=0, null=True, blank=True)


class AddtoPlaylist(models.Model):
    # many counts per user
    user_link = models.ForeignKey(User, related_name="links_user", null=True, blank=True)
    # many counts per song
    song_link = models.ForeignKey(Song, related_name="links_song", null=True, blank=True)
    # number of times each user adds a song
    times_added = models.IntegerField(default=0, null=True, blank=True)
