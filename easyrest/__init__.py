from pyramid.config import Configurator
from pyramid.events import NewRequest


# CORS fix for react
def add_cors_headers_response_callback(event):
    """Decorator for response_callback"""
    def cors_headers(request, response):
        """Function to modify every server Responce with headers:
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
            'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Authorization',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Max-Age': '1728000',
        """
        response.headers.update({
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
            'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Authorization',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Max-Age': '1728000',
        })
    event.request.add_response_callback(cors_headers)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    Initialize:
        .models: models from models folder
        pyramid_jinja2: 
        .routes: routes for app
        adds subscriber for modification of every responce(CORS fix)
    """
    with Configurator(settings=settings) as config:
        config.include('.models')
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.add_subscriber(add_cors_headers_response_callback, NewRequest)
        config.scan()
    return config.make_wsgi_app()
