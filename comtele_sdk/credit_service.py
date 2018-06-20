import requests
import json


class CreditService(object):
    def __init__(self, api_key):
        self.__api_key = api_key

    def get_credits(self, username):
        payload = {'id': username}
        request = requests.get('https://sms.comtele.com.br/api/v2/credits',
                               params=payload,
                               headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def get_my_credits(self):
        request = requests.get('https://sms.comtele.com.br/api/v2/credits',
                               headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def add_credits(self, username, amount):

        payload = {'id': username, 'amount': amount}
        request = requests.put('https://sms.comtele.com.br/api/v2/credits',
                               params=payload,
                               headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def get_history(self, username):
        payload = {'id': username}
        request = requests.get('https://sms.comtele.com.br/api/v2/balancehistory',
                               params=payload,
                               headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()
