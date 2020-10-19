from flask import render_template , request ,redirect,url_for

from newsapi import NewsApiClient

from . import main

#Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    source = get_source()
    


@main.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''

    news_id = 'News article page of your choice'
    return render_template ('news.html', id = news_id)

