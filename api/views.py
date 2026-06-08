from django.http import JsonResponse
from datetime import datetime

def hello_api(request):
    return JsonResponse({
        "message": "Hello API"
    })
def time_api(request):
    return JsonResponse({
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
