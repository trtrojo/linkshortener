from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework.response import Response
from . import models

from shortsvc.models import ShortenedLink

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')  
class SingleURL(View):
    def get(self, request, shortened_id):
        row = ShortenedLink.objects.filter(shorturl=shortened_id).first()
        s = models.ShortenedLinkSerializer(row, many=False)
        return JsonResponse(s.data)
    
    def post(self, request):

        return HttpResponse('OK!')