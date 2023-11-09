from flask import(
    Blueprint, flash, g, redirect, render_template, request,url_for
)
from werkzeug.exceptions import abort

from movies.db import get_db

bp = Blueprint('lenguaje', __name__url__preflix="/lenguaje/")

@bp.route('/')
def index():
    db = get_db()
    lenguaje = db.execute(
        """SELECT l.name AS lenguaje
           FROM language l 
           ORDER BY lenguaje ASC"""
    ).fetchall()
    return render_template('lenguaje/index.html', lenguajes=lenguaje)
