# Generated by Django 3.2.18 on 2023-03-20 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('genre', models.CharField(blank=True, choices=[('action', 'action'), ('comedy', 'comedy'), ('drama', 'drama'), ('horror', 'horror'), ('mistery', 'mistery'), ('romance', 'romance'), ('thriller', 'thriller')], max_length=20, null=True)),
                ('notas', models.FloatField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now=True, null=True, verbose_name='Data de Criação')),
                ('updatedAt', models.DateTimeField(auto_now=True, null=True, verbose_name='Data de Modificação')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_author', to=settings.AUTH_USER_MODEL)),
                ('collaborators', models.ManyToManyField(blank=True, related_name='users_collab', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
