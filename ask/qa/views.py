from multiprocessing.sharedctypes import Value
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator

from .models import Question 


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, qs, limit=10):
    MIN_LIMIT, MAX_LIMIT, DEFAULT_LIMIT = 1, 100, 10
    try:
        limit = int(limit)
        if limit < MIN_LIMIT or limit > MAX_LIMIT:
            limit = DEFAULT_LIMIT

    except ValueError:
        raise Http404
    
    try:
        pageNum = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    

    
    paginator = Paginator(qs, limit)
    paginator.baseurl = '/?page='

    try:
        page = paginator.page(pageNum)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return paginator, page
        
    

@require_GET
def home(request):
    LIMIT = 10
    qs = Question.objects.new()
    paginator, page = paginate(request, qs, LIMIT)

    return render(request, 'list.html', { 
        'paginator': paginator,
        'page': page,
    })

@require_GET
def popular(request):
    LIMIT = 10
    qs = Question.objects.popular()
    paginator, page = paginate(request, qs, LIMIT)

    return render(request, 'list.html', { 
        'paginator': paginator,
        'page': page,
    })

@require_GET
def question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        return render(request, 'question.html', { 
            'question': question_id,
        })
    except Question.DoesNotExist:
        raise Http404    