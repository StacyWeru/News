from flask import render_template
from app import app

#Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Welcome to A Catch-Up news Website'
    return render_template ('index.html' , title = title)


@app.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''

    news_id = 'News article page of your choice'
    return render_template ('news.html', id = news_id)

