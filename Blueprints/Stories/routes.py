from flask import Blueprint, render_template, url_for, request, redirect
from Models.posts import Posts
from Models import db
from Blueprints.Stories.members import *

storiesBlueprint = Blueprint("Stories", __name__, template_folder="templates", static_folder="static")

@storiesBlueprint.route('/')
def storiesHome():
    stories = fetchStories()
    return render_template('storieshome.html', stories=stories)

@storiesBlueprint.route('/like/<int:id>', methods=["GET", "POST"])
def likeStory(id):
    storyToLike = Posts.query.get_or_404(id)

    storyToLike.likes += 1

    db.session.commit()

    return redirect('/stories')

@storiesBlueprint.route('/create/', methods=["GET", "POST"])
def createStory():
    if (request.method == "POST"):
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        if (author != '' and title != '' and content != ''):
            currStory = Posts(author=author, title=title, content=content)

            db.session.add(currStory)
            db.session.commit()
            return redirect('/stories')
        else:
            return redirect('/stories/create')

    return render_template('create.html')