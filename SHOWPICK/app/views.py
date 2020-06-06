from django.shortcuts import render, redirect
from .models import Location, Store, Question, Choice, Vote, Custom_user, Temporary_Big_Category, Temporary_Small_Category, ConventionSmallVote, ConventionBigVote, ConventionTitleVote
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import csv
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)


# with open('/mnt/c/Users/User/Programming/NEXT_LION/Idea-Hackerton/Hacekrton-1430/SHOWPICK/app/data/store.csv', newline='', encoding = "euc-kr") as csvfile:
#     csv_data = list(csv.reader(csvfile))

# semi_big_category = []

# for semi in range(1, len(csv_data)):
#     semi_big_category.append(csv_data[semi][0])
# set_semi_big_category = set(semi_big_category)

# for i1 in set_semi_big_category:
#     Temporary_Big_Category.objects.create(
#         category = i1
    # )

from django.http.response import HttpResponseRedirect
from django.urls import reverse
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMP_DIR = os.path.join(BASE_DIR, "app", "data", "store.csv")


# Create your views here.

def home(request):

    return render(request, 'home.html')

def customer_map(request):

    return render(request, "Customer_map.html")

def customer_map_Anam(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMP_DIR = os.path.join(BASE_DIR, "app", "data", "store.csv")
    Temporary_Big_Category.objects.all().delete()
    with open(TEMP_DIR, newline='', encoding = "euc-kr") as csvfile:
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
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMP_DIR = os.path.join(BASE_DIR, "app", "data", "store.csv")
    Temporary_Big_Category.objects.all().delete()
    with open(TEMP_DIR, newline='', encoding = "euc-kr") as csvfile:
        csv_data = list(csv.reader(csvfile))

    semi_small_category = []

    for semi in range(1, len(csv_data)):
        if csv_data[semi][0] == check_big_category:
            semi_small_category.append(csv_data[semi][1])
    set_semi_small_category = set(semi_small_category)

    for i1 in set_semi_small_category:
        Temporary_Small_Category.objects.create(
            category = i1
        )
    Show_Small_Category = Temporary_Small_Category.objects.all()
    vote = Vote.objects.get(pk=vote_pk)
    Found_map1 = vote.location_dong
    Found_map2 = vote.big_category
    if request.method == "POST":

        Vote.objects.filter(pk=vote_pk).update(
            #onwer = vote.owner,
            #image =0,
            #big_category = vote.big_category,
            small_category = request.POST["Small_Category"],
            #location_dong = vote.location_dong,
            #title = 0
        )
        return redirect("customer_title", vote_pk)
    return render(request, "customer_small_category.html", {"Show_Small_Category":Show_Small_Category, "Found_map1":Found_map1, "Found_map2":Found_map2})

def customer_title(request,vote_pk):
    semi_vote= Vote.objects.get(pk=vote_pk)
    check_small_category = semi_vote.small_category

    Temporary_Small_Category.objects.all().delete()
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMP_DIR = os.path.join(BASE_DIR, "app", "data", "store.csv")
    Temporary_Big_Category.objects.all().delete()
    with open(TEMP_DIR, newline='', encoding = "euc-kr") as csvfile:
        csv_data = list(csv.reader(csvfile))

    semi_title_category = []

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
            title = request.POST["Title_Category"]
        )
        vote = Vote.objects.get(pk=vote_pk)
        big_category_one = vote.big_category
        small_category_one = vote.small_category
        title_one = vote.title

        if ConventionBigVote.objects.filter(category = big_category_one):
            semi_count = ConventionBigVote.objects.get(category = big_category_one)
            ConventionBigVote.objects.filter(category = big_category_one).update(
                vote_count = semi_count.vote_count +1
            )
        else:
            ConventionBigVote.objects.create(
                category = big_category_one,
                vote_count = 1
            )
        if ConventionSmallVote.objects.filter(category = small_category_one):
            semi_count = ConventionSmallVote.objects.get(category = small_category_one)
            ConventionSmallVote.objects.filter(category = small_category_one).update(
                vote_count = semi_count.vote_count +1
            )
        else:
            ConventionSmallVote.objects.create(
                category = small_category_one,
                vote_count = 1
            )
        if ConventionTitleVote.objects.filter(category = title_one):
            semi_count = ConventionTitleVote.objects.get(category = title_one)
            ConventionTitleVote.objects.filter(category = title_one).update(
                vote_count = semi_count.vote_count +1
            )
        else:
            ConventionTitleVote.objects.create(
                category = title_one,
                vote_count = 1
            )

        return redirect("Vote_Ending")
    return render(request, "customer_title.html", {"Show_Title_Category":Show_Title_Category, "Found_map1":Found_map1, "Found_map2":Found_map2})

def show_ceo(request):
    vote = Vote.objects.all()[0]
    Big_Vote_Results = ConventionBigVote.objects.all().order_by('-vote_count')[0:5]
    Small_Vote_Results = ConventionSmallVote.objects.all().order_by('-vote_count')[0:5]
    Title_Vote_Results = ConventionTitleVote.objects.all().order_by('-vote_count')[0:5]


    return render(request, "Show_CEO.html", {"Big_Vote_Results":Big_Vote_Results, "Small_Vote_Results":Small_Vote_Results, "Title_Vote_Results":Title_Vote_Results, "Region":vote.location_dong})

def vote_ending(request):

    return render(request, "Vote_Ending.html")

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
    semi_votes = Vote.objects.all()
    semi_array =[]
    for semi_vote in semi_votes:
        if semi_vote.owner == request.user:
            semi_array.append(semi_vote)
        
    return render(request, "mypage.html", {"Votes":semi_array})

def vote_home(request):
    return render(request, "vote_home.html")

def Shop_info_Anam(request):
    vote = Vote.objects.all()[0]
    Big_Vote_Results = ConventionBigVote.objects.all().order_by('-vote_count')[0:3]
    Small_Vote_Results = ConventionSmallVote.objects.all().order_by('-vote_count')[0:3]
    Title_Vote_Results = ConventionTitleVote.objects.all().order_by('-vote_count')[0:3]
    return render(request, "Shop_info_Anam.html", {"Big_Vote_Results":Big_Vote_Results, "Small_Vote_Results":Small_Vote_Results, "Title_Vote_Results":Title_Vote_Results, "Region":vote.location_dong})

def shop_info_jongam(request):
    return render(request, "shop_info_jongam.html")