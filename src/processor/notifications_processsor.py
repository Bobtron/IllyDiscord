from injector import inject
from typing import List

from data.player import Player
from cache.metadata_cache import MetadataCache
from cache.player_cache import PlayerCache
from processor.player_notification_processor import PlayerNotificationProcessor


class NotificationsProcessor():
    @inject
    def __init__(self, metadata_cache: MetadataCache, player_cache: PlayerCache, player_notification_processor: PlayerNotificationProcessor):
        print(f'Initializing {self.__class__.__name__}')
        self.metadata_cache = metadata_cache
        self.player_cache = player_cache
        self.player_notification_processor = player_notification_processor

    def process_notifications(self):
        self.metadata_cache.load(force=True)
        self.player_cache.load(force=True)

        while True:
            players_list: List[Player] = self.player_cache.get_players()

            for player in players_list:
                self.player_notification_processor.process_player(player)
            
            self.metadata_cache.load()
            self.player_cache.load()

            # Remove when running in prod
            break
