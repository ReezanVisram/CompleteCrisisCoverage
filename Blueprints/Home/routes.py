from flask import Blueprint, url_for, render_template

homeBlueprint = Blueprint('Home', __name__, template_folder='templates', static_folder='static')

@homeBlueprint.route('/')
def homeIndex():
    return render_template('home.html')