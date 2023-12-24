# Generated by Django 5.0 on 2023-12-23 18:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortsvc', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shortenedlink',
            name='user_id',
        ),
        migrations.AddField(
            model_name='shortenedlink',
            name='created_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='created_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]