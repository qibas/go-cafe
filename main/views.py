from django.shortcuts import render,redirect
from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    product_entry = Product.objects.all()
    context = {
        'name': 'American Express',
        'price': 'Rp28.000',
        'description': 'A strong black coffee drink made from espresso and hot water. Americano has a strong taste, but is not too bitter because it is mixed with water.',
        'name_person' : 'Rajendra Rifqi Baskara',
        'class_name': 'PBP C',
        'npm' : '2306245680',
        'product_entries' : product_entry,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")