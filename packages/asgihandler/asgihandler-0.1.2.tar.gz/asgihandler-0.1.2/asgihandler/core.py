import requests, urllib

class ASGIHandler:
    def asgi_get_handler(scope):
        server = scope.get('server')
        query_string = scope.get('headers').decode()
        qs = urllib.parse.parse_qs(query_string)
        print(server)
        print(query_string)
        print(qs)