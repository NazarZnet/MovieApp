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