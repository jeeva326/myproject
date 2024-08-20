from .models import Destin
from rest_framework import serializers

class DestinSerializers(serializers.ModelSerializer):
    PlaceImage=serializers.ImageField(required=False)

    class Meta:
        model=Destin
        fields="__all__"