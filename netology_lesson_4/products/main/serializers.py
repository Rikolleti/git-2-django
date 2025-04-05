from rest_framework import serializers
from .models import Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    # реализуйте все поля
    class Meta():
        model = Review
        fields = "__all__"


class ProductListSerializer(serializers.Serializer):
    # реализуйте поля title и price
    title = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Review
        fields = ["title", "description", "price", "reviews"]
    # реализуйте поля title, description, price и reviews (список отзывов к товару)
