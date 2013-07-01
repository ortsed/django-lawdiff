from django.conf import settings

def common_variables(request):    
    return {
        'static_url': settings.STATIC_URL,
    }
