from django.conf.urls import url

from . import views


urlpatterns = [
    url('', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
]