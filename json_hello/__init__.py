from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        # static file for service description
        config.add_static_view('static', 'static')
    
        # X-road services
        config.add_route('services_hello', '/services/hello')
        config.scan()
        return config.make_wsgi_app()

