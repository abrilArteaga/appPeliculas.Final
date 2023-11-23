from flask import(
    Blueprint, flash, g, redirect, render_template, request,url_for, jsonify
)
from werkzeug.exceptions import abort

from appPeliculas.db import get_db

bp = Blueprint('actores', __name__, url_prefix="/actor/")
bpapi = Blueprint('api_actores', __name__, url_prefix="api/actor/")


@bp.route('/')
def index():
    db = get_db()
    actores = db.execute(
        """SELECT first_name AS Nombre, last_name AS Apellido
           FROM actor
           ORDER BY Nombre, Apellido ASC"""
    ).fetchall()
    return render_template('actor/index.html', actores=actores)

@bp.route('/int:id')
def get_actor(id):
    actores = get_db().execute(
        """SELECT *
           FROM actor
           WHERE actor_id = ?
           (id.)"""
    ).fetchone()

    pelis = get_db().execute(
        """SELECT *
           FROM actor
           WHERE actor_id = ?
           (id.)"""
        ).fetchone()
    return render_template('actores/detalle.html', actores = actores, pelis = pelis)
    

@bpapi.route('/')
def index_api():
    db = get_db()
    actores = db.execute(
        """SELECT first_name AS Nombre, last_name AS Apellido*
           FROM actor
           ORDER BY Nombre, Apellido ASC"""
    ).fetchall()
    return jsonify(actores=actores)