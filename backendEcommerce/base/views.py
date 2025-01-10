from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .products_list import products_list

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = ['/api/products',"/api/products/create","/api/products/upload"]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    print(type(products_list[0]))
    return Response(products_list)

@api_view(['GET'])
def getProductByID(request,pk):
    product = None
    # Loop over list : each element is dict
    for i in products_list:
        if i['_id'] == pk:
            product = i
            break
    return Response(product)
