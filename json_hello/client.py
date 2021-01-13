"X-road client example with JSON"
import requests
import pprint

class JsonClient:
    """Client class for using services.
    For each service here is a method which composes input message,
    calls the method and returns response data.
    """
    def __init__(self, xroad_client, server_url, userid=None, issue=None):
        self.xroad_client = xroad_client
        self.server_url = server_url
        self.userid = userid
        self.issue = issue
        
    def _args(self):
        headers = {'Content-Type': 'application/json; charset=utf-8',
                   'X-Road-Client': self.xroad_client,
                   }
        if self.userid:
            headers['X-Road-UserId'] = self.userid
        if self.issue:
            headers['X-Road-Issue'] = self.issue
        timeout = (5,20)
        args = {'headers': headers,
                'timeout': timeout,
                }
        return args

    def get_hello(self, id):
        args = self._args()
        url = f'{self.server_url}/hello'
        params = {'name': 'Linda'}
        print(f'\nGet hello, GET {url}')        
        return requests.get(url, params=params, **args)

def show_response(response):
    status = response.status_code
    print(f'Response status: {status}')
    try:
        json_data = response.json()
    except:
        print('Error - response is not JSON')
        print(response.text)
    else:
        print('Response received:')
        pprint.pprint(json_data)
        return json_data

def run_client():
    # security server URL
    security_server = 'http://1.2.3.4' # REPLACE WITH YOUR DATA
    json_protocol = 'r1'
    serviceid = 'roksnet-dev/COM/12998179/roksnet-producer' # REPLACE WITH YOUR DATA

    # normal URL (security server)
    url = f'{security_server}/{json_protocol}/{serviceid}'

    # local URL (without using security server, for testing only)
    url = 'http://localhost:6543/services'
    
    # X-Road-Client header value as xRoadInstance/memberClass/memberCode/subsystemCode    
    xroad_client = 'roksnet-dev/COM/12998179/roksnet-consumer'

    # X-Road-UserId header value as country code + person code
    userid = 'EE30101010007' # REPLACE WITH AUTHENTICATED USER ID

    # Service client
    reg = JsonClient(xroad_client, url, userid=userid)

    response = reg.get_hello('Linda')
    data = show_response(response)
    
if __name__ == '__main__':
    run_client()

