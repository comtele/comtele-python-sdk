import requests
import json


class TokenService(object):
    def __init__(self, api_key):
        self.__api_key = api_key

    def send_token(self, phone_number, prefix):
        payload = {'phoneNumber': phone_number, 'prefix': prefix}

        request = requests.post('https://sms.comtele.com.br/api/v2/tokenmanager',
                                data=json.dumps(payload),
                                headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def send_token_without_prefix(self, phone_number):
        return self.send_token(phone_number, '')

    def validate_token(self, token_code):
        payload = {'tokenCode': token_code}

        request = requests.put('https://sms.comtele.com.br/api/v2/tokenmanager',
                               data=json.dumps(payload),
                               headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()
