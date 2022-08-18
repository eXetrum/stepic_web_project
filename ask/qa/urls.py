from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('popular/', views.popular, name='popular'),
    path('question/<int:id>/', views.show_question, name='question'),
    path('ask/', views.create_question, name='ask'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('logout/', views.logout_page, name='logout'),
    path('new/', views.test),
]
