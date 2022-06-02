from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView

from .form import UserRegistrationForm, UserPostForm
from .models import *


def baseview(request):
    return render(request, 'base.html')





def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            Profile.objects.create(user=new_user)

            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request, 'registration/registraion.html', {'user_form': user_form})


def mypage(request, myname):
    user = Profile.objects.get(user__username = myname)
    post = Posts.objects.filter(user__username=myname)







    print(myname)
    return render(request, 'account/MyPage.html', {'post': post, 'userprofile': user, })


class PostsListView(ListView):
    model = Posts
    template_name = 'account/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Posts.objects.all().order_by('-time_create')

def like_post(request, pk):
    user = request.user
    print(pk, 'asdsads')
    if request.method == 'POST':
        post_id = int(request.POST.get('post_id'))
        post_id = int(post_id)
        post_obj = Posts.objects.get(id=pk)
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, post_id=pk)
        if not created:
            if Like.value == 'like':
                Like.value = 'unlike'
            else:
                Like.value = 'like'
        like.save()

    return HttpResponseRedirect(reverse('posts_list'))


def follow_user(request, pk):
    user = request.user


class UserListView(ListView):
    model = User
    template_name = 'account/UserList.html'
    context_object_name = 'User'


def message(request):
    asd = 'dsad'
    return render(request, 'account/message.html', {'asd': asd})


def reg(request):
    return render(request, 'registration/register_done.html')

@login_required
def addpost(request):
    if request.method == 'POST':
        form = UserPostForm(request.POST, request.FILES or None)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts_list')
    else:
        form = UserPostForm

    return render(request, 'account/add_post.html', {'form': form})


def Follow(request, username):
    userprofile = Profile.objects.get(user__username=username)
    user = request.user
    if user in userprofile.user_follow.all():
        userprofile.user_follow.remove(user)
    else:
        userprofile.user_follow.add(user)
    return HttpResponseRedirect(reverse(mypage,args=[str(username)]))