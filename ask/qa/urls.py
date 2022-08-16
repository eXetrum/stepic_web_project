from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^popular/$', views.popular),
    url(r'^question/(?P<id>\d+)/$', views.show_question),
    url(r'^ask/$', views.create_question),    
    url(r'^login/$', views.test),
    url(r'^signup/$', views.test),
    url(r'^new/$', views.test),
]
