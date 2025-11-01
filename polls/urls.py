from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    path("", views.index, name="index"), #for lesson 45 - experiments with async
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("new_question/", views.new_question, name="new_question"),
    path("thanks/", views.thanks, name="thanks"),
    path("hello/", views.hello, name="hello"),
    path("request_to_nbu/", views.request_to_nbu, name="request_to_nbu"),
]