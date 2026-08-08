from django.urls import path
from .views import locations_view, location_detail_view, horses_view

urlpatterns = [
    path('', locations_view, name='locations'),
    path('location/<int:id>/', location_detail_view,name='location_detail'),
    path('horses/', horses_view,name='horses'),
]