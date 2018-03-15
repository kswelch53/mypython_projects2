from django.conf.urls import url, include
from . import views

# This is app_two
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^songs/(?P<song_id>\d+)$', views.songs, name='songs'),
    url(r'^create_song$', views.create_song, name='create_song'),
    url(r'^add_to_playlist/(?P<song_id>\d+)$', views.add_to_playlist, name='add_to_playlist'),
    url(r'^users/(?P<user_id>\d+)$', views.users, name='users'),

]
