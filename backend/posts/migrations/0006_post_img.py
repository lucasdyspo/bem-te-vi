# Generated by Django 3.2.18 on 2023-03-22 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_highlightsadmin_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='Profile'),
        ),
    ]
