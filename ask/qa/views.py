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
        paginator = Question.objects.new(pageNum)

        return render(request, 'main.html', { 
            'paginator': paginator,
            'page': paginator.page(pageNum),
        })
    except:
        return Http404