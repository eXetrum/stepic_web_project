

def wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [ ('Content-Type', 'text/plain')]
    body = environ['QUERY_STRING']
    start_response(status, headers )
    return [ body ]