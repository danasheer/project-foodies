from django.shortcuts import render
from rest_framework.generics import UpdateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView, CreateAPIView
from reciepes.models import Reciepe, Ingredient, Category
from .serializers import ReciepeSerializer, IngrediantSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor


class CreateReciepeView(CreateAPIView):
    queryset = Reciepe.objects.all()
    serializer_class = ReciepeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class listReciepeView(ListAPIView):
    queryset = Reciepe.objects.all()
    serializer_class = ReciepeSerializer


class RecipieDetailView(RetrieveAPIView):
    queryset = Reciepe.objects.all()
    serializer_class = ReciepeSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class RecipieUpdateView(UpdateAPIView):
    queryset = Reciepe.objects.all()
    serializer_class = ReciepeSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [IsAuthenticated, IsAuthor]


class RecipeDeleteView(DestroyAPIView):
    queryset = Reciepe.objects.all()
    serializer_class = ReciepeSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [IsAuthenticated, IsAuthor]


class CreateIngrediantView(CreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngrediantSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class listingrediantView(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngrediantSerializer


class UpdateIngrediantView(UpdateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngrediantSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeleteIngrediantView(DestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngrediantSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [IsAuthenticated, IsAuthor]


class CreateCategoryView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class listCategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UpdateCategoryView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [IsAuthenticated, IsAuthor]


class DeleteCategoryView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [IsAuthenticated, IsAuthor]
