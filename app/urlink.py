from flask import Flask
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from handling.middlewares.auth_middleware import AuthMiddleware
from configs.configs import DB_URI
from configs.configs import DEBUG
from .migrations import make_migrations

# Creating app
app = Flask(__name__)
app.config.from_object(__name__)

# Setup middleware
app.wsgi_app = AuthMiddleware(app.wsgi_app)

# Setup database
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_ECHO'] = DEBUG
db = SQLAlchemy(app)
migrate = Migrate(app, db)
make_migrations(db, app)


# Setup sessions
SESSION_TYPE = 'redis'
Session(app)

# Setup controllers
from handling.controllers import auth

