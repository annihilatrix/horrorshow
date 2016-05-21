from django.template import loader
from django.http import HttpResponse
from .models import Collection, Movie
from django.shortcuts import render_to_response, redirect


def index(request):
    """ Takes in http request, renders the main page. """
    recent_movies = Movie.objects.order_by('-release_date')[:5]
    featured_collection = Collection.objects.order_by('creation_date')[0]
    # get featured collection(s)
    template = loader.get_template('movies/index.html')
    context = {
        'recent_movies': recent_movies,
        'featured_collection': featured_collection
    }
    return HttpResponse(template.render(context, request))


def search(request):
    """ Takes in http request, returns the search_results html
        with the objects found by the search available to that template.
    """
    # Movie.objects.get(title__iexact=user-input)
    # Collection.objects.get(name=user-input)
    # Collection.objects.filter(movie_title_contaings=user-input)
    # # model fields to return
    # model_map = {Movie: ["title", "year", "plot", "release_date", "poster_loc"], Collection: ["title", "description", "creation_date", "movies"]}
    #
    # return render_to_response("movies/search_results.html")
    pass


def movies(request):
    """ Takes in http request, renders all movies, ordered by release date, paginated. """
    movies = Movie.objects.order_by('release_date')
    template = loader.get_template('movies/movies.html')
    context = {
        'movies': movies,
    }
    return HttpResponse(template.render(context, request))


def collections(request):
    """ Takes in http request, renders all collections, ordered by creation date, paginated. """
    # get all collections ordered with most recent creation date first
    collections = Collection.objects.order_by('-creation_date')
    # since we want to display each movie in the collection, get movies info
    collection_movies = Movie.attribute_answers.all() in Collection.attribute_answers.all()
    template = loader.get_template('movies/collections.html')
    context = {
        'collections': collections,
        'collection_movies': collection_movies,
    }
    return HttpResponse(template.render(context, request))


def create_collection(request):
    """ Takes http request, renders the page containing the form to create collections. """
    pass
