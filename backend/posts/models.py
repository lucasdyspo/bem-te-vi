from django.db import models
from users.models import User
from distutils.command.upload import upload
from pickle import TRUE
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from common.Scripts.trat_imgs import Optimize_Images
import uuid


from common.models import IndexedTimeStampedModel

from django import forms



class Post(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_author')
    collaborators = models.ManyToManyField(User, blank=True, related_name='users_collab')
    title = models.CharField(max_length=80)
    description = models.TextField()

    genre = models.CharField(max_length=20, null=True, blank=True, choices = [
    ('action', 'action'), ('comedy', 'comedy'), ('drama', 'drama'), ('horror', 'horror'),
    ('mistery', 'mistery'), ('romance', 'romance'), ('thriller', 'thriller')
    ])
    thumb_path = models.CharField(max_length=80, blank=True, null=True)
    img = models.ImageField(upload_to='Profile', blank=True, null=True)

    notas = models.FloatField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name=_('Data de Criação'))
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name=_('Data de Modificação'))
    rate = models.FloatField


    class Meta:
        ordering = ['-createdAt', 'author']
        verbose_name_plural = "postagens"



class favorites(models.Model):
    # user = models.OneToOneField(User, related_name='favorites', on_delete=models.DO_NOTHING, primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favorites')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = [['Post', 'User']]


class rating(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='rating')
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
    rating = models.IntegerField(blank= True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rating, 'user :', User)

    class Meta:
        unique_together = [['Post', 'User']]


class Likes(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        unique_together = [['Post', 'User']]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + '  ' + str(self.content)[:20]



class HighlightsAdmin(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    thumb_path = models.CharField(max_length=80, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='highlights', blank=True, null=True)

    def __str__(self):
        return self.title


    def manage_img(self):
    # self.img
        new_img = Optimize_Images(self.img, self.title)
        self.img = img.photo_url

