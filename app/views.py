import string
from random import random, randrange
import random

from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from app.models import Question, Tag, Like, Answer, Profile

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
    } for i in range(100)
]
TWO_TAGS = [

    {
        "title": "Bee",
        "color": "#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    },
    {
        "title": "Honey",
        "color": "#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    }

]
TAGS = [
    {
        "title": "Bee",
        "color": "#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    },
    {
        "title": "Honey",
        "color": "#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    },
    {
        "title": "Flower",
        "color": "#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    },
    {
        "title": "Hive",
        "color": "#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    },
    {
        "title": "Sting",
        "color": "#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    },
    {
        "title": "Foam",
        "color": "#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    },
    {
        "title": "Foam",
        "color": "#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    },
    {
        "title": "Foam",
        "color": "#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    },
    {
        "title": "Foam",
        "color": "#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    },
]

HOT_QUESTIONS = [
    {
        "likes": randrange(24, 55),
        "dislikes": randrange(3, 17),
        "answers": randrange(8, 19)
    } for i in range(10)
]


def paginate(objects_list, request, per_page=10):
    paginator = Paginator(objects_list, per_page)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    return page


def index(request):
    page = paginate(QUESTIONS, request)
    return render(request, "index.html", {"questions": QUESTIONS, "page": page, "tags": TAGS, "two_tags": TWO_TAGS})


def tag(request, tag: string):
    TaggedQuestions = Question.objects.get_tagged_question(tag)
    page = paginate(TaggedQuestions, request)
    return render(request, "tag.html", {"questions": TaggedQuestions, "page": page})


def ask(request):
    return render(request, "ask.html", {"tags": TAGS})


def signup(request):
    return render(request, "signup.html", {"tags": TAGS})


def login(request):
    return render(request, "login.html", {"tags": TAGS})


def question(request, i: int):
    specific_question = Question.objects.filter(pk_exact=i)[0]

    answers = Answer.objects.question_answers(question.pk)
    answers_list = []
    for answer in answers:
        a = {
            "answer": answer,
            "avatar": Profile.objects.get_avatar(answer.author.pk)
        }
    answers_list.append(a)

    page = paginate(ANSWERS, request)

    return render(request, "question.html",
                  {"question": QUESTIONS[i], "answers": ANSWERS, "tags": TAGS, "page": page, "index": i,
                   "two_tags": TWO_TAGS})


def hot(request):
    hot_questions = Question.objects.get_hot()
    page = paginate(hot_questions)
    return render(request, "index.html", {"questions": QUESTIONS, "hot_questions": HOT_QUESTIONS, "tags": TAGS})
