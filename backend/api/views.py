from django.http import JsonResponse

def api_home(request,*args,**kwargs):
    return JsonResponse({"message":"Hello there, This is django rest API response."})