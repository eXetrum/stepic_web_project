# -*- coding: utf-8 -*- 
from django import forms
from django.contrib.auth.models import User

from .models import Answer, Question

# - форма добавления вопроса
class AskForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(AskForm, self).__init__(*args, **kwargs)

    # - поле заголовка
    title = forms.CharField(max_length=255)
    # - поле текста вопроса
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        title = self.cleaned_data['title']
        text = self.cleaned_data['text']
        
        if title is None or len(title) == 0:
            raise forms.ValidationError(u'Введите заголовок вопроса')
        
        if text is None or len(text) == 0:
            raise forms.ValidationError(u'Введите текст вопроса')
        
        return self.cleaned_data 

    def save(self):
        # No auth yet...
        user, _ = User.objects.get_or_create(username='test', password='test')
        self.cleaned_data['author'] = user

        question = Question(**self.cleaned_data)
        question.save()
        return question

# - форма добавления ответа
class AnswerForm(forms.Form):
    # - поле текста ответа
    text = forms.CharField(widget=forms.Textarea)
    
    # - поле для связи с вопросом
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean(self):
        text = self.cleaned_data['text']
        question = self.cleaned_data['question']
        
        if text is None or len(text) == 0:
            raise forms.ValidationError(u'Введите текст ответа')
        
        if question is None:
            raise forms.ValidationError(u'Форма не валидна. Поле question не найдено')
        
        return self.cleaned_data 

    def save(self):
        question = self.cleaned_data['question']
        question = Question.objects.get(id=question)
        self.cleaned_data['question'] = question
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer