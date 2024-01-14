from . import main

from flask import render_template, redirect,url_for, current_app

@main.route('/')
def index():
    now_playing = current_app.movieapi.get_now_playing()
    popular= current_app.movieapi.get_popular()
    top_rated = current_app.movieapi.get_top_rated()
    upcoming = current_app.movieapi.get_upcoming()

    context = {
        'now_playing': now_playing[0:5],
        'popular': popular[5:10],
        'top_rated': top_rated[0:5],
        'upcoming': upcoming[5:15]
    }
    return render_template('index.html', **context)

@main.route('/movie/<int:movie_id>')
def movie(movie_id:int):
    movie = current_app.movieapi.get_movie_details(movie_id)
    video_key= current_app.movieapi.get_video_id(movie_id)
    similar = current_app.movieapi.get_similar_movies(movie_id)
    images= current_app.movieapi.get_movie_images(movie_id)

    context = {
        'movie': movie,
        'video_key': video_key,
        'similar': similar[0:5],
        'images': images
    }
    return render_template('main/movie.html', **context)

@main.route('/movies/<string:list_type>')
def movie_list(list_type:str):
    from flask import request
    page=request.args.get('page', 1, type=int)

    if list_type == 'now_playing':
        movies = current_app.movieapi.get_now_playing(page)
        title = 'Now Playing'
    elif list_type == 'popular':
        movies = current_app.movieapi.get_popular(page)
        title = 'Popular'
    elif list_type == 'top_rated':
        movies = current_app.movieapi.get_top_rated(page)
        title = 'Top Rated'
    elif list_type == 'upcoming':
        movies = current_app.movieapi.get_upcoming(page)
        title = 'Upcoming'
    else:
        movies = []
        title = 'Error'

    context = {
        'movies': movies,
        'title': title,
        'page': page,
    }
    return render_template('main/movie_list.html', **context)