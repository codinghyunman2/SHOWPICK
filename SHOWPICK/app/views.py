from django.shortcuts import render

# Create your views here.

def ceo_map(request):

    return render(request, 'CEO_map.html')

def customer_map(request):

    return render(request, "Customer_map.html")

def customer_map_Anam(request):

    return render(request, "Customer_map_Anam.html")

def customer_map_Jongam(request):

    return render(request, "Customer_map_Jongam.html")

def testing_map(request):

    return render(request, "testing_map.html")

