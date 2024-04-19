from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# def index(request: HttpRequest) -> HttpResponse:
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return HttpResponse(
#         template.render(context, request)
#     )

# def index(request: HttpRequest) -> HttpResponse:
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self) -> QuerySet[Question]:
        # lte: 指定した値より小さい、もしくは同値の場合 Less than or equal to.
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

# def detail(request: HttpRequest, question_id: int) -> HttpResponse:
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404('質問がない')
#     context = {
#         'question': question
#     }
#     return render(request, 'polls/detail.html', context)

# def detail(request: HttpRequest, question_id: int) -> HttpResponse:
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         'question': question
#     }
#     return render(request, 'polls/detail.html', context)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self) -> QuerySet[Question]:
        return Question.objects.filter(pub_date__lte=timezone.now())


# def results(request: HttpRequest, question_id: int) -> HttpResponse:
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         'question': question
#     }
#     return render(request, 'polls/results.html', context)

class ResultsView(generic.DeleteView):
    model = Question
    template_name = 'polls/results.html'


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