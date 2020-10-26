# News Api

## By Stacy Weru 

## Description
This is a web application that helps one to view various news from various sources .It helps on catching up with top news.It is built using the NEWS API.

The site can be viewed at https://catchupnews-app.herokuapp.com/

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv

### Cloning
* In your terminal:

        $ git clone https://github.com/emdeechege/NewsApi/
        $ cd NewsPI

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ python3.6 -m pip install Flask
        $ python3.6 -m pip install Flask-Bootstrap
        $ python3.6 -m pip install Flask-Script

* Setting up the API Key

        To be able to gather article info from the News API you will need an API Key.

        * Visit https://newsapi.org/ and register for an API key.
        * In the root directory of the project folder create a file: start.sh
        * Insert the following info into it:

                export NEWS_API_KEY='<Your-Api-Key>'
                python3.6 manage.py server

        * Insert the API Key you received from News Api where <Your-Api-Key> is.

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py tests

## Technologies Used
* Python3.6
* Flask

## License

Copyright (c) 2020 StacyWeru
