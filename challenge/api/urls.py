from django.urls import path

from challenge.api.views import CarListView, GetCarView, CarTypeListView

urlpatterns = [
    path('list/', view=CarListView.as_view(), name='list'),
    path('get/<int:id>', view=GetCarView.as_view(), name='get'),
    path('type_list/', view=CarTypeListView.as_view(), name='type_list'),
]
