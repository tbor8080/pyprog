import os
import sys

from wsgiref import simple_server,util
from wsgiref.handlers import CGIHandler
from wsgiref.handlers import SimpleHandler

def write_log(file, environs):
    with open(file, "a", encoding='utf-8') as fp:
        text=f'[{environs["REQUEST_METHOD"]}/ {environs["HTTP_CONNECTION"]}] [{environs["HTTP_HOST"]}] {environs["HTTP_CONNECTION"]} ({environs["HTTP_USER_AGENT"]}):{environs["PATH_INFO"]}\n'
        fp.write(text)

def application(environs, start_response):
    status='200 OK'
    static_file="index.html"
    headers=[('Content-type', 'text/html: charset=utf-8')]
    body='hello. world'.encode('utf-8')

    
    
    fn = os.path.join("", static_file)
    start_response(status, headers)
    if os.path.exists(fn):
        return util.FileWrapper(open(fn, "rb"))

    return [body]


if __name__ == "__main__":

    path=sys.argv[1] if len(sys.argv)>1 else os.getcwd()
    host=''
    port=int(sys.argv[2]) if len(sys.argv)>2 else 8000
    
    access_log="access_log.log"
    error_log="error_log.log"
    # write_log(access_log, os.environ)
    #write_log(error_log)

    s=simple_server.make_server(host, port, application)
    print(f'Path:{path}\n',f'Listen to {host}:{port}\nshut down : control-C ')

    try:
        s.serve_forever()
    except KeyboardInterrupt:
        print("shut down")
        s.server_close()