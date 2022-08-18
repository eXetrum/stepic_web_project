from datetime import datetime, timedelta
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.core.paginator import Paginator

from .forms import AnswerForm, AskForm, LoginForm, SignUpForm

from .models import Answer, Question 


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
        'title': 'Home',
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


@login_required()
def show_question(request, id):
    error = ''
    try:
        question = Question.objects.get(pk=id)    
    except Question.DoesNotExist:
        raise Http404

    if request.method == "POST":
        form = AnswerForm(request.POST)
        form._user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(question.get_absolute_url())

    else:
        form = AnswerForm(initial={'question': question.id})
    
    return render(request, 'view_question.html', { 
        'question': question,
        'form': form,
        'error': error,
    })
        

@login_required()
def create_question(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(question.get_absolute_url())
    else:
        form = AskForm()

    return render(request, 'create_question.html', { 'form': form })


def login_page(request):
    error, url = '', request.GET.get('next', '/')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            print('login redirect=', url)
            if user:
                login(request, user)
                return HttpResponseRedirect(url)
        else:
            error = 'Incorrect username/password'
    else:
        form = LoginForm()

    return render(request, 'login.html', { 'form': form, 'error': error, 'next': url })

def logout_page(request):
    url = request.GET.get('next', '/')
    logout(request)
    return HttpResponseRedirect(url)


def signup_page(request):
    error = ''
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            url = request.POST.get('next', '/')
            if user:
                login(request, user)
                return HttpResponseRedirect(url)
        else:
            error = 'Incorrect username/password'
    else:
        form = SignUpForm()

    return render(request, 'signup.html', { 'form': form, 'error': error })