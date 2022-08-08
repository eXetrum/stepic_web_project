from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from ask.qa.models import Question 


def test(request, *args, **kwargs):
    return HttpResponse('OK')


@require_GET
def main(request, page):
    posts = Question.objects.new(page)

    return render(request, 'main.html', { 
        'posts': posts,
    })