from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from urllib import parse
from django.db import IntegrityError
from linkshortner import settings
from shortsvc.models import ShortenedLink
from shortsvc import utils

# Create your views here.

class ShortWeb(View):
    def get(self, request):
        shorturl = request.GET.get('shorturl', '')
        fullurl = utils.get_full_url(shorturl) if len(shorturl) != 0 else None

        context = {
            'error': request.GET.get('error'),
            'destination_url': request.GET.get('destination_url', ''),
            'shorturl': shorturl,
            'fullurl': fullurl,
            'exampleurl': utils.get_full_url('myurl')
        }

        return render(request, 'index.html', context=context)
    
class ShortWebCreate(View):
    def get(self, request):
        # Redirect back to the main page if we are using GET (only post is allowed.)
        return redirect('/', permanent=False)
    
    def post(self, request):

        if request.user.is_authenticated or utils.ANONYMOUS_CREATION_ALLOWED:
            default_shorturl = utils.get_random_short_code()
            shorturl = request.POST.get('shorturl', '')
            custom_shorturl_used = True
            destination_url = request.POST.get('destination_url', '')

            if len(shorturl) == 0:
                custom_shorturl_used = False
                shorturl = default_shorturl
            
            if len(destination_url) == 0:
                err_msg = 'You must enter a URL to shorten.'
                return redirect(f'/?error={parse.quote(err_msg)}', permanent=False)

            try:
                shortened_link = ShortenedLink(shorturl=shorturl, destination_url=destination_url, created_by=request.user)
                shortened_link.save()
            except IntegrityError:
                if custom_shorturl_used:
                    err_msg = f'The shortened url {shorturl} is already in use.'
                    return redirect('/?error={}&destination_url={}&shorturl={}'.format(
                        parse.quote(err_msg),
                        parse.quote(destination_url),
                        shorturl
                    ))
                
                else:
                    link_pending = True
                    while link_pending and not custom_shorturl_used:
                        try:
                            shorturl = utils.get_random_short_code()
                            shortened_link = ShortenedLink(shorturl=shorturl, destination_url=destination_url, 
                                                        created_by=request.user)
                            shortened_link.save()
                            link_pending = False
                        except IntegrityError:
                            pass
            
            # return HttpResponse(f'Shortened URL: {shortened_link.shorturl} for {shortened_link.destination_url}')
            return redirect('/?destination_url={}&shorturl={}'.format(
                parse.quote(destination_url),
                shorturl
            ))
        else:
            return redirect('/?error={}'.format(
                            parse.quote('You must be logged in in order to create new links.')
                        ))
