from rest_framework import serializers
from reciepes.models import Reciepe


class ReciepeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reciepe
        fields = ['title', 'image', 'description',
                  'steps', 'category', 'ingredients']
