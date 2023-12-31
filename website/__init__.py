from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'abc'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Longvu123@localhost/e_grocery'

    db.init_app(app)

    from .views import views
    from .auth import auth
    #from .actor import actor

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    #app.register_blueprint(actor, url_prefix = '/')

    return app

