from flask import Blueprint, render_template, redirect

contact_bp = Blueprint('contact', __name__, template_folder='templates')

@contact_bp.route('/')
def index():
    return render_template('contact.html')