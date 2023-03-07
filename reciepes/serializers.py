from rest_framework import serializers
from reciepes.models import Reciepe, Ingredient, Category


class ReciepeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reciepe
        fields = ['title', 'image', 'description',
                  'steps', 'category', 'ingredients']


class IngrediantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']
