from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        # X-road services
        config.add_route('services_item', '/services/hello/{id}')        
        config.add_route('services_items', '/services/hello')
        config.scan()
        return config.make_wsgi_app()

