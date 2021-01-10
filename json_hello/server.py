from datetime import datetime
from pyramid.view import view_config
from pyramid.response import Response

import logging
log = logging.getLogger(__name__)

# example item data
name = 'Vilma'
id = 0

# get existing ite
@view_config(route_name='services_item', renderer='json', request_method='GET')
def get_hello(request):
    _log_call(request)
    id = request.matchdict.get('id')
    return {'name': name,
            'message': f'Hello, {name}'
            }

# modify existing item
@view_config(route_name='services_item', renderer='json', request_method='PUT')
def put_hello(request):
    _log_call(request)
    id = request.matchdict.get('id')
    body = request.json_body
    if not body:    
        error = 'Body is missing or not JSON'
        return {'error': error}

    global name
    name = body.get('name')
    if not name:
        error = 'name parameter missing'
        return {'error': error}
    
    return {'name': name,
            'message': f'Hello, {name}',
            }

# add new item
@view_config(route_name='services_items', renderer='json', request_method='POST')
def post_hello(request):
    _log_call(request)

    body = request.json_body
    if not body:    
        error = 'Body is missing or not JSON'
        return {'error': error}

    global id, name

    name = body.get('name')
    if not name:
        error = 'name parameter missing'
        return {'error': error}

    id += 1
    return {'id': id,
            'message': f'Hello, {name}',
            }

def _log_call(request):
    log.info('[%s] %s %s' % (request.headers.get('X-Road-Client'),
                             request.method,
                             request.url))
