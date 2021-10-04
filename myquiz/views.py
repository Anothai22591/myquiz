from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice


def index(request):
    return render(request, 'myquiz/index.html', {})


def detail(request):
    question_list = Question.objects.all()
    return render(request, 'myquiz/detail.html', {
        'question_list': question_list
    })


def results(request):
    all_question = Question.objects.all()
    total_point = 0
    user_ans = []
    for question in all_question:
        is_correct = request.POST.get(str(question.id), 'False')
        user_ans.append({
            'question': question.question_text,
            'given_answer': is_correct
        })
        if is_correct == 'True':
            total_point += 1

    context = {'point': total_point, 'user_ans': user_ans}
    return render(request, 'myquiz/results.html', context)


def answer(request):
    question_list = Question.objects.all()
    return render(request, 'myquiz/answer.html', {'question_list': question_list})
