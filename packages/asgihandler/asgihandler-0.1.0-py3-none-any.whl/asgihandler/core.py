

class ASGIHandler:
    def asgi_get_handler(self, scope, receive, send):
        print(scope, receive, send)
