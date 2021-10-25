from django.shortcuts import render
from django.core.paginator import Paginator


# Create your views here.

questions = [
    {
        "title": f"Title {i}",
        "id":i,
        "text": f"This is text for {i} question.",
    } for i in range(20)
]


def index(request):
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "index.html", {'questions': content})


# def hot(request):
#     return render(request, "base.html", )


def tags(request):
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "tags.html", {'questions': content})


answers = [
    {
        "text": f"Answer {i}",
    }for i in range(10)
]


def question(request):
    paginator = Paginator(answers, 3)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "question.html", {'questions': content})


def login(request):
    return render(request, "login.html", {})


def signup(request):
    return render(request, "sign_up.html", {})


def ask(request):
    return render(request, "ask.html", {})


def settings(request):
    return render(request, "settings.html", {})
