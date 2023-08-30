# Generated by Django 3.2.18 on 2023-03-11 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20230311_1759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendshiprequest',
            old_name='from_User',
            new_name='from_user',
        ),
        migrations.RenameField(
            model_name='friendshiprequest',
            old_name='to_User',
            new_name='to_user',
        ),
        migrations.AlterUniqueTogether(
            name='friendshiprequest',
            unique_together={('from_user', 'to_user')},
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Friend',
                'verbose_name_plural': 'Friends',
                'unique_together': {('from_user', 'to_user')},
            },
        ),
    ]