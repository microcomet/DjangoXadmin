# from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Question
# Create your views here.


def index(request):
    lasted_question_list = Question.objects.order_by('-pub_date')[0:5]
    content = {
        'latest_question_list': lasted_question_list
    }
    return render(request, 'polls/index.html', content)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id, question_id2):
    print question_id
    print question_id2
    return HttpResponse("You're voting on question %s." % question_id)
