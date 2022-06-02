from django.contrib.auth.views import *
from django.urls import path

from .views import *

urlpatterns = [
    path('', baseview , name = 'base' ),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', register, name='register'),
    path('mypage/<str:myname>/', mypage, name = 'mypage'),
    path('list/', UserListView.as_view(), name = 'userlist'),
    path('listpost/', PostsListView.as_view(), name = 'posts_list'),
    path('like/<int:pk>/', like_post, name ='like_post'),
    path('message', message, name ='message'),
    path('regg/', reg, name = 'reg'),
    path('addpost/', addpost, name = 'addpost'),
    path('follow/<str:username>', Follow, name = 'follow')


]
