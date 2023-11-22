from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Video, ProfileVideo
from .forms import VideoForm


def video_list(request):
    videos = Video.objects.order_by('-created_at')
    return render(request, 'video/video_list.html', {'videos': videos})


def video_add(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video:video_list')
    else:
        form = VideoForm()
    return render(request, 'video/video_add.html', {'form': form})


def user_video(request):
    try:
        user_info = ProfileVideo.objects.get(user=request.user)
    except:
        user_info = None
    return render(request, 'video/video_user.html', {'user_info': user_info})


def add_for_user_video(request, i):
    video = Video.objects.get(id=i)
    user_profile, created = ProfileVideo.objects.get_or_create(user=request.user)
    user_profile.video.add(video)
    user_profile.save()
    return redirect(request.META['HTTP_REFERER'])


def delete_video(request, i):
    video = Video.objects.get(id=i)
    user_profile = ProfileVideo.objects.get(user=request.user)
    user_profile.video.remove(video)
    user_profile.save()
    return redirect(request.META['HTTP_REFERER'])
