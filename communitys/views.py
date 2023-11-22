from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommunityForm
from .models import Community

def community_list(request):
    communities = Community.objects.all()
    return render(request, 'community/community_list.html', {'communities': communities})


def create_community(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            community = form.save(commit=False)
            community.save()
            community.members.add(request.user)
            return redirect('community:community_list')
    else:
        form = CommunityForm()
    return render(request, 'community/create_community.html', {'form': form})

def edit_community(request, community_id):
    community = get_object_or_404(Community, id=community_id)
    if request.method == 'POST':
        form = CommunityForm(request.POST, instance=community)
        if form.is_valid():
            form.save()
            return redirect('community:community_list')
    else:
        form = CommunityForm(instance=community)
    return render(request, 'community/edit_community.html', {'form': form})
