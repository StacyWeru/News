from flask import render_template , request ,redirect,url_for

from newsapi import NewsApiClient

from . import main
from ..requests import get_headlines , get_source , article_source

#Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    source = get_source()
    headlines = get_headlines()
    return render_template('index.html' , sources = source , headlines = headlines)



@main.route('/article/<id>')
def article(id):

    '''
    View articles page function that returns the articles details page and its data
    '''

    articles = article_source(id)
    return render_template ('news.html',articles = articles,id = id)

