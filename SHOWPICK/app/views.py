from django.shortcuts import render

# Create your views here.

def ceo_map(request):

    return render(request, 'CEO_map.html')

def customer_map(request):

    return render(request, "Customer_map.html")

