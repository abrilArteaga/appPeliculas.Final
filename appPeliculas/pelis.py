from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from appPeliculas.db import get_db

bp = Blueprint('pelis',__name__)

@bp.route ('/')
def index():
    db = get_db()
    pelis = db.execute(
        """SELECT l.name AS lenguaje, f.title AS titulo
            FROM language l JOIN film f ON l.language_id = f.language_id
            JOIN film f ON fa.film_id = f.film_id
            ORDER BY lenguaje ASC"""
  
    ).fetchall()
    return render_template('pelis/index.html', pelis=pelis)

def get_pelicula(id):
    pelicula = get_db().execute(
        """SELECT *
           FROM film
           WHERE film_id = ?
           (id.)"""
    ).fetchone()
