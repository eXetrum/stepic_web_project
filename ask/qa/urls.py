from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('/', views.test, 'home'),
    path('/login/', views.test, name='login'),
    path('/signup/', views.test, name='signup'),
    path('/question/<int:id>/', views.test, name='question'),
    path('/ask/', views.test, name='ask'),
    path('/popular/', views.test, name='popular'),
    path('/new/', views.test, 'new'),
]
