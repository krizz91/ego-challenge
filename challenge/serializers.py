from rest_framework import serializers

from challenge.models import Car, CarType

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'

class CarTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarType
        fields = '__all__'
