==========
json_hello
==========

Simple example of a X-road service
----------------------------------

This is simple X-road demo server and client for playing around to get the idea how X-road services work.
This example is based on X-road REST interface using JSON.
For simplicity, this app does not connect to any database.
More complicated REST example can be found at https://github.com/Roksnet/Python-json-adapter-sqla .

Python 3 is required. As operation system you can use any modern Linux distribution, for example Ubuntu. 

For development environment you can also use Microsoft Windows. For installing Python in Windows,
we recommend to install Cygwin (http://cygwin.com/setup-x86_64.exe) and select Python 3 among
installation options.

If you have Python ready, open terminal window and create sandbox for our project environment:

.. code-block:: bash

    virtualenv-3 /srv/python-json-demo

Activate the sandbox environment for your terminal:

.. code-block:: bash
                
   . /srv/python-json-demo/bin/activate

Install required dependency packages:

.. code-block:: bash

   cd json_hello
   python setup.py develop
   
Package subdirectory json_hello contains the following files:

* server.py - includes services to be provided
* client.py - includes demo client that calls server's service
* static/openapi.yaml - service description file (OpenAPI)
  
To run the server in development mode:

.. code-block:: bash
                
   pserve –reload development.ini

Service description file is served at the following URL:

.. code-block:: bash

   http://SERVER:6543/static/openapi.yaml
   
For running client, open another terminal window and activate the environment:

.. code-block:: bash
                
   .  /srv/python-json-demo/bin/activate

Service is running with base URL:

.. code-block:: bash
                
   http://SERVER:6543/services
   
Run client:

.. code-block:: bash
                
   python -m json_hello.client

In case of success you will see some data received from the server.
In case of errors you will see error messages.

By default, the client will connect directly to the server, without using X-road.
This configuration can be handy during preliminary development phase of the server or client. 
If you see that services are working fine, you should setup services in security server.

Open browser at user interface URL of your security server (port 4000).
We assume that you have the information system already certified.
Navigate to services page and press ADD REST.
Modal window appears, insert following values:

* URL Type: OpenAPI 3 Description
* URL: http://SERVER:6543/static/openapi.yaml
* Service Code: helloservice

Save and you see the URL. Click on the service code. You see Service URL field filled with root URI of your server.
Append /services to the Service URL (http://SERVER:6543/services). Save.

Open tab ENDPOINTS. You should see here all endpoints you have described in the description file.

Add access rights to your service consumer. Access rights may be granted either for service
(tab SERVICE PARAMETERS) or individually for each endpoint (tab ENDPOINTS).

Close service form and enable the web service (click on the right of the URL).
   
To run client against X-road security server, modify client.py to use URL of the security server
instead of local URL. You need to modify:

* Your security server’s IP address
* X-road service ID data (according to the service provider in the security server)
* X-road client data (according to the client data in the security server)
* Your user ID (2 letter country code + personal code)

After these changes run client again to check how it works via X-road.
