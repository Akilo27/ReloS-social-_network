# Generated by Django 4.2.6 on 2023-11-11 16:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0004_userprofile_friends_userprofile_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='subscriptions',
            field=models.ManyToManyField(blank=True, related_name='subscriptions', to=settings.AUTH_USER_MODEL),
        ),
    ]
