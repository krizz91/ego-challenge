from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from challenge import serializers
from challenge.models import Car

class CarListView(ListAPIView):
    """

    """
    permission_classes = (AllowAny, )
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer


class GetCarView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer
    lookup_field = 'id'
