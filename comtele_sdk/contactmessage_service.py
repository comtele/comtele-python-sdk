import requests
import json


class ContactMessageService(object):
    def __init__(self, api_key):
        self.__api_key = api_key

    def send(self, sender, content, group_name):
        payload = {'sender': sender,
                   'content': content, 'groupName': group_name}

        request = requests.post('https://sms.comtele.com.br/api/v2/sendcontactmessage',
                                data=json.dumps(payload),
                                headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def schedule(self, sender, content, group_name, schedule_date):
        payload = {'sender': sender, 'content': content,
                   'scheduleDate': schedule_date, 'groupName': group_name}

        request = requests.post('https://sms.comtele.com.br/api/v2/schedulecontactmessage',
                                data=json.dumps(payload),
                                headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()
