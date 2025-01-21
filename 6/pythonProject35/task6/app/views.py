from django.http import JsonResponse


def process_request(request):
    return JsonResponse({'message': 'Hello!', 'status': 'success'})
