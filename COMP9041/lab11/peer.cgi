#!/usr/bin/python3

# This script allows peer.py to also be run as a CGI script

import os
from wsgiref.handlers import CGIHandler
from peer import app
if 'PATH_INFO' not in os.environ:
    os.environ['PATH_INFO'] = ''
app.secret_key = 'correct horse battery staple'
CGIHandler().run(app)
