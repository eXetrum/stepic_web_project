#from django.urls import include, path
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^popular/$', views.popular, name='popular'),
    url(r'^question/(?P<id>\d+)/$', views.show_question, name='question'),
    url(r'^ask/$', views.create_question, name='ask'),
    url(r'^login/$', views.login_page, name='login'),
    url(r'^signup/$', views.signup_page, name='signup'),
    url(r'^logout/$', views.logout_page, name='logout'),
    url(r'^new/$', views.test),
]
