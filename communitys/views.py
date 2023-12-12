from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommunityForm,CommunityProfileForm,BlogCommunityForm
from .models import Community,CommunityProfile,BlogCommunity


def community_list(request):
    communities = Community.objects.all()
    return render(request, 'community/community_list.html', {'communities': communities})


def community_detail(request, name):
    community = Community.objects.get(name=name)
    blog_community = BlogCommunity.objects.filter(community=community)
    profile_community = CommunityProfile.objects.get(community=community)

    return render(request, 'community/community.html', {'community': community,
                                                        'blog_community': blog_community,
                                                        'profile_community': profile_community})


def create_community(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            community = form.save(commit=False)
            community.creator = request.user
            community.save()
            community.members.add(request.user)

            CommunityProfile.objects.create(community=community)
            return redirect('community:community_list')
    else:
        form = CommunityForm()
    return render(request, 'community/create_community.html', {'form': form})


def edit_community(request, community_id):
    community_profile = get_object_or_404(CommunityProfile, community_id=community_id)
    if request.method == 'POST':
        form = CommunityProfileForm(request.POST, request.FILES, instance=community_profile)
        if form.is_valid():
            form.save()
            return redirect('community:community_list')
    else:
        form = CommunityProfileForm(instance=community_profile)
    return render(request, 'community/edit_community.html', {'form': form})


def create_post_community(request, community_id):
    community = get_object_or_404(Community, id=community_id)

    if request.method == 'POST':
        form = BlogCommunityForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.community = community
            blog.save()
            return redirect('community:detail', name = community.name)
    else:
        form = BlogCommunityForm()

    return render(request, 'community/create_post_community.html', {'form': form, 'community': community})

def handle_like_view(request, username):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        action = request.POST['action']

        community = Community.objects.get(name=username)
        BlogCommunity.handle_like(request, post_id, action, community, username)

    return redirect(request.META['HTTP_REFERER'])


