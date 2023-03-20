from django.db import models
from users.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_author')
    collaborators = models.ManyToManyField(User, blank=True, related_name='users_collab')
    title = models.CharField(max_length=80)
    description = models.TextField()

    genre = models.CharField(max_length=20, null=True, blank=True, choices = [
    ('action', 'action'), ('comedy', 'comedy'), ('drama', 'drama'), ('horror', 'horror'),
    ('mistery', 'mistery'), ('romance', 'romance'), ('thriller', 'thriller')
    ])

    notas = models.FloatField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name=_('Data de Criação'))
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name=_('Data de Modificação'))
