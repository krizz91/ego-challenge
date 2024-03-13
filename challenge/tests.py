from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from challenge.models import Car, Brand, CarType

# Create your tests here.

class CarListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('list')

    def test_car_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetCarViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        brand = Brand.objects.create(name='Toyota')
        car_type = CarType.objects.create(name='Auto')
        self.car = Car.objects.create(name='Toyota', brand=brand, car_type=car_type, year=2020, price=100)
        self.url = reverse('get', kwargs={'id': self.car.id})

    def test_get_car_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CarTypeListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('type_list')

    def test_car_type_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
