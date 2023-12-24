import random, string
import urllib
from linkshortner import settings

def get_random_short_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=settings.DEFAULT_SHORT_CODE_LENGTH))

def get_full_url(shorturl=None, request=None):
    shorturl = '' if shorturl is None else shorturl

    if 'BASE_SHORTENER_URL' in dir(settings):
        return f'{settings.BASE_SHORTENER_URL}/{shorturl}'

    else:
        return f'http://localhost:8000/s/{shorturl}'
    

if 'ANONYMOUS_CREATION_ALLOWED' in dir(settings):
    ANONYMOUS_CREATION_ALLOWED = settings.ANONYMOUS_CREATION_ALLOWED

else:
    ANONYMOUS_CREATION_ALLOWED = False