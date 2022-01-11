from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import UserEditForm,ProfileEditForm
from .models import Profile, Blogpost

# Create your views here.
def index(request):
    myposts= Blogpost.objects.all()
    print(myposts)
    return render(request,'blog/index.html', {'myposts':myposts})

def blogPost(request, id):
    post = Blogpost.objects.filter(post_id= id)[0]
    print(post)
    return render(request,'blog/blogpost.html', {'post':post})

@login_required
def editProfile(request):
    if not Profile.objects.filter(user=request.user).exists():
        Profile.objects.create(user=request.user)
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse("blog:edit_profile"))
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'blog/edit_profile.html', context)
