import xml.etree.ElementTree as ET
from typing import List
from injector import inject

from data.notification import Notification

class XMLParser():
    @inject
    def __init__(self):
        print(f'Initializing {self.__class__.__name__}')

    def parse_notifications(self, xml_string: str, last_processed_id: int=0) -> List[Notification]:
        return_this = []

        root = ET.fromstring(xml_string)
        if (root.tag == 'notificationsapi'):
            notifications_xml = self.__get_notifications_list(root)
            for notification_xml in notifications_xml:
                notification = self.__parse_notification(notification_xml)
                if int(notification.notification_id) > int(last_processed_id):
                    return_this.append(notification)
        else:
            raise Exception('API Key Invalid')
        return return_this

    def __get_notifications_list(self, notificationsapi_xml):
        for child in notificationsapi_xml:
            if child.tag == 'notifications':
                return child

    def __parse_notification(self, notification_xml) -> Notification:
        notif_obj = {}
        for sub_notif in notification_xml:
            # print(sub_notif)
            match sub_notif.tag:
                case 'notification':
                    notif_obj['notification_id'] = sub_notif.attrib['id']
                case 'notificationtype':
                    notif_obj['notificationtype_id'] = sub_notif.attrib['id']
                    notif_obj['notificationtype'] = sub_notif.text
                case 'notificationoveralltype':
                    notif_obj['notificationoveralltype_id'] = sub_notif.attrib['id']
                    notif_obj['notificationoveralltype'] = sub_notif.text
                case 'notificationtown':
                    notif_obj['notificationtown_id'] = sub_notif.attrib['id']
                case 'notificationdetail':
                    notif_obj['notificationdetail'] = sub_notif.text
                case 'notificationoccurrencedate':
                    notif_obj['notificationoccurrencedate'] = sub_notif.text
        return Notification(notif_obj)
