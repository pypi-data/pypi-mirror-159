import requests, urllib

class ASGIHandler:
    def asgi_get_handler(scope):
        server = scope.get('server')
        print(server)
        if server[0] in ['127.0.0.1', 'localhost']:
            query_string = scope.get('headers')
            host = ''
            operator = ''
            token = ''
            for i in query_string:
                if i[0].decode() == 'host':
                    host = i[1].decode()
                    continue
                elif i[0].decode() == 'operator':
                    operator = i[1].decode()
                    continue
                elif i[0].decode() == 'token':
                    token = i[1].decode()
                    continue
                else:
                    continue
            print(host, operator, token)

            # qs = urllib.parse.parse_qs(query_string)