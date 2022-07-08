from django.conf.urls import include, url
from qa import views

urlpatterns = [
    url(r'^$', view.test),
    url(r'^/login/', view.test),
#    url(r'^/signup/', include('qa.urls')),
#    url(r'^/question/(\d+)/$', include('qa.urls')),
#    url(r'^/ask/', include('qa.urls')),
#    url(r'^/popular/', include('qa.urls')),
#    url(r'^/new/', include('qa.urls')),
]
