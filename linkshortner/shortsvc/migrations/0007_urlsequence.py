# Generated by Django 5.0 on 2023-12-23 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortsvc', '0006_remove_shortenedlink_shortened_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlSequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_value', models.IntegerField(default=0)),
            ],
        ),
    ]