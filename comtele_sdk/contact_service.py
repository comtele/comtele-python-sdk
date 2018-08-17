import requests
import json


class ContactService(object):
    def __init__(self, api_key):
        self.__api_key = api_key

    def create_group(self, group_name, group_description):
        payload = {'name': group_name, 'description': group_description}

        request = requests.post('https://sms.comtele.com.br/api/v2/contactgroup',
                                data=json.dumps(payload),
                                headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def remove_group(self, group_name):
        payload = {'groupName': group_name}

        request = requests.delete('https://sms.comtele.com.br/api/v2/contactgroup',
                                  params=payload,
                                  headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def get_all_groups(self):
        request = requests.get('https://sms.comtele.com.br/api/v2/contactgroup',
                               headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def get_group_name(self, group_name):
        payload = {'groupName': group_name}

        request = requests.get('https://sms.comtele.com.br/api/v2/contactgroup',
                               params=payload,
                               headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def add_contact_to_group(self, group_name, contact_phone, contact_name):
        payload = {'groupName': group_name,
                   'contactPhone': contact_phone, 'contactName': contact_name, 'action': 'add_number'}

        request = requests.put('https://sms.comtele.com.br/api/v2/contactgroup',
                               data=json.dumps(payload),
                               headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def remove_contact_from_group(self, group_name, contact_phone):
        payload = {'groupName': group_name,
                   'contactPhone': contact_phone, 'action': 'remove_number'}

        request = requests.put('https://sms.comtele.com.br/api/v2/contactgroup',
                               data=json.dumps(payload),
                               headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()
