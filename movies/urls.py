from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search', views.search, name='search'),
    url(r'^movies', views.movies, name='movies'),
    url(r'^collections', views.collections, name='collections'),
    url(r'^create_collection', views.create_collection, name='create_collection'),
    url(r'^movie/(?P<imdb_id>[\w\-]+)/$', views.movie_detail, name='movie_detail'),
    url(r'^collection/(?P<collection_id>[0-9]+)/$', views.collection_detail, name='collection_detail'),
    # data import URLs
    url(r'^guidebox_import', views.guidebox_import, name='guidebox_import'),
    url(r'^omdb_import', views.omdb_import, name='omdb_import'),
]
