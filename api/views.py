from django.http import JsonResponse
from datetime import datetime

def time_api(request):
    return JsonResponse({
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })