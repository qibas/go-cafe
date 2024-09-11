from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'American Express',
        'price': 'Rp28.000',
        'description': 'A strong black coffee drink made from espresso and hot water. Americano has a strong taste, but is not too bitter because it is mixed with water.',
        'name_person' : 'Rajendra Rifqi Baskara',
        'class_name': 'PBP C',
        'npm' : '2306245680'
    }

    return render(request, "main.html", context)