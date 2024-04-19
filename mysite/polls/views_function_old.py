from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse

# def index(request: HttpRequest) -> HttpResponse:
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return HttpResponse(
#         template.render(context, request)
#     )

def index(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)

# def detail(request: HttpRequest, question_id: int) -> HttpResponse:
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404('質問がない')
#     context = {
#         'question': question
#     }
#     return render(request, 'polls/detail.html', context)

def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)

def results(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/results.html', context)

def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    try :
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            "question": question,
            'error_message': '選択できていません'
        }
        return render(request, 'polls/detail.html', context)
    # tryでうまくいった場合だけ
    else:
        selected_choice.votes += 1
        selected_choice.save()
    # reverse('設定したname') argsの最後の「,」はtuple型であることを示すためにある
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))