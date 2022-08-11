from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator

from .models import Question 


def test(request, *args, **kwargs):
    return HttpResponse('OK')


@require_GET
def main(request):
    try:
        pageNum = request.GET.get('page', 1)
        try:
            pageNum = int(pageNum)
        except ValueError:
            return Http404

        paginator = Question.objects.new()
        
        if(pageNum < 1 or pageNum > paginator.num_pages):
            return Http404

        page = paginator.page(pageNum)
        
        return render(request, 'main.html', { 
            'paginator': paginator,
            'page': page,
        })
    except:
        return Http404
    