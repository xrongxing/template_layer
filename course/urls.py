from django.conf.urls import url

from . import views as course_views

urlpatterns = [
    url(r'^$', course_views.index, name = 'index'),
    url(r'^course/([0-9]{4})/$', course_views.index2, name = 'index2'),
]
