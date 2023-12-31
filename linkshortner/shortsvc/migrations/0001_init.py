# Generated by Django 5.0 on 2023-12-24 05:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortenedLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_url', models.TextField()),
                ('created_by', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('shorturl', models.CharField(default='', max_length=16)),
            ],
            options={
                'indexes': [models.Index(fields=['shorturl'], name='shortened_url_idx')],
            },
        ),
        migrations.AddConstraint(
            model_name='shortenedlink',
            constraint=models.UniqueConstraint(fields=('shorturl',), name='Shortened Url'),
        ),
        migrations.AlterModelTable(
            name='shortenedlink',
            table='shortenedlinks',
        ),
        migrations.RemoveConstraint(
            model_name='shortenedlink',
            name='Shortened Url',
        ),
        migrations.AlterField(
            model_name='shortenedlink',
            name='shorturl',
            field=models.CharField(max_length=16, unique=True),
        ),
        migrations.CreateModel(
            name='UrlSequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_value', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='shortenedlink',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
