from django.shortcuts import render, redirect
from .models import Location, Store, Question, Choice, Custom_user, Vote, ConventionVote, Temporary_Big_Category, Temporary_Small_Category
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.urls import reverse 
import csv


# Create your views here.

def home(request):

    return render(request, 'home.html')

def customer_map(request):

    return render(request, "Customer_map.html")

def customer_map_Anam(request):
    Temporary_Big_Category.objects.all().delete()
    with open('/mnt/c/Users/User/Programming/NEXT_LION/Idea-Hackerton/Hacekrton-1430/SHOWPICK/app/data/store.csv', newline='', encoding = "euc-kr") as csvfile:
        csv_data = list(csv.reader(csvfile))

    semi_big_category = []

    for semi in range(1, len(csv_data)):
        semi_big_category.append(csv_data[semi][0])
    set_semi_big_category = set(semi_big_category)

    for i1 in set_semi_big_category:
        Temporary_Big_Category.objects.create(
            category = i1
        )
        Show_Big_Category = Temporary_Big_Category.objects.all()
    
    if request.method == "POST":
        print(request.POST)
        new_vote = Vote.objects.create(
            owner = request.user,
            image = 0,
            big_category =request.POST["Big_Category"],
            small_category = 0,
            location_dong = "안암동",
            title = 0
        )
        return redirect('customer_small_category', new_vote.pk)
    
    return render(request, 'customer_map_Anam.html', {'Show_Big_Category':Show_Big_Category})

def customer_small_category(request,vote_pk):
    semi_vote= Vote.objects.get(pk=vote_pk)
    check_big_category = semi_vote.big_category

    Temporary_Small_Category.objects.all().delete()
    with open('/mnt/c/Users/User/Programming/NEXT_LION/Idea-Hackerton/Hacekrton-1430/SHOWPICK/app/data/store.csv', newline='', encoding = "euc-kr") as csvfile:
        csv_data = list(csv.reader(csvfile))

    semi_small_category = []

    for semi in range(1, len(csv_data)):
        if csv_data[semi][0] == checkbig_category:
            semi_big_category.append(csv_data[semi][0])
    set_semi_big_category = set(semi_big_category)

    for i1 in set_semi_big_category:
        Temporary_Small_Category.objects.create(
            category = i2
        )
        Show_Small_Category = Temporary_Big_Category.objects.all()
    return render(request, "customer_small_category.html", {"Show_Small_Category":Show_Small_Category})

def customer_title(reuqest):
    for semi in range(1, len(csv_data)):
        if csv_data[semi][1] == check_small_category:
            semi_title_category.append(csv_data[semi][2])
    set_semi_title_category = set(semi_title_category)

    for i1 in set_semi_title_category:
        Temporary_Small_Category.objects.create(
            category = i1
        )
    Show_Title_Category = Temporary_Small_Category.objects.all()
    vote = Vote.objects.get(pk=vote_pk)
    Found_map1 = vote.location_dong
    Found_map2 = vote.small_category
    if request.method == "POST":
        vote = Vote.objects.get(pk=vote_pk)
        Vote.objects.filter(pk=vote_pk).update(
            title = request.POST["title_category"]
        )
        return redirect("Customer_map_Anam")
    return render(request, "customer_title.html", {"Show_Title_Category":Show_Title_Category, "Found_map1":Found_map1, "Found_map2":Found_map2})


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
    custom_user = Custom_user.objects.all()
    return render(request, "mypage.html")
    
def vote_home(request):
    return render(request, "vote_home.html")

def shop_info_anam(request):
    return render(request, "shop_info_anam.html")

def shop_info_jongam(request):
    return render(request, "shop_info_jongam.html")