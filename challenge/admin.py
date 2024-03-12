from django.contrib import admin

from challenge.models import Brand, CarType, Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'year')
    list_filter = ('car_type', )

admin.site.register(Brand)
admin.site.register(CarType)
admin.site.register(Car, CarAdmin)
