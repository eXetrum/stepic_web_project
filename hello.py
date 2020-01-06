

def wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [ ('Content-Type', 'text/plain')]
    query = environ['QUERY_STRING']
    body = "\n".join(query.split("&"))
    start_response(status, headers )
    return [ body ]