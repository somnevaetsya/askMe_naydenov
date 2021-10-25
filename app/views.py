from django.shortcuts import render
from django.core.paginator import Paginator


# Create your views here.

questions = [
    {
        "title": f"Title {i}",
        "id": i,
        "text": f"This is text for {i} question.",
    } for i in range(20)
]


def pagination(request, listing, n):
    paginator = Paginator(listing, n)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return content


def index(request):
    content = pagination(request, questions, 10)
    return render(request, "index.html", {'questions': content})


def hot(request):
    return render(request, "base.html", )


def tags(request):
    content = pagination(request, questions, 5)
    return render(request, "tags.html", {'questions': content})


answers = [
    {
        "text": f"Answer {i}",
    }for i in range(10)
]


def question(request):
    content = pagination(request, answers, 5)
    return render(request, "question.html", {'questions': content})


def login(request):
    return render(request, "login.html", {})


def signup(request):
    return render(request, "sign_up.html", {})


def ask(request):
    return render(request, "ask.html", {})


def settings(request):
    return render(request, "settings.html", {})
