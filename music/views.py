from django.shortcuts import render, redirect
from .forms import SongForm
from .models import Song, ProfileSong


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'music/song_list.html', {'songs': songs})


def song_upload(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('music:song_list')
    else:
        form = SongForm()
    return render(request, 'music/song_upload.html', {'form': form})


def music_user(request):
    try:
        user_info = ProfileSong.objects.get(user=request.user)
    except:
        user_info = None
    return render(request, 'music/song_user.html', {'user_info': user_info})


def add_for_user_song(request, i):
    video = Song.objects.get(id=i)
    user_profile, created = ProfileSong.objects.get_or_create(user=request.user)
    user_profile.song.add(video)
    user_profile.save()
    return redirect(request.META['HTTP_REFERER'])


def delete_song(request, i):
    video = Song.objects.get(id=i)
    user_profile = ProfileSong.objects.get(user=request.user)
    user_profile.song.remove(video)
    user_profile.save()
    return redirect(request.META['HTTP_REFERER'])
