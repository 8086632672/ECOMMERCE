from django.shortcuts import get_object_or_404, render
from models import Category, Product


def index():
    from django.http import HttpResponse
    return HttpResponse("hi...:-)")


def allProdCat(request, c_slug=None):
    c_page = None
    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.all().filter(category=c_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request, "category.html", {'category': c_page, 'products': products})
