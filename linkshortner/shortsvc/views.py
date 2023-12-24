from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from .models import ShortenedLink, UrlSequence
    
class ShortnerView(View):
    def get(self, request, shortened_id):
        
        #ShortenedLink.objects.filter(shorturl=shortened_id).first()
        row = get_object_or_404(ShortenedLink, shorturl=shortened_id)
        
        # wait_seconds = 5
        # html_content = f"""
        # <!DOCTYPE html>
        # <html>
        # <head>
        #     <meta http-equiv="refresh" content="{wait_seconds};url={row.destination_url}">
        #     <title>Redirecting...</title>
        # </head>
        # <body>
        #     <p>{UrlSequence.objects.first().get_next_value()}</p>
        #     <p>If you are not redirected, <a href="{row.destination_url}">click here</a>.</p>
        #     <!-- Add more fallback content here if necessary -->
        # </body>
        # </html>
        # """

        # return HttpResponse(html_content)
        return redirect(row.destination_url, permanent=False)

def shortner_404_view(request, exception):
    # You can render a custom template here
    # return render(request, '404.html', {})
    
    # Or return a custom HttpResponse
    return HttpResponseNotFound('<h1>Page not found</h1>')