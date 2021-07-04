#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

from wsgiref import simple_server,util
from wsgiref.handlers import CGIHandler
from wsgiref.handlers import SimpleHandler

def app(environs, start_response):
    status='200 OK'
    headers=[('Content-type', 'application/x-httpd-cgi charset=utf-8')]
    body='test'.encode('utf-8')
    start_response(status, headers)
    return [body]