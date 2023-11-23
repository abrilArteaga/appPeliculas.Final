from flask import(
    Blueprint, flash, g, redirect, render_template, request,url_for, jsonify
)
from werkzeug.exceptions import abort

from appPeliculas.db import get_db

bp = Blueprint('categoria', __name__, url_prefix="/categoria/")
bpapi = Blueprint('api_categoria', __name__, url_prefix="api/categoria/")

@bp.route('/')
def index():
    db = get_db()
    categoria = db.execute(
        """SELECT c.name AS categoria
           FROM category c 
           ORDER BY categoria ASC"""
    ).fetchall()
    return render_template('category/index.html', categoria=categoria)


@bpapi.route('/')
def index_api():
    db = get_db()
    categoria = db.execute(
        """SELECT *
           FROM category
           WHERE category_id = ?
           """,(id,)
    ).fetchall()
    return jsonify(categoria=categoria)


    