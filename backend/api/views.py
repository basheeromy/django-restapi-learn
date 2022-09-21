import json
from django.http import JsonResponse
from products.models import Product

def api_home(request,*args,**kwargs):
    body = request.body
    data = {}
    products = Product.objects.all().order_by("?").first()
    if products:
        data['title'] = products.title
        data['contents'] = products.contents
        data['price'] = products.price
    else:
        data['title'] = "no data found"

    return JsonResponse(data)
    #    data = json.loads(body)
    #except:
    #data['headers'] = dict(request.headers) # use python dict function to convert headers (json object) to python dictionary.
    #data['content_type'] = request.content_type
    #data['params'] = dict(request.GET)
    #print(data.keys())
    #print(body)
    #print(request.GET) # request.GET will help us to access params we passed from client through url as Query dict.
    #return JsonResponse(data)