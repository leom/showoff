#!/usr/bin/env python
from flup.server.fcgi import WSGIServer
from run_admin import app

WSGIServer(app, bindAddress=app.config['ADMIN_FCGI_SOCKET']).run()
