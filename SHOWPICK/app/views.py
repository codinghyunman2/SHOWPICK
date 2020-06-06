from django.shortcuts import render, redirect
from .models import Location, Store
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):

    return render(request, 'home.html')

def customer_map(request):

    return render(request, "Customer_map.html")

def customer_map_Anam(request):

    return render(request, "Customer_map_Anam.html")

def customer_map_Jongam(request):

    return render(request, "Customer_map_Jongam.html")


def ceo_map(request):

    return render(request, 'CEO_map.html')

def ceo_map_Anam(request):

    return render(request, "CEO_map_Anam.html")

def ceo_map_Jongam(request):

    return render(request, "Ceo_map_Jongam.html")


def testing_map(request):

    return render(request, "testing_map.html")

def mypage(request):
    if (request.method == 'POST'):
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if (found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html', {'error': error })

        auth.login(
            request, 
            found_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect(request.GET.get('next', '/'))
    return render(request, "mypage.html")

