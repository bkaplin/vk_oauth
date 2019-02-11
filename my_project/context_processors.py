from django.conf import settings
#from django_geoip.base import location_model

def get_settings(request):
    protocol = request.META.get('wsgi.url_scheme')
    print settings.STATIC_URL
    return {
        'STATIC_URL': settings.STATIC_URL,
        'SERVER_PROTOCOL': protocol
    }
