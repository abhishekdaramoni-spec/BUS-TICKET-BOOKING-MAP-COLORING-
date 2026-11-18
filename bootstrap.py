import os

dirs = [
    "algorithms",
    "models",
    "routes",
    "templates",
    "templates/admin",
    "static/css",
    "static/js",
    "database",
    "tests"
]

for d in dirs:
    os.makedirs(d, exist_ok=True)

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# config.py
write_file("config.py", """
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = 'super-secret-key-for-college-project'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database', 'bus_booking.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
""")

# app.py
write_file("app.py", """
from flask import Flask
from config import Config
from models import db
from routes.main import main_bp
from routes.auth import auth_bp
from routes.booking import booking_bp
from routes.admin import admin_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
""")

# requirements.txt
write_file("requirements.txt", """
Flask==3.0.3
Flask-SQLAlchemy==3.1.1
Werkzeug==3.0.3
pytest==8.2.2
""")

# algorithms/__init__.py
write_file("algorithms/__init__.py", "")
# models/__init__.py
write_file("models/__init__.py", "from flask_sqlalchemy import SQLAlchemy\ndb = SQLAlchemy()")
# routes/__init__.py
write_file("routes/__init__.py", "")

print("Bootstrap complete.")
