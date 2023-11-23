from flask import(
    Blueprint, flash, g, redirect, render_template, request,url_for, jsonify
)
from werkzeug.exceptions import abort

from appPeliculas.db import get_db

bp = Blueprint('lenguaje', __name__, url_prefix="/lenguaje/")
bpapi = Blueprint('api_lenguaje', __name__, url_prefix="api/lenguaje/")

@bp.route('/')
def index():
    db = get_db()
    lenguaje = db.execute(
        """SELECT l.name AS lenguaje
           FROM language l 
           ORDER BY lenguaje ASC"""
    )
    return render_template('lenguaje/index.html', lenguajes=lenguaje)

bp.route('/')
def index():
    db = get_db()
    lenguaje = db.execute(
        """SELECT *
           FROM lenguaje
           ORDER BY lenguaje_id =?
           (id.)"""
    ).fetchone()

@bpapi.route('/')
def index_api():
    db = get_db()
    lenguaje = db.execute(
        """SELECT l.name AS lenguaje
           FROM language l 
           ORDER BY lenguaje ASC"""
    ).fetchall()
    return jsonify(lenguajes=lenguaje)
                       

