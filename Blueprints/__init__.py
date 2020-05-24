from flask import Flask, redirect, render_template, url_for
from Models import db
from Models.posts import Posts
from flask_bootstrap import Bootstrap
from Blueprints.Home.routes import homeBlueprint
from Blueprints.Stats.routes import statsBlueprint
from Blueprints.Stories.routes import storiesBlueprint
import os


def createApp():    
    app = Flask(__name__)
    Bootstrap(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/openhacksmay23'
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    db.init_app(app)
    app.register_blueprint(Home.routes.homeBlueprint, url_prefix="/home")
    app.register_blueprint(Stats.routes.statsBlueprint, url_prefix="/stats")
    app.register_blueprint(Stories.routes.storiesBlueprint, url_prefix="/stories")
    return app

app = createApp()

@app.route('/')
def homeIndex():
    return redirect(url_for('Home.homeIndex'))


