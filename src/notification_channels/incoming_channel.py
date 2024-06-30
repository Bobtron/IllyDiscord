from injector import inject
from typing import List
import re

from notification_channels.notification_channel_interface import NotificationChannel
from discord.discord import Discord
from data.player import Player
from data.player_notifications import PlayerNotifications
from cache.metadata_cache import MetadataCache
from data.notification import Notification

class IncomingChannel(NotificationChannel):
    @inject
    def __init__(self, discord: Discord, metadata_cache: MetadataCache):
        print(f'Initializing {self.__class__.__name__}')
        super().__init__(discord, metadata_cache)

    def process(self, player: Player, player_notifications: PlayerNotifications) -> None:
        webhook_url: str = self.metadata_cache.channel_to_webhook_url['INCOMING_WEBHOOK_URL']

        notifs_to_post: List[Notification] = self.sort_notifications_asc(self.filter_notifications(player_notifications.notifications))

        player_regex = re.compile(r"\[@ps=(.*?)\|.*?\]")
        town_regex = re.compile(r"\[@t=(.*?)\|.*?\]")

        for notif in notifs_to_post:
            notif_detail = notif.notificationdetail
            notif_detail = player_regex.sub(r"\1", notif_detail)
            notif_detail = town_regex.sub(r"\1", notif_detail)

            notif_detail = f"Hey <@{player.discord_user_id}> - {notif.notificationtype} | {notif_detail}"

            print(notif_detail)
            
            self.discord.post_message_to_webhook(webhook_url, notif_detail)

        

    def filter_notifications(self, notifications_list: List[Notification]) -> List[Notification]:
        return list(filter(self.is_hostile_incoming, notifications_list))

    def is_hostile_incoming(self, notification: Notification) -> bool:
        return (notification.notificationtown_id != "0"
            and "68" == notification.notificationtype_id
            and "inbound" in notification.notificationdetail
            and "with Hostile intentions" in notification.notificationdetail
        )

