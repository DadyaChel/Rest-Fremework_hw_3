from rest_framework import serializers

from .models import *


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


# class FirmaSerializers(serializers.ModelSerializer):
#     name = serializers.CharField(max_length=99)
#     address = serializers.CharField(max_length=222)
#
#     class Meta:
#         model = Firma
#         fields = "__all__"
#
#     def create(self, validated_data):
#         massage = Firma.objects.create(
#             name=validated_data['name'],
#             address=validated_data['address']
#         )
#         return massage
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data['name']
#         instance.address = validated_data['address']
#         return instance


class FirmaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Firma
        fields = "__all__"


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

