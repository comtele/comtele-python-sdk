import requests
import json


class ContextMessageService(object):
    def __init__(self, api_key):
        self.__api_key = api_key

    def send(self, sender, context_rule_name, receivers):
        payload = {'sender': sender, 'contextRuleName': context_rule_name,
                   'receivers': ','.join(receivers)}

        request = requests.post('https://sms.comtele.com.br/api/v2/sendcontextmessage',
                                data=json.dumps(payload),
                                headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def schedule(self, sender, context_rule_name, schedule_date, receivers):
        payload = {'sender': sender, 'contextRuleName': context_rule_name,
                   'scheduleDate': schedule_date, 'receivers': ','.join(receivers)}

        request = requests.post('https://sms.comtele.com.br/api/v2/schedulecontextmessage',
                                data=json.dumps(payload),
                                headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def get_report(self, start_date, end_date, sender='', context_rule_name=''):
        payload = {'startDate': start_date, 'endDate': end_date,
                   'sender': sender, 'contextRuleName': context_rule_name}

        request = requests.get('https://sms.comtele.com.br/api/v2/contextreporting',
                               params=payload,
                               headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()
