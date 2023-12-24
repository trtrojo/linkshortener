from django.db import models
from django.conf import settings

# Create your models here.

class ShortenedLink(models.Model):
    class Meta:
        db_table = 'shortenedlinks'

        indexes = [
            models.Index(fields=['shorturl'], name='shortened_url_idx')
        ]

    shorturl = models.CharField(max_length=16, unique=True, null=False, blank=False)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='created_by',
        null=True
    )

    destination_url = models.TextField(null=False, blank=False)

    def __str__(self):
        return f'{self.created_by} - {self.shorturl} - {self.destination_url}'
    

class UrlSequence(models.Model):
    current_value = models.IntegerField(default=0)

    def get_next_value(self):
        # Increment the current value
        self.current_value = models.F('current_value') + 1
        self.save(update_fields=['current_value'])

        # Refresh from DB to get the updated value
        self.refresh_from_db()
        return self.current_value