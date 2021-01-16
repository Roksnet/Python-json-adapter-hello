from datetime import datetime
from pyramid.view import view_config
from pyramid.response import Response
import logging
log = logging.getLogger(__name__)

@view_config(route_name='services_hello', renderer='json', request_method='GET')
def get_hello(request):
    "Simple X-road service"
    _log_call(request)
    error = None
    try:
        name = request.params.get('name')
        if not name:
            error = 'name parameter missing'
        else:
            res = {'name': name,
                   'message': f'Hello, {name}',
                   }
            # return response with default status code 200 OK
            return res
    except Exception as ex:
        log.error(ex)
        error = 'error occurred'

    request.response.status_code = 400
    res = {'error': error}
    return res

def _log_call(request):
    log.info('[%s] %s %s' % (request.headers.get('X-Road-Client'),
                             request.method,
                             request.url))
