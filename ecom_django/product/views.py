from django.shortcuts import render
from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer
from .models import Category, Product
from rest_framework.decorators  import api_view
# Create your views here.

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products= Product.objects.all()[0:4]
        serializer= ProductSerializer(products,many=True)
        return Response(serializer.data)

class ProductDetails(APIView):
    def get_product(self,category_slug,product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            return Http404

    def get(self,request, category_slug, product_slug, format=None):
        product= self.get_product(category_slug, product_slug)
        serializer= ProductSerializer(product)
        return Response(serializer.data)

class CategoryDetails(APIView):
    def get_category(self,category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            return Http404

    def get(self,request, category_slug,format=None):
        category= self.get_category(category_slug)
        serializer= CategorySerializer(category)
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})