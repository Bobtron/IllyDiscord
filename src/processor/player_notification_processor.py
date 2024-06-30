from injector import inject
from typing import List

from cache.player_cache import PlayerCache
from illyriad.illyriad import Illyriad
from notification_channels.incoming_channel import IncomingChannel
from notification_channels.notification_channel_interface import NotificationChannel
from data.player_notifications import PlayerNotifications

class PlayerNotificationProcessor():
    @inject
    def __init__(self, player_cache: PlayerCache, illyriad: Illyriad, incoming_channel: IncomingChannel):
        print(f'Initializing {self.__class__.__name__}')
        
        self.player_cache = player_cache
        self.illyriad = illyriad
        self.notification_channels_list: List[NotificationChannel] = [
            incoming_channel
        ]

    def process_player(self, player):
        player_notifications: PlayerNotifications = self.illyriad.get_player_notifications(player)

        if player_notifications.is_empty:
            return

        for notification_channel in self.notification_channels_list:
            notification_channel.process(player, player_notifications)

        self.player_cache.update_player_latest_notif_id(player, player_notifications.latest_notif_id)
