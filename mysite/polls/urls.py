from django.conf.urls import url

from . import views
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),




    # ex: /polls/5/
    # https://docs.djangoproject.com/en/1.10/intro/tutorial03/
    # url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
