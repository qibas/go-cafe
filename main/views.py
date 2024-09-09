from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name_app': 'Go Cafe',
        'name': 'Rajendra Rifqi Baskara',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)