from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Posts(models.Model):
    text = models.TextField('text')
    image = models.ImageField(upload_to='images/%Y-%m-%d/',null=True, blank=True)
    time_create = models.TimeField(auto_now=True, blank=True)
    time_update = models.TimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post')
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')

    class Meta:
        verbose_name = 'posts'


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_profile')
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)


    user_follow = models.ManyToManyField(User, related_name='user_follow', blank=True, null=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'


class Like(models.Model):
    LIKE_CHOICE = (
        ('like', 'like'),
        ('unlike', 'unlike'),
    )
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_like')
    value = models.CharField(choices=LIKE_CHOICE, max_length=10, default='unlike')

    def __str__(self):
        return self.post


class Follow(models.Model):
    FOLLOW_CHOICE = (
        ('Follow', 'Follow'),
        ('Unlike', 'Unlike')
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(choices=FOLLOW_CHOICE, max_length=10, default='unlike')

    def __str__(self):
        return self.profile

