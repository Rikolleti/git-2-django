from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Review
from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer
from django.http import Http404


@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            queryset = Product.objects.get(id=product_id)
            serializer_class = ProductListSerializer(queryset)
            return Response(serializer_class.data)
        except Product.DoesNotExist:
            return Response({"error": "Продукт не найден"}, status=404)
        # """реализуйте получение товара по id, если его нет, то выдайте 404
        # реализуйте сериализацию полученных данных
        # отдайте отсериализованные данные в Response"""
        # pass


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            reviews = product.comments.all()
            mark = request.GET.get('mark', None)
            if mark is not None:
                reviews = reviews.filter(mark=mark)
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"error": "Продукт не найден"}, status=404)
        # """обработайте значение параметра mark и
        # реализуйте получение отзывов по конкретному товару с определённой оценкой
        # реализуйте сериализацию полученных данных
        # отдайте отсериализованные данные в Response"""
