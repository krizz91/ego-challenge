from django.contrib import admin

from challenge.models import Brand, CarType, Car

# Register your models here.

admin.site.register(Brand)
admin.site.register(CarType)
admin.site.register(Car)