import requests, json

class userCheck:
    def get_auth_check(host, operator, token):
        context = {
            "host": host,
            "operator": operator,
            "token": token
        }
        print(context)
        response = requests.post('http://192.168.1.3:8007/asgihandler/', json=context)
        res_feedback = json.loads(response.text.replace("'", '"'))
        print(res_feedback)
        print(host, operator, token)