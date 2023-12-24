# Generated by Django 5.0 on 2023-12-23 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortsvc', '0005_shortenedlink_shortened_url_idx_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='shortenedlink',
            name='Shortened Url',
        ),
        migrations.AlterField(
            model_name='shortenedlink',
            name='shorturl',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
