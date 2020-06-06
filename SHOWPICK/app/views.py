from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http.response import HttpResponseRedirect
from django.urls import reverse 

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