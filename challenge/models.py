from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Car(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=32)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    year = models.PositiveSmallIntegerField(verbose_name=_('Year'))
    price = models.DecimalField(verbose_name=_('Price'), max_digits=12, decimal_places=2)
    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    car_type = models.ForeignKey('CarType', on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(verbose_name=_('Photo'))
    description = models.TextField(verbose_name=_('Description'))

class Brand(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=32)

    def __str__(self):
        return self.name

class CarType(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=32)

    def __str__(self):
        return self.name
