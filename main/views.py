from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product

# Create your views here.
def show_main(request):
    product_list = Product.objects.all()
    
    context = {
        'name': 'Ahmad Anggara Bayuadji Prawirosoenoto',
        'class': 'PBP A',
        'product_list' : product_list # DONT FORGET TO DOUBLE CHECK THIS??? IDK WHAT TO DO
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form' : form}
    return render(request, "create_product.html", context)

def show_product(request, name):
    product = get_object_or_404(Product, pk=name)
    
    context = {
        'product' : product
    }
    
    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    product_data = serializers.serialize("xml", product_list)
    return HttpResponse(product_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    product_data = serializers.serialize("json", product_list)
    return HttpResponse(product_data, content_type="application/json")

def show_xml_by_id(request, name):
    try:
        product_list = Product.objects.filter(pk=name)
        product_data = serializers.serialize("xml", product_list)
        return HttpResponse(product_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, name):
    try:
        product_list = Product.objects.filter(pk=name)
        product_data = serializers.serialize("json", product_list)
        return HttpResponse(product_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def test(requets): # tes rebuild
    return requets