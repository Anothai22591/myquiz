from django.conf.urls import url

from . import views
app_name = 'myquiz'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^results/$', views.results, name='results'),
    url(r'^answer/$', views.answer, name='answer'),
]
