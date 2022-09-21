#import json
from django.http import JsonResponse, HttpResponse
from products.models import Product
from django.forms.models import model_to_dict

def api_home(request,*args,**kwargs):
    body = request.body
    data = {}
    products = Product.objects.all().order_by("?").first()
    if products:
        data = model_to_dict(products, fields=['id','title','price']) 
        # model_to_dict function allows us to convert a django model in to python dictionary and we can
        # send that model as json data by using JsonResponse fuction
        #data['title'] = products.title
        #data['contents'] = products.contents
        #data['price'] = products.price
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