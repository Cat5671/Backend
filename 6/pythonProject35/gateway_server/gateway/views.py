from django.http import JsonResponse
import requests
from django.conf import settings


def pro_req(request):
    try:
        return JsonResponse(requests.get(settings.URL_FIRST_SERVER).json())
    except requests.RequestException as event:
        return JsonResponse({'error': str(event)}, status=500)
