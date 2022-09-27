#import json
from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(["GET"])
def api_home(request,*args,**kwargs):
    """
    DRF API VIEW
    """
    #body = request.body
    data = {}
    instance = Product.objects.all().order_by("?").first()
    if instance:
        #data = model_to_dict(instance, fields=['id','title','price','sale_price','get_discount']) 
        data = ProductSerializer(instance).data
       
    else:
        data['title'] = "no data found"

    return Response(data)
  