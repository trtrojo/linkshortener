from django.db import models
from rest_framework import serializers
from shortsvc.models import ShortenedLink

# Create your models here.

class ShortenedLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedLink
        fields = '__all__'