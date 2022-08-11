from multiprocessing.sharedctypes import Value
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator

from .models import Question 


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request):
    LIMIT = 10
    try:
        pageNum = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    
    qs = Question.objects.new()
    paginator = Paginator(qs, LIMIT)
    paginator.baseurl = '/?page='

    try:
        page = paginator.page(pageNum)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return paginator, page
        
    

@require_GET
def main(request):
    paginator, page = paginate(request)
      
    return render(request, 'main.html', { 
        'paginator': paginator,
        'page': page,
    })
    