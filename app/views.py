import string
from random import random, randrange

from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

QUESTIONS = [
    {
        "title": f"Title #{i}",
        "text": f"This is text for question #{i}",
        "number": i,
    } for i in range(100)

]

ANSWERS = [
    {
        "title": f"Answer#{i}",
        "text": f"This is text for answer #{i}",
        "number": i,
    } for i in range(10)
]

TAGS = [
    {
        "title": f"Answer#{i}",
        "text": f"This is text for answer #{i}",
        "number": i,
    } for i in range(10)
]

HOT_QUESTIONS= [
    {
        "likes": randrange(24, 55),
        "dislikes": randrange(3, 17),
        "answers": randrange(8, 19)
    } for i in range(10)
]



def paginate(objects_list, request, per_page=10):
    question_paginator = Paginator(objects_list, per_page)
    page_num = request.GET.get('page')
    page = question_paginator.get_page(page_num)
    return page


def index(request):
    page = paginate(QUESTIONS,request)
    return render(request, "index.html", {"questions": QUESTIONS, "page": page})


def tag(request, s: string):
    return render(request, "tag.html", {"questions": QUESTIONS, "tag": s})


def ask(request):
    return render(request, "ask.html")


def signup(request):
    return render(request, "signup.html")


def login(request):
    return render(request, "login.html")


def question(request, i: int):
    return render(request, "question.html", {"question": QUESTIONS[i], "answers": ANSWERS})


def hot(request):
    return render(request, "index.html", {"questions": QUESTIONS, "hot_questions": HOT_QUESTIONS})
