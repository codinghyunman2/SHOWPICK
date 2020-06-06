from django.shortcuts import render, get_object_or_404, redirect 
from .models import Question, Choice, Location, Store
from django.http.response import HttpResponseRedirect
from django.urls import reverse 
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
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


def home(request):
    return render(request, 'home.html')

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


def login(request):
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
    return render(request, 'registration/login.html')

