from flask import Blueprint, url_for, render_template, request
from Blueprints.Stats.members import *

statsBlueprint = Blueprint('Stats', __name__, template_folder='templates', static_folder='static')

@statsBlueprint.route('/', methods=['GET', 'POST'])
def statsIndex():
    confirmed, deaths, recovered = [], [], []
    wantConfirmed, wantDeaths, wantRecovered = None, None, None
    if (request.method == 'POST'):
        allLists = organizeCovidNumbers(getCovidNumbers(request.form.get('country')))
        wantConfirmed = request.form.get('confirmed')
        wantDeaths = request.form.get('deaths')
        wantRecovered = request.form.get('recovered')

        confirmed, deaths, recovered = allLists[0], allLists[1], allLists[2]
    return render_template('stats.html', confirmed=confirmed, deaths=deaths, recovered=recovered, wantConfirmed=wantConfirmed, wantDeaths=wantDeaths, wantRecovered=wantRecovered)
