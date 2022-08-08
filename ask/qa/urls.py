from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^login/$', views.test),
    url(r'^signup/$', views.test),
    url(r'^question/(\d+)/$', views.test),
    url(r'^ask/$', views.test),
    url(r'^popular/$', views.test),
    url(r'^new/$', views.test),
]
