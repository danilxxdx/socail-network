from django.contrib import admin

from .models import *


@admin.register(Posts)
class AdmoinPosts(admin.ModelAdmin):
    list_display = ('text',)


@admin.register(Profile)
class AdmoinProfile(admin.ModelAdmin):
    list_display = ('photo', 'user', 'date_of_birth')
    list_display_links = ('photo', 'user', 'date_of_birth')


@admin.register(Like)
class AdmoinLike(admin.ModelAdmin):
    list_display = ('user', 'post', 'value')
    list_display_links = ('user', 'post', 'value')

@admin.register(Follow)
class AdmoinFollow(admin.ModelAdmin):
    list_display = ('user', 'profile', 'value')
    list_display_links = ('user', 'profile', 'value')
