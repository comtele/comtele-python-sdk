import requests
import json

class AccountService(object):
    def __init__(self, api_key):
        self.__api_key = api_key

    def get_all_accounts(self):
        request = requests.get('https://sms.comtele.com.br/api/v2/accounts',                          
                         headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def get_account_by_username(self, username):
        payload = { 'id': username }
        request = requests.get('https://sms.comtele.com.br/api/v2/accounts',                          
                                params=payload,
                                headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()


