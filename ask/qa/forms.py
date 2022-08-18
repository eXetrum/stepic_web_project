# -*- coding: utf-8 -*- 
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Answer, Question


class LoginForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username is None or len(username) == 0:
            raise forms.ValidationError(u'Введите имя пользователя')
        
        if password is None or len(password) == 0:
            raise forms.ValidationError(u'Введите пароль')

        if authenticate(username=username, password=password) is None:
            raise forms.ValidationError(u'Логин/Пароль неверны')
        
        return self.cleaned_data 

    def save(self):
        return authenticate(**self.cleaned_data)
    

class SignUpForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username is None or username.strip() == '':
            raise forms.ValidationError(u'Username is empty', code='validation_error')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email is None or email.strip() == '':
            raise forms.ValidationError(u'Email is empty', code='validation_error')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password is None or password.strip() == '':
            raise forms.ValidationError(u'Password is empty', code='validation_error')
        return password

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        return authenticate(**self.cleaned_data)

# - форма добавления вопроса
class AskForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(AskForm, self).__init__(*args, **kwargs)

    # - поле заголовка
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # - поле текста вопроса
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def clean(self):
        title = self.cleaned_data.get('title')
        text = self.cleaned_data.get('text')
        
        if title is None or len(title) == 0:
            raise forms.ValidationError(u'Введите заголовок вопроса')
        
        if text is None or len(text) == 0:
            raise forms.ValidationError(u'Введите текст вопроса')
        
        return self.cleaned_data 

    def save(self):
        self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question

# - форма добавления ответа
class AnswerForm(forms.Form):
    # - поле текста ответа
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    # - поле для связи с вопросом
    question = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'form-control'}))

    def clean(self):
        text = self.cleaned_data.get('text')
        question = self.cleaned_data.get('question')
        
        if text is None or len(text) == 0:
            raise forms.ValidationError(u'Введите текст ответа')
        
        if question is None or question == 0:
            raise forms.ValidationError(u'Форма не валидна. Поле question не найдено')
        
        return self.cleaned_data 

    def save(self):
        question = self.cleaned_data.get('question')
        self.cleaned_data['question'] = Question.objects.get(pk=question)
        self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer