from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from appPeliculas.db import get_db

bp = Blueprint('pelis',__name__)
bpapi = Blueprint('api_pelis',__name__, url_prefix='api/pelis')

@bp.route ('/')
def index():
    db = get_db()
    pelis = db.execute(
        """SELECT title AS Peliculas, first_name AS Nombre, last_name AS Apellidos
            FROM actor a JOIN film_actor fa ON a.actor_id = fa.actor_id
            JOIN film f ON fa.film_id = f.film_id
            ORDER BY Peliculas ASC"""
  
    ).fetchall()
    return render_template('pelis/index.html', pelis=pelis)

def get_pelicula(id):
    pelis = get_db().execute(
    """SELECT *
       FROM film
       WHERE film_id = ?
       (id.)"""
    ).fetchone()


def get_pelicula(id):
    actores = get_db().execute(
        """SELECT *
           FROM actor
           WHERE actor_id = ?
           (id.)"""
    ).fetchone()
    return render_template('pelis/detalle.html', pelis = pelis, actores = actores)


@bpapi.route ('/')
def index_api():
    db = get_db()
    pelis = db.execute(
        """SELECT title AS Peliculas, first_name AS Nombre, last_name AS Apellidos
            FROM actor a JOINfilm_actor fa ON a.actor_id = fa.actor_id
            JOIN film f ON fa.film_id = f.film_id
            ORDER BY Peliculas ASC"""
  
    ).fetchall()
    return jsonify (pelis=pelis)
