# -*- coding: utf-8 -*- 
from django import forms

from .models import Answer, Question

# - форма добавления вопроса
class AskForm(forms.Form):
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
        
        return "OK"

    def save(self):
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
        pass

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer