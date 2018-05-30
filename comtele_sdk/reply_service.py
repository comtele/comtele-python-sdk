import requests

class ReplyService(object):
    def __init__(self, api_key):
        self.__api_key = api_key

    def get_report(self, start_date, end_date, sender = ''):
        payload = {'startDate': start_date, 'endDate': end_date, 'sender': sender}

        request = requests.get('https://sms.comtele.com.br/api/v2/replyreporting', 
                         params=payload, 
                         headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()


