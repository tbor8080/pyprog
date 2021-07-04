import os
import sys

from wsgiref import simple_server,util
from wsgiref.handlers import CGIHandler
from wsgiref.handlers import SimpleHandler
# application
from test import app
# 継承
class _Wsgi(SimpleHandler):

    def __init__(self,stdin, stdout, stderr, environs):
        self.stdin=stdin
        self.stdout=stdout
        self.stderr=stderr
        self.environs=environs
        self.path=sys.argv[1] if len(sys.argv)>1 else os.getcwd()
        self.host=''
        self.port=int(sys.argv[2]) if len(sys.argv)>2 else 8000

    def run(self,application):
        return application

    def setPath(self, path):
        return os.path.join("", path)


# mimetype: application/x-httpd-python application/x-httpd-cgi

def cgi_application(environs, start_response):
    status='200 OK'
    headers=[('Content-type','application/x-httpd-python charset=utf-8')]
    body='hello. world'.encode('utf-8')
    #fn = os.path.join("/","")
    fn = os.path.join("","test.py")
    os.path.append("/test","test.py")
    if os.path.exists(fn):
        start_response(status, headers)
        return util.FileWrapper(open(fn, "rb"))
    # print(environs)
    else:
        return [body]

# print(os.environ)

if __name__ == "__main__":
    path=sys.argv[1] if len(sys.argv)>1 else os.getcwd()
    host=''
    port=int(sys.argv[2]) if len(sys.argv)>2 else 8000

    access_log="access_log.log"
    error_log="error_log.log"
    
    # s=simple_server.make_server(host, port, app)
    # CGIHandler().run(app)
    # print(f'{host}:{port} control-C Shut down')
    # s.serve_forever()
    test = _Wsgi(sys.stdin,sys.stdout,sys.stderr,os.environ)
    test.run(app)
    print(test.get_stdin(),os.environ)

