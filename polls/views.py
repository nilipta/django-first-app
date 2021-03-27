from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.

def mainF(request):
    return HttpResponse('This is polls main page')

#to show the perticular question
def details(request, question_id):
    return HttpResponse("You are showing the question %s" % question_id)

def result(request, question_id):
    myIncomingRes = "The result showing is of question %s"
    return HttpResponse(myIncomingRes % question_id) 

def vote(request, question_id):
    return HttpResponse("your vote showing on question id %s" % question_id )

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'database_questions_results': latest_question_list,
    }
    return render(request, 'polls/index.html', context)