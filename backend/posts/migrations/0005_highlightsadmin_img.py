# Generated by Django 3.2.18 on 2023-03-21 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_highlightsadmin_thumb_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='highlightsadmin',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='highlights'),
        ),
    ]
