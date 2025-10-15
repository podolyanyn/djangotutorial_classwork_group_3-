from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

# from .models import Question
class Question:
    def __init__(self, id, question_text):
        self.id = id
        self.question_text = question_text

    def __str__(self):
        return f'{self.question_text},id={self.id}'

latest_question_list = [Question(1,'question_text_1'), Question(2,'question_text_2'),
                        Question(3,'question_text_3')]
# latest_question_list = []

# def index(request):
#     # latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

def index(request):
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

def detail(request, question_id):
    try:
        # question = Question.objects.get(pk=question_id)
        question = latest_question_list[question_id - 1]
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)