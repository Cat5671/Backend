from django.http import JsonResponse
import requests


def pro_req(request):
    try:
        return JsonResponse(requests.get("http://127.0.0.1:8000/").json())
    except requests.RequestException as event:
        return JsonResponse({'error': str(event)}, status=500)
