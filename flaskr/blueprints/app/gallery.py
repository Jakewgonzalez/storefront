from flask import Blueprint, render_template, redirect

gallery_bp = Blueprint('gallery', __name__, template_folder='templates')

@gallery_bp.route('/')
def index():
    return render_template('gallery.html')