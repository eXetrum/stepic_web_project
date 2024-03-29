# -*- coding: utf-8 -*- 

from __future__ import unicode_literals
from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# - менеджер модели Question
class QuestionManager(models.Manager):
    # - метод возвращающий последние добавленные вопросы
    def new(self):
        return self.order_by('-pk')

    # - метод возвращающий вопросы отсортированные по рейтингу
    def popular(self):
        return self.order_by('-rating')


# - вопрос
class Question(models.Model):
    
    objects = QuestionManager() 

    # - заголовок вопроса
    title = models.CharField(max_length=255)
    
    # - полный текст вопроса  
    text = models.TextField()
    
    # - дата добавления вопроса
    added_at = models.DateTimeField(auto_now_add=True)
    
    # - рейтинг вопроса (число)
    rating = models.IntegerField(default=0)
    
    # - автор вопроса
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question_set')
    
    # - список пользователей, поставивших "лайк"
    likes = models.ManyToManyField(User, related_name='likes_set')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/question/%d/' % self.pk

    class Meta:
        db_table = 'questions'
        ordering = ['-added_at']



# - ответ
class Answer(models.Model):
    
    # - текст ответа
    text = models.TextField()

    #  - дата добавления ответа
    added_at = models.DateTimeField(auto_now_add=True)

    # - вопрос, к которому относится ответ
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # - автор ответа
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.text

    def get_absolute_url(self):
        return '/answer/%d/' % self.pk

    class Meta:
        db_table = 'answers'
        ordering = ['-added_at']