from django.shortcuts import render, Http404, get_object_or_404

# Create your views here.

from .models import Product,ProductImage


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = Product.objects.filter(title__icontains= q)
        context = {'query': q, 'products': products}
        template = 'products/search.html'
    else:
        template = 'products/home.html'
        context = {}

    return render(request, template, context)

def home(request):
    products = Product.objects.all()
    context = {"products": products}
    template = 'products/home.html'
    return render(request, template, context)

def all(request):
    products = Product.objects.all()
    context = {"products": products}
    template = 'products/all.html'

    return render(request, template, context)

def single(request, slug):
    try:
        product = Product.objects.get(slug = slug)
        images = ProductImage.objects.filter(product = product)
        context = {"product": product, "images": images}
        template = 'products/single.html'
        return render(request, template, context)
    except :
        raise Http404