from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.categories),
    path("products/", views.protucts),
    path("category/<int:id", views.category_products),
]