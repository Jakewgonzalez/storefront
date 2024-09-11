from flask import Blueprint, render_template, redirect

app_bp = Blueprint('app', __name__, template_folder='templates')

@app_bp.route('/')
def index():
    return render_template('index.html')
