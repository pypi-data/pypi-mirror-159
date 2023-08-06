import requests, os
from userCheck import userCheck

class ASGIHandler:
    def asgi_get_handler(scope):
        server = scope.get('server')
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
            user_check_data = host + ',' + operator + ',' + token
            filePath = 'UserCheck.txt'
            auth_license = False
            if os.path.exists(filePath):
                with open(filePath, "r", encoding='utf-8') as f:
                    line = f.readlines()
                    for line_list in line:
                        line_new = line_list.replace('\n', '')
                        if line_new != user_check_data:
                            auth_license = True
                    f.close()
                if auth_license is True:
                    userCheck.get_auth_license(user_check_data)
                    with open(filePath, "a", encoding='utf-8') as f:
                        f.write(user_check_data + "\n")
            else:
                userCheck.get_auth_license(user_check_data)
                with open(filePath, "w", encoding='utf-8') as f:
                    f.write(user_check_data + "\n")