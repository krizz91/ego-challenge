from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from challenge import serializers
from challenge.models import Car, CarType

class CarListView(ListAPIView):
    """

    """
    permission_classes = (AllowAny, )
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['car_type']
    ordering_fields = ['price', 'created']

class GetCarView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer
    lookup_field = 'id'

class CarTypeListView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = CarType.objects.all()
    serializer_class = serializers.CarTypeSerializer
