import requests, urllib

class ASGIHandler:
    def asgi_get_handler(scope):
        server = scope.get('server')
        query_string = scope.get('headers')
        for i in query_string:
            print(i)
        # qs = urllib.parse.parse_qs(query_string)