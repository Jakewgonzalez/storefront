from flask import Flask
from blueprints.app.app import app_bp
from blueprints.app.cart import cart_bp
from blueprints.app.gallery import gallery_bp
from blueprints.app.contact import contact_bp

app = Flask(__name__)
app.register_blueprint(app_bp)
app.register_blueprint(cart_bp, url_prefix='/cart')
app.register_blueprint(gallery_bp, url_prefix='/gallery')
app.register_blueprint(contact_bp, url_prefix='/contact')

if __name__ == '__main__':
    app.run(debug=True)
