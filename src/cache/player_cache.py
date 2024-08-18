from injector import inject

from cache.cache_interface import Cache
from aws.illyriad_db_dao import IllyriadDBDao
from data.player import Player
from typing import List

class PlayerCache(Cache):
    @inject
    def __init__(self, illyriad_db_dao: IllyriadDBDao):
        super().__init__(illyriad_db_dao)
        print(f'Initializing {self.__class__.__name__}')
        self.players: List[Player] = []

    def load(self, force: bool = False) -> None:
        if force or self.get_refresh_needed():
            self.__load_from_dao()
            self.set_refreshed()

    def get_players(self) -> List[Player]:
        return self.players

    def update_player_latest_notif_id(self, player: Player, latest_notif_id: str) -> None:
        self.illyriad_db_dao.update_player_latest_notif_id(player.player_id, latest_notif_id)
        player.latest_notif_id = latest_notif_id

    def set_refreshed(self) -> None:
        self.illyriad_db_dao.set_players_refreshed()

    def get_refresh_needed(self) -> bool:
        return self.illyriad_db_dao.get_player_refresh_needed()

    def __load_from_dao(self) -> None:
        items = self.illyriad_db_dao.scan_players()

        self.players = [Player(
            player_id=item['player_id'],
            discord_user_id=item['discord_user_id'],
            latest_notif_id=item['last_notification_id'],
            notif_api_key=item['notification_api_key'],
            ) for item in items]
