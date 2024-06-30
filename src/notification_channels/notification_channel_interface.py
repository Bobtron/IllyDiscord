from typing import List

from discord.discord import Discord
from data.player import Player
from data.player_notifications import PlayerNotifications
from data.notification import Notification
from cache.metadata_cache import MetadataCache

class NotificationChannel():
    def __init__(self, discord: Discord, metadata_cache: MetadataCache):
        print(f'Initializing {self.__class__.__name__}')
        self.discord = discord
        self.metadata_cache = metadata_cache

    def process(self, player: Player, player_notifications: PlayerNotifications) -> None:
        raise NotImplementedError()

    def filter_notifications(self, notifications_list: List[Notification]) -> List[Notification]:
        raise NotImplementedError()

    def sort_notifications_asc(self, notifications_list: List[Notification]) -> List[Notification]:
        return sorted(notifications_list, key=lambda x: x.notification_id)
