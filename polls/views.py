from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question
from django.views import generic
from .forms import QuestionForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
import random

# class IndexView(LoginRequiredMixin, generic.ListView):
#     template_name = "polls/index.html"
#     context_object_name = "latest_question_list"
#
#     # def get_queryset(self):
#     #     """Return the last five published questions."""
#     #     return Question.objects.order_by("-pub_date")[:5]
#
#     def get_queryset(self):
#         """
#         Return the last five published questions (not including those set to be
#         published in the future).
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

# function for lesson 45 - experiments with async
def index(request):
    latest_question_list = Question.objects.order_by('?')[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


class DetailView(generic.DetailView):
    model = Question
    # template_name = "polls/question_detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/question_detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

# @login_required
# @permission_required("polls.add_question")
def new_question(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = QuestionForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            print(form.cleaned_data)
            # process the data in form.cleaned_data as required
            question = Question(
                question_text = form.cleaned_data["question_text"],
                pub_date = form.cleaned_data["pub_date"],
            )
            question.save()
            # redirect to a new URL:
            # return HttpResponseRedirect("pools/thanks/")
            return HttpResponseRedirect(reverse("polls:thanks"))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuestionForm()

    return render(request, "polls/new_question.html", {"form": form})

def thanks(request):
    return HttpResponse('  THANKS !')


def hello(request):
    greetings = [
        "hello, world",
        "hi, universe",
        "hey there, world",
        "hello, folks",
        "greetings, earthlings",
        "salutations, world",
        "yo, world",
        "bonjour, le monde",
        "hola, mundo",
        "ciao, mondo",
        "hallo, welt",
        "こんにちは、世界",  # Japanese
        "안녕하세요, 세계",  # Korean
        "привіт, світе",
        "добрий день, світ",
        "γειά σου, κόσμε",  # Greek
        "سلام دنیا",  # Persian
        "שלום עולם",  # Hebrew
        "नमस्ते दुनिया",  # Hindi
        "olá, mundo",
        "hello, planet",
        "hey, all",
        "hiya, world",
        "howdy, world",
        "welcome, world",
        "peace, world",
        "what's up, world?",
        "top of the morning, world",
        "cheerio, world",
        "ahoj, světe"  # Czech
    ]
    return HttpResponse(random.choice(greetings))

def request_to_nbu(request):
    import json
    from datetime import date, timedelta, datetime
    import requests
    import time

    start = time.time()
    current_day = date.today()
    result = []
    url = f'https://bank.gov.ua/NBU_Exchange/exchange?json&date={(current_day - timedelta(days=random.randint(1,30))).strftime("%d.%m.%Y")}'
    response = requests.get(url)
    result += response.json()
    return HttpResponse(result)