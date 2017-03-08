from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question ,Choice 
def index(request):
    return render(request, 'myquiz/index.html', '')
def detail(request):
    question_list =  Question.objects.all()
    return render(request, 'myquiz/detail.html',{'question_list': question_list})

def results(request):
    c_all = Choice.objects.count()
    q_all = Question.objects.count()
    point=0
    user_ans = []
    for i in range(1,q_all+1):
        c=request.POST[str(i)]
        user_ans.append(request.POST[str(i)])
        if c == 'True':
            point+=1
    
    context = {'point':point,'user_ans':user_ans}
    return render(request, 'myquiz/results.html', context)

def answer(request):
    question_list =  Question.objects.all()
    return render(request, 'myquiz/answer.html',{'question_list': question_list})
