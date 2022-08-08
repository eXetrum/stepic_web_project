from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator

from .models import Question 


def test(request, *args, **kwargs):
    return HttpResponse('OK')


@require_GET
def main(request):
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)

    posts = Question.objects.new()
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/question/'
    page = paginator.page(page)

    return render(request, 'main.html', { 
        'posts': page.object_list,
        'paginator': paginator,
        'page': page,
    })