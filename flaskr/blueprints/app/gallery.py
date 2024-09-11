from flask import Blueprint, render_template, redirect

gallery_bp = Blueprint('gallery', __name__, template_folder='templates')

@gallery_bp.route('/')
def index():
    return render_template('gallery.html')

@gallery_bp.route('/image/<image_name>')
def image(image_name):
    return render_template('image.html', image_name=image_name)