from injector import inject
import requests
from typing import List

from illyriad.xml_parser import XMLParser
from data.player_notifications import PlayerNotifications
from data.notification import Notification

class Illyriad():
    @inject
    def __init__(self, xml_parser: XMLParser):
        print(f'Initializing {self.__class__.__name__}')
        self.xml_parser = xml_parser

    def get_player_notifications(self, player) -> PlayerNotifications:
        result = requests.get(f'https://elgea.illyriad.co.uk/external/notificationsapi/{player.notif_api_key}',
            params={
                'LastNotificationID': player.latest_notif_id
            },
            timeout=20
        )

        assert result.status_code == 200

        notifications_list: List[Notification] = self.xml_parser.parse_notifications(result.text, player.latest_notif_id)

        return PlayerNotifications(notifications_list)
