from django import forms
from .models import Community,CommunityProfile,BlogCommunity

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['name', 'description']

class CommunityProfileForm(forms.ModelForm):

    class Meta:
        model = CommunityProfile
        fields = ['image', 'status', 'about_community']


class BlogCommunityForm(forms.ModelForm):

    class Meta:
        model = BlogCommunity
        fields = ['title','image']
