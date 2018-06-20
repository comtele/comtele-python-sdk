import requests
import json


class BlacklistService(object):
    def __init__(self, api_key):
        self.__api_key = api_key

    def get_blacklist(self):
        request = requests.get('https://sms.comtele.com.br/api/v2/blacklist',
                               headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def get_by_phone_number(self, phone_number):
        payload = {'id': phone_number}
        request = requests.get('https://sms.comtele.com.br/api/v2/blacklist',
                               params=payload,
                               headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def insert(self, phone_number):
        payload = {'phoneNumber': phone_number}

        request = requests.post(
            'https://sms.comtele.com.br/api/v2/blacklist', data=json.dumps(payload),
            headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def remove(self, phone_number):
        payload = {'id': phone_number}

        request = requests.delete('https://sms.comtele.com.br/api/v2/blacklist',
                                  params=payload,
                                  headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()
