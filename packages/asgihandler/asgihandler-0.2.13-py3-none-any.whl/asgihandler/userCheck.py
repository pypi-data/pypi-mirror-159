import requests

class userCheck:
    def get_auth_check(host, operator, token):
        context = {
            "host": host,
            "operator": operator,
            "token": token
        }
        print(context)
        response = requests.post('http://192.168.1.3:8007/asgihanlder/', json=context)
        print(response.status_code)
        print(host, operator, token)