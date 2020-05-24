from Models.posts import Posts

def fetchStories():
    stories = Posts.query.all()
    stories.sort(key=lambda x: x.likes, reverse=True)
    return stories