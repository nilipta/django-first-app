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
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))