from flask import(
    Blueprint, flash, g, redirect, render_template, request,url_for
)
from werkzeug.exceptions import abort

from movies.db import get_db

bp = Blueprint('categoria', __name__url__preflix="/categoria/")

@bp.route('/')
def index():
    db = get_db()
    categorias = db.execute(
        """SELECT c.name AS categoria
           FROM category 
           ORDER BY categoria ASC"""
    ).fetchall()
    return render_template('categoria/index.html', categorias=categorias)
