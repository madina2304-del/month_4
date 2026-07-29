from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.MyFavouriteBook),
    path('about/', views.AboutMySelf),
    path('dream/', views.MyDream),
]