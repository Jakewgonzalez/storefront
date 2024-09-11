from flask import Blueprint, render_template, redirect

cart_bp = Blueprint('cart', __name__, template_folder='templates')

@cart_bp.route('/')
def index():
    return render_template('cart.html')