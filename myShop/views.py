from django.shortcuts import render
from .models import Category, Product

def categories(request):
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})


def protucts(request):
    products = Product.objects.all()
    return render(request, "products.html",  {"products": products})

def category_products(request, id):
    category = Category.objects.get(id=id)
    protucts = Product.objects.filter(category=category)
    return render(request, "category_products.html", 
                  {"category": category,
                  "products": protucts}
                  )

