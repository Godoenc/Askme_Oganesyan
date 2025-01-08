import random
from http.client import HTTPResponse

from django.core.paginator import Paginator
from django.http import HttpResponse

from django.shortcuts import render

TAGS = [
    {
        'id': i,
        'name': f'Tag {i}'
    } for i in range(1, 25)
]

QUESTIONS = [
    {
        'title': f'title {i}',
        'id': i,
        'text': f'This is text for question # {i}',
        'url': f'https://example.com/images/image_{i}.jpg',
        'description': f'This is a placeholder for image #{i}',
        'ratings': i * 3 - 1,
        'count_of_answers': i*2-1,
        'tags': [tag['name'] for tag in random.sample(TAGS, random.randint(2, 5))]
    } for i in range(1, 31)
]

HOT_QUESTIONS = [
    {
        'title': f'Hot title {i}',
        'id': i,
        'text': f'This is text for hot question # {i}',
        'url': f'https://example.com/images/image_{i}.jpg',
        'description': f'This is a placeholder for image #{i}',
        'ratings': i * 3 - 1,
        'count_of_answers': i * 2 - 1,
        'tags': [tag['name'] for tag in random.sample(TAGS, random.randint(2, 5))]
    } for i in range(1, 31)
]

ANSWERS = [
    {
        'id': i,
        'count_point': i*2,
        'check_box': i%2 == 0,
        'text': f'This is text for answer # {i}',
        'url': f'https://example.com/images/image_{i}.jpg',
    } for i in range(1, 10)
]

MEMBERS = [
    {
        'id': i,
        'name': f'Member {i}'
    } for i in range(1, 8)
]

POPULAR_TAGS = [
    {
        'id': i,
        'name': f'PopularTag {i}'
    } for i in range(1, 25)
]

def pagination(request, object_list, per_page=5):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(object_list, per_page)
    page = paginator.get_page(page_num)
    return {
        'page_obj': page,
        'object_list': page.object_list
    }



def index(request):
    paginated_data = pagination(request, QUESTIONS, per_page=5)
    return render(
        request,
        'index.html',
        context = {
            'questions': paginated_data['object_list'],
            'page_obj': paginated_data['page_obj'],
            'popular_tags': POPULAR_TAGS,
            'members': MEMBERS
        }
    )

def hot(request):
    paginated_data = pagination(request, HOT_QUESTIONS, per_page=5)
    return render(
        request,
        'hot.html',
        context = {
            'hot_questions': paginated_data['object_list'],
            'page_obj': paginated_data['page_obj'],
            'popular_tags': POPULAR_TAGS,
            'members': MEMBERS
        }
    )


def question(request, question_id):
    one_question = QUESTIONS[question_id-1]
    paginated_data = pagination(request, ANSWERS, per_page=5)
    return render(
        request,
        'question.html',
        context = {
            'one_question': one_question,
            'answers': paginated_data['object_list'],
            'page_obj': paginated_data['page_obj'],
            'popular_tags': POPULAR_TAGS,
            'members': MEMBERS
        }
    )


def question_tag(request, questiontag):
    question_of_tag = [q for q in QUESTIONS if questiontag in q['tags']]
    return render(
        request,
        'question_tag.html',
        context = {
            'question_of_tag': question_of_tag,
            'popular_tags': POPULAR_TAGS,
            'members': MEMBERS,
            'current_tag': questiontag
        }
    )


def login(request):
    return render(
        request,
        'login.html',
        context = {
            'popular_tags': POPULAR_TAGS,
            'members': MEMBERS
        }
    )


def signup(request):
    return render(
        request,
        'registration.html',
        context={
            'popular_tags': POPULAR_TAGS,
            'members': MEMBERS
        }
    )


def ask(request):
    return render(
        request,
        'ask.html',
        context={
            'popular_tags': POPULAR_TAGS,
            'members': MEMBERS
        }
    )