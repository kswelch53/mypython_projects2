from django.shortcuts import render, HttpResponse, redirect
from ..playlist1.models import User
from .models import *
from django.contrib import messages


# renders index.html (dashboard)
def index(request):
    if 'user_id' not in request.session:
        return redirect('playlist1:index')
    else:
        print("This is index function in playlist2 views.py")

        context = {
            'playlist': Song.objects.all()
        }
        return render(request, 'playlist2/index.html', context)


# renders songs.html
def songs(request, song_id):
    print("This is songs function in playlist2 views.py")
    this_song = Song.objects.get(id=song_id)
    # song_users = User.objects.filter(added=this_song)
    this_song_added = AddtoPlaylist.objects.filter(song_link=this_song)
    context = {
        'song': this_song,
        'song_added': this_song_added,
    }
    return render(request, 'playlist2/songs.html', context)


# creates a new Song object from form data
def create_song(request):
    print("This is create_song function in playlist2 views.py")
    if request.method == 'POST':
        print("method=POST")
        this_title = request.POST['title']
        this_artist = request.POST['artist']
        print(this_title, this_artist)
# song validations
# checks for blank form field / field length
        if len(this_title) == 0 or len(this_artist) == 0:
            print("Please fill out the form field")
            messages.warning(request, "Form fields must not be left blank")
            return redirect('playlist2:create_song')
        if len(this_title) < 2 or len(this_artist) == 0:
            print("Song title/artist must have at least 2 characters")
            messages.warning(request, "Item must have at least 2 characters")
            return redirect('playlist2:create_song')
# validations passed; creates song
        # print("Ready to create song")
        this_song = Song.objects.create(title=this_title, artist=this_artist)
        return redirect('playlist2:index')

    return redirect('playlist2:index')


# adds a song to session user's playlist
# increases count of times song added
def add_to_playlist(request, song_id):
    print("This is add_to_playlist function in playlist2 views.py")
    this_song = Song.objects.get(id=song_id)
    user_id = request.session['user_id']
    this_user = User.objects.get(id=user_id)
    this_song.added_by.add(this_user)

# song counter, total adds
    this_song.times_added = this_song.times_added + 1
    this_song.save()
    print("Total times song added:", this_song.times_added)

# song count by user
# checks whether an AddtoPlaylist object exists for session user and selected song
    user_adds_song = AddtoPlaylist.objects.filter(user_link=this_user).filter(song_link=this_song)
# checks how many times user has added this song
    this_add_count = user_adds_song.count()
    print(this_user, "has added this song", this_add_count, "times")

    if this_add_count == 0: # if session user has never added this song to their playlist
        print("IF")
        # creates an AddtoPlaylist object for session user and this song
        this_add = AddtoPlaylist.objects.create(user_link=this_user, song_link=this_song, times_added=1)
        print(this_add.user_link.first_name, "created an AddtoPlaylist object for", this_add.song_link.title)

    else: # if session user has added this song to their playlist before
        print("ELSE")
        # fetches to AddtoPlaylist object for updating
        this_add = AddtoPlaylist.objects.filter(user_link=this_user).get(song_link=this_song)
        this_add.times_added = this_add.times_added + 1 # increments the count
        this_add.save()
        print(this_add.user_link.first_name, "has added", this_add.song_link.title, this_add.times_added, "times")

    return redirect('playlist2:index')


# renders users.html
def users(request, user_id):
    print("This is users function in playlist2 views.py")
    this_user = User.objects.get(id=user_id)
    # user_added_songs = Song.objects.filter(added_by=this_user)
    context = {
        'user': this_user,
        'playlist': AddtoPlaylist.objects.filter(user_link=this_user),
    }
    return render(request, 'playlist2/users.html', context)
