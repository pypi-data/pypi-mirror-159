

class ASGIHandler:
    def asgi_get_handler(scope, receive, send):
        print(scope, receive, send)
