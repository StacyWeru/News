import urllib.request ,json
import requests

from app  import app
from newsapi import NewsApiClient
from .models import Article ,Source ,Headlines

#Getting the api key
api_key = app.config ['NEWS_API_KEY']
newsapi = NewsApiClient(api_key='426ff5e837834be3926cb36886b36071')

# To fetch the top headlines
top_headlines_url = 'https://newsapi.org/v2/top-headlines'
# To fetch news articles
everything_news_url = 'https://newsapi.org/v2/everything'
# To retrieve the sources
sources_url = 'https://newsapi.org/v2/sources'


def get_source():

    get_source_url = sources_url

    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

        return source_results

def process_results(source_list):

    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        if id:
            source_object = Source(id,name,description,url)
            source_results.append(source_object)

    return source_results



