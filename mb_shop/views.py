import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from .models import *
from rest_framework import generics
from .serial_lisers import *
from rest_framework import viewsets


@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_tweet = Product.objects.create(**data)
        json_data = {
            'name': new_tweet.name,
            'product_sum': new_tweet.product_sum,
            'firm': new_tweet.firm,
        }
        return JsonResponse(json_data, safe=False)
    if request.method == 'GET':
        tweets = Product.objects.all()
        data = []
        for tweet in tweets:
            data.append(
                {
                    'name': tweet.name,
                    'product_sum': tweet.product_sum
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)


@csrf_exempt
def create_firma(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_tweet = Firma.objects.create(**data)
        json_data = {
            'name': new_tweet.name,
            'address': new_tweet.address
        }
        return JsonResponse(json_data, safe=False)
    if request.method == 'GET':
        tweets = Firma.objects.all()
        data = []
        for tweet in tweets:
            data.append(
                {
                    'name': tweet.name,
                    'address': tweet.address
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)


@csrf_exempt
def create_category(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_tweet = Category.objects.create(**data)
        json_data = {
            'category_name': new_tweet.category_name
        }
        return JsonResponse(json_data, safe=False)
    if request.method == 'GET':
        tweets = Category.objects.all()
        data = []
        for tweet in tweets:
            data.append(
                {
                    'category_name': tweet.category_name
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)


class ProductCreateListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class FirmaCreateListView(generics.ListCreateAPIView):
    queryset = Firma.objects.all()
    serializer_class = FirmaSerializers


class FirmaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Firma.objects.all()
    serializer_class = FirmaSerializers


class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class FirmaViewSet(viewsets.ModelViewSet):
    queryset = Firma.objects.all()
    serializer_class = FirmaSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
