from django.conf.urls import url

from . import views
app_name = 'myquiz'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^results/$', views.results, name='results'),
    url(r'^show_score/$', views.show_score, name='show_score'),
]
