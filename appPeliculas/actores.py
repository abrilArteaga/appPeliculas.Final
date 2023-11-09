from flask import(
    Blueprint, flash, g, redirect, render_template, request,url_for
)
from werkzeug.exceptions import abort

from movies.db import get_db

bp = Blueprint('actores', __name__url__preflix="/actor/")

@bp.route('/')
def index():
    db = get_db()
    actores = db.execute(
        """SELECT first_name AS Nombre, last_name AS Apellido*
           FROM actor
           ORDER BY Nombre, Apellido ASC"""
    ).fetchall()
    return render_template('actores/index.html', actores=actores)
