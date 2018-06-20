import requests
import json
from comtele_sdk.delivery_status import DeliveryStatus
from comtele_sdk.report_group_type import ReportGroupType


class TextMessageService(object):
    def __init__(self, api_key):
        self.__api_key = api_key

    def send(self, sender, content, receivers):
        payload = {'sender': sender, 'content': content,
                   'receivers': ','.join(receivers)}

        request = requests.post('https://sms.comtele.com.br/api/v2/send',
                                data=json.dumps(payload),
                                headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def schedule(self, sender, content, schedule_date, receivers):
        payload = {'sender': sender, 'content': content,
                   'scheduleDate': schedule_date, 'receivers': ','.join(receivers)}

        request = requests.post('https://sms.comtele.com.br/api/v2/schedule',
                                data=json.dumps(payload),
                                headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def get_detailed_report(self, start_date, end_date, delivery_status):

        delivery_status_as_string = self.__delivery_status_to_string(
            delivery_status)

        payload = {'startDate': start_date, 'endDate': end_date,
                   'delivered': delivery_status_as_string}
        request = requests.get('https://sms.comtele.com.br/api/v2/detailedreporting',
                               params=payload,
                               headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def get_consolidated_report(self, start_date, end_date, group_type):
        group_type_as_string = self.__report_group_type_to_string(group_type)

        payload = {'startDate': start_date,
                   'endDate': end_date, 'group': group_type_as_string}
        request = requests.get('https://sms.comtele.com.br/api/v2/consolidatedreporting',
                               params=payload,
                               headers={'content-type': 'application/json', 'auth-key': self.__api_key})

        return request.json()

    def __delivery_status_to_string(self, delivery_status):
        if delivery_status == DeliveryStatus.ALL:
            return 'all'
        elif delivery_status == DeliveryStatus.DELIVERED:
            return 'true'
        elif delivery_status == DeliveryStatus.UNDELIVERED:
            return 'false'

        return 'all'

    def __report_group_type_to_string(self, group_type):
        if group_type == ReportGroupType.MONTHLY:
            return 'true'
        elif group_type == ReportGroupType.DAILY:
            return 'false'

        return 'true'
