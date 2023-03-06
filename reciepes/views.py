from django.shortcuts import render
from rest_framework.generics import UpdateAPIView, DestroyAPIView, RetrieveAPIView
from reciepes.models import Reciepe
from .serializers import ReciepeSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor


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
