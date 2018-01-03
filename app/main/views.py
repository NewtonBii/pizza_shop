from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Roles, Pizza, Order, Toppings 
from .forms import UpdatePizza
from .. import db, photos


@main.route('/')
def index():
    """View root page function that returns index page and the various news sources"""

    title = 'Home- Welcome to the Pitch Website'
    categories = PitchCategory.get_categories()
    return render_template('index.html', title=title, categories=categories)
