from django.shortcuts import render, redirect
from .models import Location, Store, Question, Choice, Custom_user
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.urls import reverse 

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

def mypage(request, user_pk):
    custom_user = Custom_user.objects.get(pk=user_pk)

    return render(request, "mypage.html", { "custom_user": custom_user})

def mypage_edit(request):
    if request.method == 'POST':
        Custom_user.objects.create(
            real_user = request.user,
            gender = request.POST['gender'],
            age = request.POST['age'],
            location_gu = request.POST['location_gu'],
            location_dong = request.POST['location_dong'],
            email = request.POST['email'],
        )
        return redirect('mypage')
    else:
        return render(request, 'mypage_edit.html')

def vote_index(request):
  questions = Question.objects.all()
  return render(request, 'vote_index.html', { 'questions':questions })

def vote_category(request, qid):
  categorys = get_object_or_404(Question, id=qid)
  return render(request, 'vote_category.html', { 'categorys':categorys })

def vote_store(request):
  if request.method == "POST":

    category_id = request.POST.get('questions')
    category = get_object_or_404(Choice, id = category_id)

    category.votes += 1
    category.save()
    return HttpResponseRedirect(reverse('vote_store:vote_result', args=(category.questions.id,)))

def vote_result(request, q_id):

  return render(request, 'vote_result.html', {'categorys':get_object_or_404(Question, id=q_id)})
